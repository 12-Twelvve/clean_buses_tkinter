from tkinter import *
import tkinter as tk 
import json

ratesList= []
data ={}
try:
    with open("feedback.json", "r") as df:
        data = json.load(df)
        ratesList =data['rate']
except:
    print('')

win = tk.Tk()
win.resizable(height = None, width = None)
win.title('cleaniness Rater')

def calAvg(val):
    print(val)
    selection = str(val)
    ratesList.append(int(selection))
    if len(ratesList)>0:
        sel = str(round((sum(ratesList)/len(ratesList)), 2))
    else:
        sel =str(0)
    print(ratesList)
    data['rate'] = ratesList
    with open("feedback.json", "w") as dff:
        json.dump(data, dff)
    label.config(text=sel)

# frame
frame1=Frame(win)
frame1.pack(ipadx=1, ipady=1, fill="both", expand=True)
frame2=Frame(win)
frame2.pack(ipadx=3, ipady=1, fill="both", expand=True)
frame3=Frame(win)
frame3.pack(ipadx=1, ipady=1, fill="both", expand=True)
# label
Label(frame1,font=("Arial", 12), text="Rate the cleanliness of this bus :").pack()
# buttons
but1= tk.Button(frame2,
          text=1, 
          height = 1, 
          width = 12,
          font=('Verdana', 12, 'bold'),
          command=lambda:calAvg("1")
          )
but2= tk.Button(frame2,
                text=2, 
                height = 1, 
                width = 12,
                font=('Verdana', 12, 'bold'),
                command=lambda:calAvg("2")
                )
but3= tk.Button(frame2,
                text=3,
                height = 1, 
                width = 12,
                font=('Verdana', 12, 'bold'),
                command=lambda:calAvg("3")
                )
but4= tk.Button(frame2,
                text=4,
                height = 1, 
                width = 12,
                font=('Verdana', 12, 'bold'),
                command=lambda:calAvg("4")
                )
but5= tk.Button(frame2,
                text=5,
                height = 1, 
                width = 12,
                font=('Verdana', 12, 'bold'),
                command=lambda:calAvg("5")
                )
but1.grid(column=0, row=1)
but2.grid(column=1, row=1)
but3.grid(column=2, row=1)
but4.grid(column=3, row=1)
but5.grid(column=4, row=1)

avglable = Label(frame3,font=("Arial", 15) ,text="This Bus has an average cleanliness rating of :")
avglable.grid(column=1, row=0)
label =Label(frame3, font=("Arial", 15))
if len(ratesList)>0:
    sel = str(round((sum(ratesList)/len(ratesList)), 2))
else:
    sel =str(0)
label.config(text=sel)
label.grid(column=2, row=0)
win.mainloop()