#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools


requirements = ['numpy', 'pandas']

setuptools.setup(
    name="time_series_cross_validation",
    author="Roel Bertens",
    author_email="roelbertens@godatadriven.com",
    description="""A cross-validation splitter for time series data.""",
    license="MIT",
    packages=setuptools.find_packages("time_series_cross_validation"),
    version="0.1.0",
    install_requires=requirements,
)
