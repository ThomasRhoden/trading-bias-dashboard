from app.dao.ativo_dao import AtivoDAO
from app.models.ativos import AtivoB3
from app.config.database import SessionLocal

def popular_banco():
    # Vamos limpar os antigos se precisar (opcional)
    session = SessionLocal()
    session.query(AtivoB3).delete()
    
    ativos = [
        ("SPY", "S&P 500", "Índice", "AMEX", "america"),
        ("EWZ", "EWZ Brasil", "Índice", "AMEX", "america"),
        ("USO", "Petróleo", "Commodity", "AMEX", "america"),
        ("VALE3", "Vale S.A.", "Mineração", "BMFBOVESPA", "brazil"),
        ("PETR4", "Petrobras", "Petróleo", "BMFBOVESPA", "brazil")
    ]
    
    for t, n, s, ex, sc in ativos:
        novo = AtivoB3(ticker=t, nome=n, setor=s, exchange=ex, screener=sc)
        session.add(novo)
    
    session.commit()
    session.close()
    print("Banco populado com sucesso!")

if __name__ == "__main__":
    popular_banco()