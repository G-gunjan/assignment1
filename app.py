from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<p>About Page</p>"

@app.route('/contact')
def contact():
    return "<p>Contact Page</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"),debug=True)

