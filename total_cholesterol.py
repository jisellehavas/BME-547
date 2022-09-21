#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:33:06 2022

@author: jisellehavas
"""


def input_chol():
    chol_input = input("Enter the total cholesterol value:")
    return int(chol_input)


def check_chol(num_chol):
    if num_chol >= 240:
        return "high"
    elif num_chol >= 200:
        return "borderline high"
    else:
        return "normal"


def chol_driver():
    chol_value = input_chol()
    answer = check_chol(chol_value)
    output_chol(chol_value, answer)


def output_chol(chol_value, charac):
    print("The results for an LDL value of {} is {}".format(chol_value, charac))


chol_driver()
