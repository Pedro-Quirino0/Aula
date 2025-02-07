import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from flask import render_template, url_for, redirect
from projeto import app
from forms import FormCadastrar
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='SensorAranha',
    autocommit=True
)

cursor = conexao.cursor()


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    formcadastrar = FormCadastrar()
    if formcadastrar.validate_on_submit():
        nome = formcadastrar.nome.data
        email = formcadastrar.email.data
        idade = formcadastrar.idade.data
        feedback = formcadastrar.feedback.data
        cursor.execute("INSERT INTO Usuario (nome, email, idade, feedback) VALUES (%s, %s, %s, %s);", (nome, email, idade, feedback))
        conexao.commit()
        return redirect(url_for('homepage'))
    return render_template("cadastro.html", form=formcadastrar)


@app.route("/resultado")
def resultado():
    cursor.execute("SELECT nome, email, idade, feedback FROM Usuario")
    usuarios = cursor.fetchall()
    return render_template("resultado.html", usuarios=usuarios)
