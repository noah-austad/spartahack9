from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch')
def launch():
    return render_template('launch.html')

if __name__ == '__main__':
    app.run(port=5000)
