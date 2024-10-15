from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/our_team')
def our_team():
    return render_template('our_team.html')

@app.route('/portfolios')
def portfolios():
    return render_template('portfolios.html')

@app.route('/news_and_events')
def news_and_events():
    return render_template('news_and_events.html')

if __name__ == '__main__':
    app.run(host='10.33.46.70', port=3000, debug=True)