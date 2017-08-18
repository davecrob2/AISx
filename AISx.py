# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:28:06 2017

@author: davecrob2
"""
import csv
from je_num import code_gen
import json

JE = {}

def gl_add():
    password=input("Enter a Password")
    
    #Poor man's security
    if password == "Password":
        
        #Requests Account Name and Number to be added
        Account_Name=input("Enter an Account Name")
        Account_Number=input("Enter an Account Number")
    
    
    #Writes Account Name and Account Number inputs into a .json dictionary
        with open('gl.json','r') as fp:
            json_data=json.load(fp)
            json_data[Account_Name]=int(Account_Number)
        with open('gl.json','w') as fp:
            fp.write(json.dumps(json_data))

def JE_writer():
    code=code_gen()
    journ[code]={}
    while True:
    
        y=input('Account Name: ')
        z=input('Amount Debit/(Credit): ')
        journ[code].update({y:int(z)})
        if sum(journ[code].values()) == 0:
            break
    

    with open('jeextract.json','r') as fp:
        json_data=json.load(fp)
        json_data=journ
  
    with open('jeextract.json','w') as fp:
        fp.write(json.dumps(json_data))

    #return(journ)


def dictionary(code,acct,amt):
    dic={}
    dic[code]={}
    dic[code][acct]=int(amt)
    return dic