from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    news_list = [
        "AI теперь умеет писать стихи!",
        "Вышла новая версия ChatGPT.",
        "Роботы учатся понимать юмор."
    ]
    return render_template("index.html", news_list=news_list)

if __name__ == "__main__":
    app.run(debug=True)
from flask import send_from_directory
import os

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)
