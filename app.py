from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Главная страница"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Страница «О проекте»"""
    return render_template('about.html')

@app.route('/test')
def test():
    """Базовая страница"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    