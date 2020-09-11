from flask import Flask
import os
import dlib

app = Flask(__name__)

print("hello world")

wsgi_app = app.wsgi_app

if __name__ == "__main__":

    app.run()
