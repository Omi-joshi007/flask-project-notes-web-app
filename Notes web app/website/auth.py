from flask import Blueprint, render_template,request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods =['GET','POST'])
def login():
    return render_template('login.html',text='passing variable')

@auth.route('/logout')
def logout():
    return '<p>Logout page</p>'

@auth.route('/sign-up',methods =['GET','POST'])
def signup():
    if request.form == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Enter a valid email greater than 3 characters.',category='error')
        elif len(firstName) <2:
            flash('Enter a valid name greater than 1 character',category='error')
        elif password1 != password2:
            flash('Passwords don\'t match',category='error')
        elif len(password1 < 7):
            flash('Enter a valid password minimun 7 characters',category='error')
        else:
            flash('Account created successfully!!', category='success')
            
    return render_template('sign_up.html')