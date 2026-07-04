from app.config.database import SessionLocal
from app.models.market_history import MarketHistory

class MarketDataDAO:
    @staticmethod
    def salvar_registro(vies):
        """Salva um novo registro de viés no histórico."""
        session = SessionLocal()
        try:
            novo_registro = MarketHistory(vies=vies)
            session.add(novo_registro)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def buscar_ultimo_registro():
        """Busca o registro mais recente."""
        session = SessionLocal()
        try:
            return session.query(MarketHistory).order_by(MarketHistory.id.desc()).first()
        finally:
            session.close()