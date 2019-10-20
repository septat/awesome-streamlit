"""This example is a Streamlit implementation of an interactive Gaussian plot.

The purpose of this example is to test what we can do and cannot (yet) do in Streamlit compared
to [Voila](https://github.com/voila-dashboards/voila) and
list how the development experience and the end result compares

The benchmark example from Voila is https://github.com/voila-gallery/gaussian-density

Author: Marc Skov Madsen https://github.com/marcskovmadsen

"""
import streamlit as st
import numpy as np
from scipy.stats import norm
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def write():
    intro_section()
    plot_streamlit_section()
    plot_voila_section()
    findings_section()


def plot_streamlit_section():
    st.markdown(
        """
## Plot - Streamlit

"""
    )
    x = get_x()
    mu = st.slider(
        "mu", value=float(0), min_value=float(-5), max_value=float(5), step=float(0.1)
    )
    sigma = st.slider(
        "sigma",
        value=float(1),
        min_value=float(0.1),
        max_value=float(5),
        step=float(0.1),
    )
    # Cannot use plotly as it crashes
    # plot_figure_matplotlib(x, mu, sigma)
    plot_figure_plotly(x, mu, sigma)


def plot_voila_section():
    st.markdown(
        """
## Plot - Voila

We compare to the Gaussian Density plot in the Voila Gallery. See

- [Source](https://github.com/voila-gallery/gaussian-density)
- [Binder](https://mybinder.org/v2/gh/voila-gallery/gaussian-density/master?urlpath=voila%2Frender%2Findex.ipynb)

![Reference](interactive_gaussian_plot_reference.png)
"""
    )


def intro_section():
    st.markdown(
        """
# Interactive Gaussian Plot

## Introduction

This example is a Streamlit implementation of an interactive Gaussian plot.

The purpose of this example is to test what we can do and cannot (yet) do in Streamlit compared
to [Voila](https://github.com/voila-dashboards/voila) and
list how the development experience and the end result compares

"""
    )


def findings_section():
    st.markdown(
        """
## Findings

### Pros of Voila

- The plot **updates very, very fast** when the user changes the mu and sigma settings
- Well tested slider widget
- Layout options like HBox and VBox. But for this example they are not nescessary.

### Pros of Streamlit

- Very fast and simple development cycle of develop-test-refactor
because of very fast, automatic hot reload.
- You can use your one editor of choice
  - Streamlit does not require knowing something like how to install and use a notebook editor.
  - You you can use integrated, automatic tests like pylint, mypy etc. to help  produce quality code.
- End result is a code file that works very well with Git.
- End result can very easily be deployed to multiuser production ready server.

### Issues

Both Streamlit and Jupyter Notebook crashed during development

- Streamlit:
  - [Matplotlib Crash issue 469](https://github.com/streamlit/streamlit/issues/469)
  - [Slider issue 470](https://github.com/streamlit/streamlit/issues/470)
"""
    )


@st.cache
def get_x():
    return np.linspace(-10, 10, 200)


def plot_figure_matplotlib(x, mu: float = 0, sigma: float = 1):
    y = norm.pdf(x, mu, sigma)
    title = f"Gaussian Density (mu = {mu} and sigma = {sigma})"
    plt.scatter(x=x, y=y)
    st.pyplot()


def plot_figure_plotly(x, mu: float = 0, sigma: float = 1):
    y = norm.pdf(x, mu, sigma)
    dataframe = pd.DataFrame({"x": x, "y": y})
    title = f"Gaussian Density (mu = {mu:.2} and sigma = {sigma:.2})"
    fig = px.line(dataframe, x="x", y="y", title=title)
    st.plotly_chart(fig)


write()
