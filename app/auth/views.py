from . import auth
from app.froms import LoginForm
from flask import render_template, session, redirect, flash, url_for


@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': LoginForm()
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de Usuario Registrado con exito')
        return redirect(url_for('index'))
    return render_template('login.html', **context)
