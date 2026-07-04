from flask import Blueprint, render_template
from app.models.market_engine import MarketEngine

# Cria um Blueprint para gerenciar as rotas principais. 
# Isso permite escalar o app dividindo-o em vários arquivos de rotas no futuro.
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    """
    Rota raiz da aplicação.
    Solicita os dados processados ao Model e os injeta na View (Template HTML).
    """
    # 1. Pede ao Model para fazer o "trabalho pesado" (Buscar e calcular)
    dados_operacionais = MarketEngine.obter_dados_mercado()
    
    # 2. Envia o pacote de dados pronto para o arquivo HTML renderizar na tela
    return render_template('dashboard.html', dados=dados_operacionais)