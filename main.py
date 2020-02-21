import unittest

from flask import request, make_response, redirect, render_template, session, url_for, flash
from random import randint
from app import create_app
from app.froms import LoginForm
import app.db_service as db

app = create_app()

TODOS = ['Comprar Cafe', 'Enviar solicitud de compra', 'Retirar producto']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET'])
def hello_world():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'list_todos': TODOS,
        'login_form': login_form,
        'username': username
    }
    return render_template('hello.html', **context)


@app.route('/base', methods=['GET', 'POST'])
def get_user_database():
    password = 'myPassword{}'.format(randint(0,99))
    user_in = 'Pepe{}'.format(randint(0,99))
    db.create_user(user_in,password)
    users = db.get_users()
    for user in users:
        print(user.printInfo())
    return 'Good'


if __name__ == '__main__':
    app.run()
