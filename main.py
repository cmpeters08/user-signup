from flask import Flask, request, render_template, redirect
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/join')
def index():
    return render_template("signin.html",username='', username_error='', password='', pass_error='', verify_password='', pass_v_error='', email='', email_error='',submit='')

@app.route('/join', methods=['POST','GET'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']
        username_valid = True
        password_valid = True
        verify_password_valid = True
        email_valid = True
        
        username_error = ''
        
        if len(username) < 3:
            username_error = 'Username is too short, username must be between 3 and 20 characters in lenth'
            username_valid = False 
        if len(username) > 20:
            username_error = 'Username is too long, username must be between 3 and 20 characters in length'
            username_valid = False
        elif len(username) is 0:
            username_valid = False
            username_error = 'Please Enter a Username'
        for each_char in username:
            if each_char == ' ':
                username_error = 'Username may not contain spaces. Please enter valid username'
                username_valid = False
        if username_valid is False:
            return render_template ("signin.html",username='', username_error=username_error, password='', pass_error='', verify_password='', pass_v_error='', email=email, email_error='')

        pass_error = ''
        if len(password) < 3:
            pass_error = 'Password is too short, username must be between 3 and 20 characters in lenth'
            password_valid = False
        if len(password) > 20:
            pass_error = 'Password is too long, username must be between 3 and 20 characters in length'
            password_valid = False      
        elif len(password) is 0:
            password_valid = False
            pass_error = 'Please Enter a Password'    
        for each_char in password:
            if each_char == ' ':
                pass_error = 'Password may not contain spaces. Please enter valid password'
                password_valid = False
        if password_valid is False:
            return render_template("signin.html",username=username, username_error='', password='', pass_error=pass_error, verify_password='', pass_v_error='', email=email, email_error='')

        pass_v_error = ''
        if verify_password != password:
            pass_v_error = 'Passwords do not match, please re-enter password'
            verify_password_valid = False
            if len(verify_password) is 0:
                pass_v_error = 'Please re-enter the password from above'
            verify_password_valid = False
        if verify_password_valid is False:
            return render_template("signin.html",username=username, username_error='', password='', pass_error='', verify_password='', pass_v_error=pass_v_error, email=email, email_error='')


        email_error = ''
        #at and dot are used as counters to verify only one @ and one . will be in the email.
        at = 0
        dot = 0
        if len(email) is not 0:
            if len(email) < 3:
                email_valid = False
                email_error = 'Email too short. Email must be between 3 and 20 characters in length'
            if len(email) > 20:
                email_valid = False
                email_error = 'Email too long. Email must be between 3 and 20 characters in lenth'
            for each_char in email:
                if each_char == '@':
                    at = at + 1
                    if at != 1:
                        email_valid = False
                        email_error = "You need one @ symbol in your email"
            for each_char in email:
                if each_char == '.':
                    dot = dot + 1
                    if dot != 1:
                        email_valid = False
                        email_error = "You only need one dot (.) in your email"
                    
        if email_valid is False:
            return render_template("signin.html",username=username, username_error='', password='', pass_error='', verify_password='', pass_v_error='', email='', email_error=email_error)

        
        return redirect('/success?username={}'.format(username) )

    #else:
        #return render_template("signin.html",username='', username_error='', password='', pass_error='', verify_password='', pass_v_error='', email='', email_error='')
        
@app.route('/success', methods=['GET'])
def post_it():
    username = request.args.get('username')
    #password = request.args.get('password')
    #verify_password = request.args.get('verify_password')
    #email = request.args.get('email')
    return render_template('success.html', username=username)

app.run()