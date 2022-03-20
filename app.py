
#Chama as biblitecas do Flask e Flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__,template_folder='template',static_folder='static')

#antes de usar nao esqueça de instalar o python e tambem o flask com o comando pip install flask e o pip install flask_sqlalchemy
#Boms estudos ;)


#Na pasta static pode adicionar seus arquivos css e js
#funcoes para retornar html
#voce pode adicionar mais funcoes ou modificar essas.


@app.route("/", methods=['GET'])
def home():
    #renderiza pagina html home

    return render_template('index.html')

@app.route("/dashboard", methods=['GET'])
def dashboard():
    #renderiza pagina html dashboard
    return render_template('dashboard.html')


@app.route("/tabela", methods=['GET'])
def tabela():
    return render_template('tabela.html')

if __name__ == '__main__':
    app.run(debug=True)
