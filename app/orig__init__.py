# app/__init__.py
print("starting __init__.py")

from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')


from app.views import index

print("finished __init__.py")