# Environment Setup 
This is my environment setup for machine learing and python projects. The scientific packages are what I use for my default setup 

## Python Version 
For python version, I use whichever version is currently supported by pytorch -> 3.12 right now. 
*installation* - uv python pin 3.12 

## Dependencies 
*installation* - uv add 
### Scientific Packages 
- numpy 
- matplotlib 
- scipy 
- pandas 
- sympy

## Dev Dependcies 
*installation* - uv add --dev 
- jupyter-lab 
- pytest 
- ruff 

## Other Dependencies 
Depending on the project, I usually use one or more of these packages
### Machine Learning 
- scikit-learn 
### Probabilistic Modeling 
- pymc 
### Visualization 
- seaborn 
- plotly 
### High Performance Computing 
- numba 
- jax
### Deep Learning 
- pytorch(lightning, accelerate)
- flax 
- equinox 
### Image Analysis and Computer Vision 
- scikit-image 
### Notebooks 
- marimo
### Web Applications 
- fastapi 
- flask 
### Search
- elasticsearch (python)
### Data Engineering 
- pyspark 
