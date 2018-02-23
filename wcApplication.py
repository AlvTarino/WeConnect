#from flask import Flask,request, jsonify, make_response
from flask import *
from functools import *
from models.wcUser import wcUser

app = Flask(__name__)

wcuser_accounts = {}
wcUser = wcUser()

"""
@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.email or not auth.password:
        return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login required"'})
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login required"'})
"""
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap

#Route to main page after login
@app.route('/base')
@login_required
def base():
    descriptions = user.business
    return render_template('base.html', descriptions=descriptions)

#Route to enable user signup
#@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        flash("You have succesfully been registered {} {}".format(name, password))
        if name and password:
            users[email] = password
            return redirect(url_for('login'))
    return render_template('create_account.html', error=error)

#Route enables user to login after registration
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] not in users.keys() or request.form['password'] not in users.values():
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('base'))
    return render_template('login.html', error=error)

#Route enables user to add business idea
@app.route('/add_a_business_idea', methods=['GET', 'POST'])
@login_required
def add_a_business_idea():
    error = None
    if request.method == 'POST':
        business_name = request.form['business_name']
        business_description = request.form['business_description']
        flash("You have successfully added registered {} {}".format(business_name, business_description))
        if business_name and business_description:
            user.create_business(business_name, business_description)
            return redirect(url_for('base'))
    return render_template('update_business.html', error=error)

#Route enables user to add a business description
@app.route('/add_a_description/<business_name>', methods=['GET', 'POST'])
@login_required
def add_a_description(business_name):
    error = None
    if request.method == 'POST':
        business_name = request.form['business_name']
        business_description = request.form['business_description']
        flash("You have succesfully added registered {} {}".format(business_name, business_description))
        if business_name and business_description:
            user.add_business_description(business_name, business_description)
            return redirect(url_for('description', business_name=business_name))
    return render_template('update_business.html', business_name=business_name, error=error)

#Route logs out user from the site
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect(url_for('login'))

@app.route('/description/<business_name>')
@login_required
def description(business_name):
    business_description = user.read_business(business_name)
    return render_template('read_review.html', business_description=business_description, business_name=business_name)

#Route enables user to delete business description
@app.route('/delete/<business_name>/<description>')
@login_required
def delete(business_name, description):
    user.delete_business_description(business_name, description)
    return redirect(url_for('description', business_name=business_name))
    return render_template('view_business.html')

#Route enables user to delete business
@app.route('/delete_business/<business_name>')
@login_required
def delete_business(business_name):
    user.delete_business(business_name)
    return redirect(url_for('base'))
    return render_template('base.html')

#Route enables user to edit business
@app.route('/update_a_business/<business_name>', methods=['GET', 'POST'])
@login_required
def update_a_business(business_name):
    error = None
    if request.method == 'POST':
        business_name = request.form['business_name']
        new_name = request.form['new_name']
        flash("You have succesfully added registered {} {}".format(business_name, new_name))
        if business_name and new_name:
            user.update_business(business_name, new_name)
            return redirect(url_for('base',business_name=business_name))
    return render_template('update_business.html',business_name=business_name)

#Route enables user to edit business_description
@app.route('/update_a_business_description/<business_name>/<description>', methods=['GET', 'POST'])
@login_required
def update_a_business_description(business_name, description):
    error = None
    if request.method == 'POST':
        business_name = request.form['business_name']
        description = request.form['description']
        new_name = request.form['new_description']
        flash("You have succesfully added registered {} {} {}".format(business_name, description, new_name))
        if business_name and description:
            user.update_business_description(business_name, description, new_name)
            return redirect(url_for('description', business_name=business_name, description=description))
    return render_template('view_business.html', business_name=business_name, description=description)

if __name__=='__main__':
    app.run(debug=True)
