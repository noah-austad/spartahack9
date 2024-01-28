from options_data import stock, trending_req
from flask import Flask, render_template, request
from json2table import convert
import json
from pricing import bearspread, bullspread, butterflyspread

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
    #asset.update_prices()
    recent=['187.4200', '190.4300', '173.9300', '173.9400', '172.8300', '171.4800', '166.8400', '166.0800', '166.9600', '165.8000', '162.1600', '161.2300', '160.0800', '161.1400']
    return render_template('strategies.html', recent=recent, ticker=asset.ticker)

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

@app.route('/math', methods=['POST'])
def math():
    e1 = request.form.get('e1')
    e2 = request.form.get('e2')
    s=request.form.get('S')
    referer = request.headers.get('Referer')
    print(referer)
    if 'bear' in referer:
        cost=bearspread(e1,e2,s)
    elif 'bull' in referer:
        cost=bullspread(e1,e2,s)
    elif 'butterfly' in referer:
        cost=butterflyspread(e1,e2,s)
    else:cost=0
    return render_template('math.html',cost=cost)

if __name__ == '__main__':
    app.run(port=5000)
