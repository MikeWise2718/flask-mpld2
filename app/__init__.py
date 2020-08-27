# app/__init__.py
print("starting __init__.py")

from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt
import numpy as np
import mpld3


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

from . import index
from . import simple

if __name__ == "__main__":
    print("__name__==\"__main__\" so invoking app.run(...)")
    app.run(threaded=False)

print("finished __init__.py")