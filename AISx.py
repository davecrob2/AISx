# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:28:06 2017

@author: davecrob2
"""
import csv

gl ={}
JE = {}

def gl_add():
    password=input("Enter a Password")
    if password == "Password":
        Account_Name=input("Enter an Account Name")
        Account_Number=input("Enter an Account Number")
        gl[Account_Name]=Account_Number
        with open("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\gl.csv",'w') as gl_csv:
            writer =csv.writer(gl_csv)
            for key, value in gl.items():
                writer.writerow([key,value])
    return gl

def JE_writer():
    Account_Number=input("Enter an Account Number")
    Amount =input("Enter an Amount")
    JE[Account_Number]=Amount
    with open("C:\\Users\\davecrob2\\Documents\\GitHub\\AIS\\jeextract.csv",'w') as je_csv:
        writer =csv.writer(je_csv)
        for key, value in JE.items():
            writer.writerow([key,value])
    return JE

