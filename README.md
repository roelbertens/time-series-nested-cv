Time series nested cross-validation
==============================

This project contains the code that belongs to the following 
[blog post](https://blog.godatadriven.com/time-series-nested-cv).

Project Organization
------------

    │
    ├── notebooks/                      <- Jupyter notebooks.
    │
    ├── timeseries_cross_validation/    <- Python module with source code of this project.
    │
    ├── environment.yml                 <- conda virtual environment definition file.
    │
    ├── LICENSE
    │
    ├── README.md                       <- This file
    │
    └── setup.py                        <- To install timeseries_cross_validation



Set up
------------

Create the virtual environment with conda and and activate it:

```bash
$ conda env create -f environment.yml
$ source activate timeseries-nested-cv 
```

Install `timeseries-nested-cv` in the virtual environment:

```bash
$ pip install --editable .
```

Run Jupyter Notebook and open the notebooks in `notebooks/`:

```bash
$ jupyter notebook
```
