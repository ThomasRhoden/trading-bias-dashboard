import time
from app.models.market_engine import MarketEngine
from app.dao.market_data_dao import MarketDataDAO

def run_worker():
    print("Iniciando Worker de Automação (DAO Pattern)...")
    engine = MarketEngine()
    
    while True:
        try:
            print(f"Coletando dados: {time.ctime()}")
            dados = engine.obter_dados_mercado()
            
            # Utilizando o DAO (Fase 2)
            MarketDataDAO.salvar_registro(dados['vies'])
            
            print("Dados salvos via MarketDataDAO.")
            time.sleep(300)
        except Exception as e:
            print(f"Erro no worker: {e}")
            time.sleep(60)

if __name__ == "__main__":
    run_worker()