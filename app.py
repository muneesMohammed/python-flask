from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route("/contact")
def contact():
    return "<h2> welcome to contact page </h2>"

# app.run()
if __name__=="__main__":
    app.run(debug=True)