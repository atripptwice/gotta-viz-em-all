#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:54:19 2022

@author: ATripp
"""
#lets try a scatter plt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokemon.csv')

df.plot.scatter(x='Attack',y='Defense')