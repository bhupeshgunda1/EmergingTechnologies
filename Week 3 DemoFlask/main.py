from flask import Flask, request, render_template

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return 'Hello World'

# http://127.0.0.1:5000/welcome ----using jinja2 template
@app.route('/welcome')
def hello_world1():
    return render_template('hello.html')

# http://127.0.0.1:5000/welcome/Bhupesh ----paraeter injection into jinja2 template
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', name=name) #passing parameter to template



@app.route('/user-data', methods=['POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        result = '''
                <h1> First Name: {}<h1>
                <h1> Last Name: {}<h1>
                '''
    return result.format(first_name, last_name)

# http://127.0.0.1:5000/user
@app.route('/user')
def user_form():
    return '''
    <form method='POST' action ="http://127.0.0.1:5000/user-data">
    <div> <label> First Name: <input type="text" value="first_name"> </label></div>
    <div> <label> Last Name: <input type="text" value="last_name"> </label></div>
    <input type="submit" value="submit"> 
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
