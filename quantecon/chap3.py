import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo 
    import numpy as np 
    import pandas as pd 
    import matplotlib.pyplot as plt 
    return mo, np, plt


@app.cell
def _(mo):
    mo.md("#Plotting White Noise Process")
    return


@app.cell
def _(np, plt):
    epsilon_values = np.random.randn(100)
    plt.plot(epsilon_values)
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("#Bank Balance Application")
    return


@app.cell
def _(np, plt):
    r = 0.025 # interest rate 
    T = 50 # end date 
    b = np.empty(T+1)
    b[0] = 10 # init balance 

    for t in range(T):
        b[t+1] = (1 + r) * b[t]
    plt.plot(b, label='bank balance')
    plt.legend()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md("#Exercises")
    return


@app.cell
def _(mo):
    mo.md("##Exercise 3.1")
    return


@app.cell
def _(np, plt):
    def _():
        alpha = 0.9 
        t_end = 200 
        x = np.empty(t_end+1)
        x[0] = 0 
        for t in range(t_end):
            x[t+1] = alpha * x[t] + np.random.randn()
        plt.plot(x)
        return plt.show()


    _()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
