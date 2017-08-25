# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:37:30 2017

@author: davecrob2
"""

from tkinter import *
import tkinter.messagebox


class Dashboard():
    def __init__(self,master):
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('AISx Dashboard')

        #Enter Invoice Module
        self.enterInvoicebutton=Button(self.master,text="Enter Invoice",command=self.enterInvoice).grid(row=0,column=2)
    def enterInvoice(self):
        leveltwo=Toplevel(self.master)
        window=InvoiceScreen(leveltwo)
        
    def finish(self):
        self.master.destroy()

class InvoiceScreen():
    def __init__(self,master):
        self.amtvar=DoubleVar()
        self.numbervar=StringVar()
        self.datevar=StringVar()
        self.duedatevar=StringVar()
        self.custnamevar=StringVar()
        self.custnumvar=StringVar()
        
        self.master=master
        self.master.geometry('500x300')
        self.master.title('Enter Invoice Details')
        
        self.numberlabel=Label(self.master,text='Invoice Number').grid(row=0,column=1)
        self.amtlabel=Label(self.master,text='Invoice Amount').grid(row=1,column=1)
        self.datelabel=Label(self.master,text='Invoice Date').grid(row=2,column=1)
        self.duedatelabel=Label(self.master,text='Due Date').grid(row=3,column=1)
        self.custnamelabel=Label(self.master,text='Customer Name').grid(row=4,column=1)
        self.custnumlabel=Label(self.master,text='Customer Number').grid(row=5,column=1)
        
        
        self.number=Entry(self.master,textvariable=self.numbervar).grid(row=0,column=2)
        self.amt=Entry(self.master,textvariable=self.amtvar).grid(row=1,column=2)
        self.date=Entry(self.master,textvariable=self.datevar).grid(row=2,column=2)
        self.duedate=Entry(self.master,textvariable=self.duedatevar).grid(row=3,column=2)
        self.custname=Entry(self.master,textvariable=self.custnamevar).grid(row=4,column=2)
        self.custnum=Entry(self.master,textvariable=self.custnumvar).grid(row=5,column=2)
        
        self.button1=Button(self.master,text="Save Invoice",command=self.saveInvoice).grid(row=6,columnspan=2)
    
        
    def saveInvoice(self):
        catch=messagebox.askyesno(self.master,'Are all invoice details correct?')
        try:
            if catch==True:
                current=Invoice(self.numbervar.get(),self.amtvar.get(),self.datevar.get(),self.custnamevar.get(),self.custnumvar.get(),self.duedatevar.get())
                
        except:
            messagebox.showinfo(self.master,"Error in Invoice Details")

#currency=Label(window,text='Currency')
#
#cc=Label(window,text='Cost Center')
#per=Label(window,text='Period')
#
#number
#amount
#date
#
#duedate
#custname
#custnum
#
#currency.grid(row=2,column=0)
#cc.grid(row=2,column=1)
#per.grid(row=2,column=2)




#Class for Invoices
class Invoice(object):
    def __init__(self,number,amount,date,custname,custnum,duedate):
        self.number=number
        self.amount=amount
        self.date=date
        self.custname=custname
        self.custnum=custnum
        self.duedate=duedate
        
    #Add function to print invoice in invoice format?
        
#Class for JournalEntries
class JournalEntry(object):
    def __init__(self,code,entries):
        self.code=code
        self.entries=entries
    #Add function JE_Write
    #Add function if balanced
def main():
    root=Tk()
    initDashboard=Dashboard(root)
    root.mainloop()
