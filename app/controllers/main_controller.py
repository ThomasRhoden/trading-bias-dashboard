from flask import Blueprint, render_template
from app.models.market_engine import MarketEngine

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    dados_operacionais = MarketEngine.obter_dados_mercado()
    return render_template('dashboard.html', dados=dados_operacionais)