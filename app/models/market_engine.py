from tradingview_ta import TA_Handler, Interval

class MarketEngine:
    @staticmethod
    def obter_dados_mercado():
        # Configuração dos ativos usando ETFs hiper líquidos para garantir estabilidade da API
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
                # Conecta no TradingView e puxa os dados do gráfico Diário
                handler = TA_Handler(
                    symbol=config["symbol"],
                    exchange=config["exchange"],
                    screener=config["screener"],
                    interval=Interval.INTERVAL_1_DAY
                )
                analise = handler.get_analysis()
                
                # Coleta os indicadores atuais
                preco_atual = analise.indicators.get("close", 0.0)
                preco_abertura = analise.indicators.get("open", 0.0)
                
                # Calcula a variação percentual do dia
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
                # Se algo falhar, printa no terminal para você debugar, mas não quebra a tela
                print(f"Erro ao buscar {nome} no TradingView: {erro}")
                resultados[nome] = {"preco": "Indisponível", "variacao": 0.0}

        # Lógica de negócio baseada na confluência macro
        if soma_variacoes > 0.5:
            vies_final = "COMPRA (Confluência Macro de Alta)"
            cor_vies = "success"
        elif soma_variacoes < -0.5:
            vies_final = "VENDA (Confluência Macro de Baixa)"
            cor_vies = "danger"
        else:
            vies_final = "NEUTRO (Mercado Misto / Cuidado com consolidação)"
            cor_vies = "warning"

        return {"ativos": resultados, "vies": vies_final, "classe_cor": cor_vies}