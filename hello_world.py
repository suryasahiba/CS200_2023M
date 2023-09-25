from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Group name : VOYAGE (23) \n PERUMALLU MALLUKARJUN 12041030 \n SOUMEN \n"


if __name__ == "__main__":
    app.run()
