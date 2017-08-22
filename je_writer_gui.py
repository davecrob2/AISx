# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:44:45 2017

@author: davecrob2
"""

from tkinter import *
from je_num import code_gen
import tkinter.messagebox
import json

root = Tk()
root.title("Manual Journal Entry Tool")
root.geometry('500x300')
journalentry=dict()

with open('gl.json','r') as fp:
    gldictionary=json.load(fp)
            
            
def JE_post(entry):
    y=code_gen()
    z=dict()
    z[y]=entry
    with open('jeextract.json','r') as fp:
        json_data=json.load(fp)
        json_data.update(z)    
  
    with open('jeextract.json','w') as fp:
        fp.write(json.dumps(json_data))
    return(z)
    #print(z)

def guiJE(event):
    z=dict()
    x=dict()

    z[var1.get()]=int(accountentry1.get())
    z[var2.get()]=int(accountentry2.get())
    journalentry.update(z)
    if sum(journalentry.values())==00:
        return(JE_post(journalentry))
    else:
        journalentry.update(z)
    

      
var1=StringVar(root)
var1.set(gllist[0])

var2=StringVar(root)
var2.set(gllist[0])


accountlabel=Label(root,text="Account Name")
accountentrylabel=Label(root,text="Amount Debit/(Credit)")

menu1=OptionMenu(root,var1,*gldictionary)
accountentry1=Entry(root)

menu2=OptionMenu(root,var2,*gldictionary)
accountentry2=Entry(root)

enterbutton=Button(text="Submit Journal Entry")

root.bind("<Return>",guiJE)
enterbutton.bind("<Button-1>",guiJE)


accountlabel.grid(row=0,column=0)
accountentrylabel.grid(row=0,column=1)

menu1.grid(row=1,column=0)
accountentry1.grid(row=1,column=1)

menu2.grid(row=2,column=0)
accountentry2.grid(row=2,column=1)


enterbutton.grid(columnspan=2)

root.mainloop()