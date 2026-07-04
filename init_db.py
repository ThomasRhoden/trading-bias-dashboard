from app.config.database import engine, Base
# Importar todos os modelos é obrigatório para o create_all funcionar
from app.models.ativos import AtivoB3
from app.models.market_history import MarketHistory

def init_db():
    print("Criando/Atualizando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_db()