from app import app
from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt
import numpy as np
import mpld3


@app.route("/")
@app.route("/index")
def temperature():
    print("index route invoked")
    date = ([1, 2, 3, 4])
    y = ([1, 2, 3, 4])

    fig = plt.figure(figsize=(10, 5))
    plt.title('Temperature', fontsize=15)
    plt.ylabel('Temperature' + u'u2103', fontsize=15)

    plt.plot(date, y, 'b-')
    plt.ylim([0, 40])

    myfig = mpld3.fig_to_html(fig, template_type='simple')

    plt.clf() # clear figure
    plt.cla() # clear axes
    plt.close('all') # close all figures

    # Print as HTML
    return myfig

# if __name__ == "__main__":