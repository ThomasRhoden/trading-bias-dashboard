import time
from tradingview_ta import TA_Handler, Interval

class MarketEngine:
    """
    Classe responsável por concentrar as regras de negócio relacionadas 
    à leitura de mercado e cálculo de viés operacional.
    """
    
    # Sistema de Cache: Evita banimento da API e deixa a tela instantânea
    _cache_dados = None
    _ultimo_update = 0
    _TEMPO_CACHE_SEGUNDOS = 300  # 5 minutos (300 segundos)

    @classmethod
    def obter_dados_mercado(cls):
        tempo_atual = time.time()

        # 1. Verifica se o cache existe e ainda está dentro da validade (menos de 5 minutos)
        if cls._cache_dados and (tempo_atual - cls._ultimo_update) < cls._TEMPO_CACHE_SEGUNDOS:
            print("[LOG] Retornando dados da Memória CACHE (Super Rápido)")
            return cls._cache_dados
            
        print("[LOG] Buscando dados atualizados no TradingView...")

        config_ativos = {
            "S&P 500 (ETF SPY)": {"symbol": "SPY", "exchange": "AMEX", "screener": "america"},
            "EWZ (ETF Brasil NY)": {"symbol": "EWZ", "exchange": "AMEX", "screener": "america"},
            "Petróleo WTI (ETF USO)": {"symbol": "USO", "exchange": "AMEX", "screener": "america"},
            "VALE3 (B3)": {"symbol": "VALE3", "exchange": "BMFBOVESPA", "screener": "brazil"}
        }
        
        resultados = {}
        soma_variacoes = 0.0

        for nome, config in config_ativos.items():
            try:
                handler = TA_Handler(
                    symbol=config["symbol"],
                    exchange=config["exchange"],
                    screener=config["screener"],
                    interval=Interval.INTERVAL_1_DAY
                )
                analise = handler.get_analysis()
                
                preco_atual = analise.indicators.get("close", 0.0)
                preco_abertura = analise.indicators.get("open", 0.0)
                
                if preco_abertura > 0:
                    variacao = ((preco_atual - preco_abertura) / preco_abertura) * 100
                else:
                    variacao = 0.0

                resultados[nome] = {
                    "preco": round(preco_atual, 2),
                    "variacao": round(variacao, 2)
                }
                soma_variacoes += variacao

            except Exception as erro:
                print(f"[LOG] Erro ao buscar {nome} no TradingView: {erro}")
                resultados[nome] = {"preco": "Indisponível", "variacao": 0.0}

        if soma_variacoes > 0.5:
            vies_final = "COMPRA (Confluência Macro de Alta)"
            cor_vies = "success"
        elif soma_variacoes < -0.5:
            vies_final = "VENDA (Confluência Macro de Baixa)"
            cor_vies = "danger"
        else:
            vies_final = "NEUTRO (Mercado Misto / Cuidado com consolidação)"
            cor_vies = "warning"

        resultado_final = {"ativos": resultados, "vies": vies_final, "classe_cor": cor_vies}
        
        # 2. Salva o resultado no cache antes de devolver para o Controller
        cls._cache_dados = resultado_final
        cls._ultimo_update = tempo_atual

        return resultado_final