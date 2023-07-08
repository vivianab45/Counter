from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'secret'


@app.route('/')
def counter():
    if "count" not in session:
        session["count"]=1
    else:
        session["count"]+=1
    return render_template('index.html')

# @app.route('/destroy_session')
# def destroy():
#     session.clear()
#     return redirect('/')

@app.route('/increase',methods=['POST'])
def add_two():
    session['count']+=1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')












if __name__=="__main__":  
    app.run(debug=True)