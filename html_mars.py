from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def main_web():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return ("И на Марсе будут яблони цвести!")

@app.route('/promotion')
def ad_text():
    countdown_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(countdown_list)

@app.route('/image_mars')
def image():
    return render_template('image.html')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')