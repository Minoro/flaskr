import os

from flask import Flask

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flasker.sqlite')
    )
    
    if test_config is None:
        # Carrega a instancia de config, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega as configurações de teste
        app.config.from_mapping(test_config) 
        
    # Garante que a pasta da instância exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return 'Olá Mundo!'
    
    return app