# 🚀 Roadmap: Evolução do Sistema para Arquitetura Corporativa

Este documento mapeia a transição do nosso protótipo para um sistema robusto, baseado em padrões de engenharia de software (DAO/Repository) e persistência de dados (PostgreSQL).

## 📋 Objetivos Estratégicos
- [ ] Implementar persistência de dados real (PostgreSQL).
- [ ] Abstrair o acesso a dados através do padrão DAO.
- [ ] Criar uma camada de validação e limpeza de dados (Data Integrity).
- [ ] Gerenciamento dinâmico de ativos B3 via banco de dados.

## 📅 Etapas de Execução

### Fase 1: Infraestrutura e Modelagem
- [ ] Configuração do ambiente (SQLAlchemy + psycopg2).
- [ ] Mapeamento das Classes de Modelo (Representação SQL das tabelas).
- [ ] Configuração do Banco de Dados PostgreSQL (Local ou Nuvem).

### Fase 2: Camada de Acesso a Dados (DAO)
- [ ] Criação da pasta `app/dao/`.
- [ ] Implementação do `AssetDAO` (Gestão de quais ativos monitorar).
- [ ] Implementação do `MarketDataDAO` (Escrita/Leitura de preços).

### Fase 3: Validação e Lógica (Service Layer)
- [ ] Criação de validadores (checkers) para dados vindos da API.
- [ ] Implementação da lógica de sanitização (evitar dados corrompidos no SQL).

### Fase 4: O "Registry" de Ativos da B3
- [ ] Criação da Tabela `ativos_b3` (Ticker, Nome, Setor, Flag de Ativo).
- [ ] Script de carga inicial para importar o IBOV.
- [ ] Integração do sistema de coleta para ler dessa tabela em vez de hardcode.

### Fase 5: Refatoração do "Cérebro" (Business Logic)
- [ ] Ajustar o `MarketEngine` para consumir os DAOs.
- [ ] Garantir que a matemática e a decisão de viés permaneçam isoladas da interface.