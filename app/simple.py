from app import app
from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import io
import base64

def get_simple_plot():
    print("get_simple_plot invoked")
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()
    return fig

@app.route("/simple")
def simple():
    print("simple route invoked")
    fig = get_simple_plot()


    myfig = mpld3.fig_to_html(fig, template_type='simple')

    plt.clf() # clear figure
    plt.cla() # clear axes
    plt.close('all') # close all figures

    # Print as HTML
    return myfig    



def cvt_fig_to_b64(fig):
    buf = io.BytesIO()
    fig.savefig(buf,format="jpg")
    buf.seek(0)
    b64data = base64.b64encode(buf.getvalue())
    retval = b64data.decode('utf8')
    return retval

@app.route("/simple1")
def simple1():
    print("simple1 route invoked")
    fig = get_simple_plot()


    b64 = cvt_fig_to_b64(fig)

    rtemp = render_template('simpleplot.html',title="a simple1 plot", fig=b64 )
    return  rtemp

    # Print as HTML
    return myfig    

@app.route("/simple2")
def simple2():
    print("simple2 route invoked")

    fig = get_simple_plot()
    myfig = mpld3.fig_to_html(fig, template_type='simple')

    plt.clf() # clear figure
    plt.cla() # clear axes
    plt.close('all') # close all figures


    rtemp = render_template('simpleplot2.html',title="a simple2 plot", mpld2code=myfig )
    return  rtemp

    # Print as HTML
    return myfig    



