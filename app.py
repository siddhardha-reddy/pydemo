from flask import Flask,render_template,request,redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('signup.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/add')
def add():
    k=request.form['task']
    #sql query to add task
    #commit tasks
    return redirect('/showtasks')
@app.route('/showtasks')
def showtasks():
    tasks=[]#code to retrive tasks in db
    return render_template('showtasks.html',tasks)

if(__name__=="__main__"):
    app.run(debug=True)
