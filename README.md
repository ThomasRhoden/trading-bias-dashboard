# 📊 Trading Bias Dashboard

> 🇧🇷 Painel macroeconômico em Flask (MVC) para leitura de mercado pré-abertura.
> 🇺🇸 Flask (MVC) macro dashboard for pre-market reading.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white) ![Status](https://img.shields.io/badge/status-descontinuado%20%2F%20discontinued-lightgrey)

## 📖 Visão geral

Consolida dados macroeconômicos e entrega um viés estatístico direcional para o dia, com separação estrita de responsabilidades (MVC + DAO). Pode rodar ao lado de plataformas de trading como apoio analítico. **Não é recomendação de investimento.**

<details><summary>🇺🇸 English</summary>

Consolidates macro data and outputs a directional statistical bias for the day, with strict separation of concerns (MVC + DAO). Meant to run alongside trading platforms as an analytical aid. **Not investment advice.**
</details>

## ✨ Funcionalidades · Features

- Dados do TradingView via `tradingview_ta` (AMEX, BMFBOVESPA) / *TradingView data via `tradingview_ta`*
- Cálculo de viés ponderando SPY, USO, EWZ e VALE3 / *Bias computed by weighting SPY, USO, EWZ and VALE3*
- Worker (`worker.py`) que coleta e grava o histórico no banco / *Worker that collects and stores history*
- Dashboard web em Bootstrap 5

## 🧰 Stack

Python 3 · Flask 3 · tradingview_ta · pandas · SQLAlchemy + PostgreSQL (psycopg2) · python-dotenv · HTML/CSS/Bootstrap 5

## 🧱 Arquitetura · Architecture

```
main.py              # Flask app factory (create_app)
worker.py            # coleta periódica / periodic collector
init_db.py, seed_db.py, load_ibov.py
app/
├── config/database.py   # conexão via .env / connection from .env
├── controllers/main_controller.py
├── dao/                 # ativo_dao, market_data_dao
├── models/              # ativos, market_engine, market_history
└── views/templates/dashboard.html
```

## 🚀 Como executar · How to run

```bash
git clone https://github.com/ThomasRhoden/trading-bias-dashboard.git
cd trading-bias-dashboard
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install sqlalchemy psycopg2-binary python-dotenv   # ainda não estão no requirements / not yet in requirements
```

Crie um `.env` com / Create a `.env` with: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME` (PostgreSQL).

```bash
python init_db.py     # cria tabelas / creates tables
python seed_db.py     # dados iniciais / seed data
python main.py        # http://127.0.0.1:5000
python worker.py      # opcional: coleta contínua / optional: continuous collection
```

## 📍 Status

Descontinuado, mantido como portfólio / Discontinued, kept as portfolio. Roadmap original e diretrizes em [PROJECT_ROADMAP.md](./PROJECT_ROADMAP.md) e [GUIDELINES.md](./GUIDELINES.md).


## 👤 Autor · Author

**Thomas Rhoden Gonçalves** — Suporte de TI que programa e usa IA / IT support who codes and uses AI  
✉️ rhodenthomas@gmail.com · [github.com/ThomasRhoden](https://github.com/ThomasRhoden)
