#DATABASE
import sqlite3
con=sqlite3.Connection('empdata')
cur=con.cursor()
cur.execute("create table if not exists emp(ecode number,fname varchar(30),lname varchar(30))")

#GUI
from Tkinter import *
from tkMessageBox import *
root=Tk()
root.title("Emp_database")
Label(root,text='EMPLOYEE RECORD KEEPING SYSTEM :',font='times 20 bold').grid(row=0)
Label(root,text=" ").grid(row=1)

Label(root,text='Enter Emp Code:',font='times 12').grid(row=2)

ecode=Entry(root)
ecode.grid(row=2,column=1)

Label(root,text='Enter First Name:',font='times 12').grid(row=3)

efname=Entry(root)
efname.grid(row=3,column=1)

Label(root,text='Enter Last name:',font='times 12').grid(row=4)

elname=Entry(root)
elname.grid(row=4,column=1)

Label(root,text='Enter id to fetch record:',font='times 12').grid(row=5,column=0)

eid=Entry(root)
eid.grid(row=5,column=1)


Label(root,text=" ").grid(row=6)
def indata():

            cur.execute("insert into emp values (?,?,?)",(int(ecode.get()),efname.get(),elname.get()))
            con.commit()
            print "Data Inserted"
            
def display():
        d=int(eid.get())
        cur.execute("select * from emp where ecode==?",(d,))
        x=cur.fetchall()
        ecode.insert(0,x[0][0])
        efname.insert(0,x[0][1])
        elname.insert(0,x[0][2])
        
def dispall():
            cur.execute("select * from emp")
            x=cur.fetchall()
            print "E_ID|Fname|Lname"
            for i in x:
                for j in i:
                    print j,
                    print" |",
                print 
            
Button(root,activebackground="grey",text="Insert",width=5,command=indata).grid(row=7,column=0)
Button(root,activebackground="grey",text="Show",width=5,command=display).grid(row=7,column=1)
Button(root,activebackground="grey",text="Show All",width=7,command=dispall).grid(row=7,column=2)

Label(root,text="    ").grid(row=7,column=3)
Label(root,text=" ").grid(row=8)

#Button(root,activeforeground="red",font="2px ",bg="red",text="CLOSE",width=8,command=root.destroy).grid(row=9,column=1)
a=PhotoImage(file='closebtt.gif')
def func():
    y=askyesno('Close','Do you want to close ?')
    if y==True:
        root.destroy()
Button(root,image=a,width=35,height=35,command=func).grid(row=10,column=1)
root.mainloop()

