#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:10 2022

@author: jisellehavas
"""

def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice:")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
    
def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)


def check_HDL(num_HDL):
    if num_HDL >= 60:
        return "Normal"
    elif num_HDL >= 40 and num_HDL < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def HDL_driver():
    HDL_value = input_HDL()
    answer = check_HDL(HDL_value)
    output_HDL(HDL_value,answer)
    
def output_HDL(HDL_value,charac):
    print("The results for an HDL value of {} is {}".format(HDL_value,charac))
    


interface()