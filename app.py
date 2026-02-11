from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Python App Successfully Deployed on Azure 🚀"

if __name__ == "__main__":
    app.run()
