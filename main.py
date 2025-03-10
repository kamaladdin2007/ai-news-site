from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    news_list = [
        "AI теперь умеет писать стихи!",
        "Вышла новая версия ChatGPT.",
        "Роботы учатся понимать юмор."
    ]
    return render_template("index.html", news_list=news_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
