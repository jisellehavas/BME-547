#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:11:56 2022

@author: jisellehavas
"""
import blood_calculator

print("This is the database.py module")
print("Python thinks this is called {}".format(__name__))

"""
from blood_calculator import check_HDL
import blood_calculator as bc
from blood_calculator import * (means import everything, 
if you have multiple of these then you won't know where it is coming from)
"""

answer = blood_calculator.check_HDL(55)
#answer = check_HDL(55)

print("The HDL of 55 is {}".format(answer))
