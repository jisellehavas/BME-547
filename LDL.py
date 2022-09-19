#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:57:46 2022

@author: jisellehavas
"""

def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)


def check_LDL(num_LDL):
    if num_LDL >= 190:
        return "very high"
    elif num_LDL >= 160:
        return "high"
    elif num_LDL >= 130:
        return "borderline high"
    else:
        return "normal"
        
def LDL_driver():
    LDL_value = input_LDL()
    answer = check_LDL(LDL_value)
    output_LDL(LDL_value,answer)
    
def output_LDL(LDL_value,charac):
    print("The results for an LDL value of {} is {}".format(LDL_value,charac))
    

if __name__=="__main__":
    LDL_driver()