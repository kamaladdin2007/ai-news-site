from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AI News</title>
        </head>
        <body>
            <h1>Последние новости</h1>
            <ul>
                <li><strong>Новости 1:</strong> AI теперь умеет писать стихи!</li>
                <li><strong>Новости 2:</strong> Вышла новая версия ChatGPT.</li>
                <li><strong>Новости 3:</strong> Роботы учатся понимать юмор.</li>
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
