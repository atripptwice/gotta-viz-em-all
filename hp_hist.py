#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:08:05 2022

@author: ATripp
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#lets try now to a historgram 
df = pd.read_csv('pokemon.csv')
df.hist(column='HP')
# we can see the distrubtion of hp per pokemon
#Chansey is def one of the ones with 250 
