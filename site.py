from flask import Flask, render_template

app = Flask(__name__)


menu = ['Установка', 'Первое приложение', 'Обратная связь']

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title = 'About Flack', menu=menu)

@app.route("/about")
def about():
    return '<h1>О Сайте</h1>'

@app.route("/author")
def author():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=True)