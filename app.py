from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
  return render_template('home.html')
  
@app.route("/contact_me")
def cont_world():
  return render_template('contact.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)