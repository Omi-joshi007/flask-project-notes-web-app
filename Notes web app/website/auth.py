from flask import Blueprint, render_template,request, flash, redirect , url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash 
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Succesfully.', category='success')
                login_user(user, remember=True)
            else:
                flash('Try again, incorrect password.', category='error')
        else:
            flash('Email does not exsist.', category='error')
    return render_template('login.html',text='passing variable')

@auth.route('/logout')
@login_required
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email)
        if user:
            flash('This email already exsist.', category='error')
        elif len(email) < 4:
            flash('Enter a valid email greater than 3 characters.',category='error')
        elif len(firstName) <2:
            flash('Enter a valid name greater than 1 character',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match',category='error')
        elif len(password1) < 7:
            flash('Enter a valid password minimun 7 characters',category='error')
        else:
            new_user = User(email = email,firstName = firstName,password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created successfully!!', category='success')
            return redirect(url_for('views.home'))
            
    return render_template('sign_up.html')