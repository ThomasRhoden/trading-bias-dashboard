from app.models.market_engine import MarketEngine

def run_test():
    print("--- Iniciando Teste de Integração (DB + Engine + Validação) ---")
    
    engine = MarketEngine()
    resultado = engine.obter_dados_mercado()
    
    print(f"\nViés do Mercado: {resultado['vies']}")
    print("-" * 30)
    print("Detalhe dos Ativos:")
    for nome, dados in resultado['ativos'].items():
        print(f"{nome:20} | Preço: {str(dados['preco']):>10} | Var: {dados['variacao']}%")
    
    print("\n--- Teste Concluído ---")

if __name__ == "__main__":
    run_test()