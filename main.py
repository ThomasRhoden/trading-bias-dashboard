from app import create_app

# Inicializa a aplicação configurada através do padrão "Application Factory"
app = create_app()

if __name__ == '__main__':
    # Inicia o servidor web interno do Flask.
    # debug=True permite que o servidor recarregue sozinho ao salvar alterações no código.
    app.run(debug=True, port=5000)