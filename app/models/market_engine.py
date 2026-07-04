import time
from tradingview_ta import TA_Handler, Interval
from app.dao.ativo_dao import AtivoDAO

class MarketEngine:
    _cache_dados = None
    _ultimo_update = 0
    _TEMPO_CACHE_SEGUNDOS = 300 

    @classmethod
    def _carregar_ativos_do_banco(cls):
        """Busca os ativos autorizados no banco de dados."""
        ativos_db = AtivoDAO.listar_ativos_ativos()
        configuracoes = []
        for ativo in ativos_db:
            configuracoes.append({
                "nome": ativo.nome,
                "symbol": ativo.ticker,
                "exchange": ativo.exchange,
                "screener": ativo.screener
            })
        return configuracoes

    def _validar_dados(self, preco, abertura):
        """Validação de integridade dos dados recebidos."""
        if preco is None or abertura is None:
            return False
        if preco <= 0 or abertura <= 0:
            return False
        return True

    @classmethod
    def obter_dados_mercado(cls):
        tempo_atual = time.time()

        # Verifica Cache
        if cls._cache_dados and (tempo_atual - cls._ultimo_update) < cls._TEMPO_CACHE_SEGUNDOS:
            print("[LOG] Retornando dados da Memória CACHE")
            return cls._cache_dados
            
        print("[LOG] Buscando dados atualizados no TradingView via DB...")
        
        # DEFINIÇÃO DA VARIÁVEL QUE CAUSOU O ERRO
        lista_ativos = cls._carregar_ativos_do_banco()
        
        resultados = {}
        soma_variacoes = 0.0

        # Loop principal
        for config in lista_ativos:
            try:
                handler = TA_Handler(
                    symbol=config["symbol"],
                    exchange=config["exchange"],
                    screener=config["screener"],
                    interval=Interval.INTERVAL_1_DAY
                )
                analise = handler.get_analysis()
                
                preco_atual = analise.indicators.get("close")
                preco_abertura = analise.indicators.get("open")
                
                # Validação
                if not cls()._validar_dados(preco_atual, preco_abertura):
                    print(f"[ALERTA] Dados inválidos para {config['symbol']}. Pulando.")
                    resultados[config["nome"]] = {"preco": "Dados Corrompidos", "variacao": 0.0}
                    continue

                variacao = ((preco_atual - preco_abertura) / preco_abertura) * 100
                
                resultados[config["nome"]] = {
                    "preco": round(preco_atual, 2),
                    "variacao": round(variacao, 2)
                }
                soma_variacoes += variacao

            except Exception as erro:
                print(f"[LOG] Erro ao buscar {config['nome']}: {erro}")
                resultados[config["nome"]] = {"preco": "Indisponível", "variacao": 0.0}

        # Cálculo de viés
        if soma_variacoes > 0.5:
            vies_final = "COMPRA (Confluência Macro de Alta)"
            cor_vies = "success"
        elif soma_variacoes < -0.5:
            vies_final = "VENDA (Confluência Macro de Baixa)"
            cor_vies = "danger"
        else:
            vies_final = "NEUTRO (Mercado Misto)"
            cor_vies = "warning"

        resultado_final = {"ativos": resultados, "vies": vies_final, "classe_cor": cor_vies}
        
        cls._cache_dados = resultado_final
        cls._ultimo_update = tempo_atual

        return resultado_final