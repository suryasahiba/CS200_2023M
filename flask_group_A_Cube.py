from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Group name : A-Cube \n Aakash Thatte - 12041590 \n Amogh Joshi - 12040120 \n Aman Vishnoi - 12040090\n"

if __name__ == '__main__':
   app.run()