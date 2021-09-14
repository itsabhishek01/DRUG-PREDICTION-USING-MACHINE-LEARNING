import pandas as pd
from joblib import load
from tkinter import *

la=load("Drug.joblib")
ls=load("Sex.joblib")
lb=load("BP.joblib")
lc=load("Cholesterol.joblib")
sc=load("scaling.joblib")
lr=load("regressor.joblib")

def result():
    new=pd.DataFrame({"Age":[(int(a1.get()))],"Sex":[(a2.get())],"BP":[(a3.get())],"Cholesterol":[(a4.get())],"Na_to_K":[(float(a5.get()))]})
    new["Sex"]=ls.transform(new["Sex"])
    new["BP"]=lb.transform(new["BP"])
    new["Cholesterol"]=lc.transform(new["Cholesterol"])
    new=sc.transform(new)
    o=lr.predict(new)
    if o==0:
        drug=Label(root,text="Required Drug is [DrugY]",font=("arial",20),fg="white",bg="red")
        drug.place(x=10,y=300)
    elif o==1:
        drug=Label(root,text="Required Drug is [drugA]",font=("arial",20),fg="white",bg="red")
        drug.place(x=10,y=300)
    elif o==2:
        drug=Label(root,text="Required Drug is [drugB]",font=("arial",20),fg="white",bg="red")
        drug.place(x=10,y=300)
    elif o==3:
        drug=Label(root,text="Required Drug is [drugC]",font=("arial",20),fg="white",bg="red")
        drug.place(x=10,y=300)
    else:
        drug=Label(root,text="Required Drug is [drugX]",font=("arial",20),fg="white",bg="red")
        drug.place(x=10,y=300)
root=Tk()
root.geometry("1000x400")
root.resizable(0,0)
root.title("Drug Prediction")
a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()

heading=Label(root,text="Drug Prediction Using ML",font=("Arial",25),fg="darkblue")
heading.place(x=0,y=10)

age=Label(root,text="Enter the Age")
age.place(x=10,y=80)
age1=Entry(root,textvariable=a1)
age1.place(x=250,y=80)

sex=Label(root,text="Enter the Gender(M/F)")
sex.place(x=10,y=110)
sex1=Entry(root,textvariable=a2)
sex1.place(x=250,y=110)

bp=Label(root,text="Enter the BP (HIGH/NORMAL/LOW)")
bp.place(x=10,y=140)
bp1=Entry(root,textvariable=a3)
bp1.place(x=250,y=140)

Cholesterol=Label(root,text="Enter the Cholesterol level(HIGH/NORMAL) ")
Cholesterol.place(x=10,y=170)
Cholesterol1=Entry(root,textvariable=a4)
Cholesterol1.place(x=250,y=170)

Na_to_K=Label(root,text="Enter the Na to K value")
Na_to_K.place(x=10,y=200)
Na_to_K1=Entry(root,textvariable=a5)
Na_to_K1.place(x=250,y=200)

submit=Button(root,text="Predict",command=result,font=("Arial",20),fg="white",bg="red")
submit.place(x=250,y=230)

bg = PhotoImage(file = r"img.png")

# Show image using label
label2 = Label( root, image = bg)
label2.place(x = 500, y = 0)
root.mainloop()