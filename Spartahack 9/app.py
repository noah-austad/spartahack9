from options_data import stock, trending_req
from flask import Flask, render_template, request
from json2table import convert
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch')
def launch():
    return render_template('launch.html')

@app.route('/trending')
def trending():
    raw_data=trending_req()
    table=json.loads(raw_data)
    
    return render_template('trending.html',table=table)

@app.route('/strategies', methods=['POST'])
def strategies():
    ticker_str = request.form['user_input']
    asset=stock(ticker_str)
    asset.update_prices()
    return render_template('strategies.html', recent=asset.price_history, ticker=asset.ticker)

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/bull')
def bull():
    return render_template('bull.html')

@app.route('/bear')
def bear():
    return render_template('bear.html')

@app.route('/butterfly')
def butterfly():
    return render_template('butterfly.html')


if __name__ == '__main__':
    app.run(port=5000)
