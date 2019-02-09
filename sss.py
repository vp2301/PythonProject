from Tkinter import *
from tkMessageBox import *
import time
import sqlite3
import re

master=Tk()
master.title("INTRODUCTION WINDOW")
master.configure(background="light green")
logo=PhotoImage(file="logo.gif")
Label(master,image=logo).grid(row=0,column=0,rowspan=6)
Label(master,text="WELCOME TO THIS PROJECT",font=('helvetica',20,'bold'),bg="light green").grid(row=0,column=1,columnspan=10,sticky='nsew')
Label(master,text="STUDENT NAME:VINEET PAL",font=('helvetica',15,'bold'),width=40,anchor='w',bg="light green").grid(row=1,column=1)

Label(master,text="BATCH:B9",font=('helvetica',15,'bold'),width=40,anchor='w',bg="light green").grid(row=2,column=1)
Label(master,text="ER NO.:161B269",font=('helvetica',15,'bold'),width=40,anchor='w',bg="light green").grid(row=3,column=1)
Label(master,text="COURSE COORDINATOR:MR MAHESH KUMAR",width=40,font=('helvetica',15,'bold'),anchor='w',bg="light green").grid(row=4,column=1)
Label(master,text="PROJECT NAME:IRON AND STEEL \n SUPPLY MANAGEMENT",font=('helvetica',15,'bold'),width=40,anchor='w',bg="light green").grid(row=5,column=1)

def main():
    master.destroy()
    root=Tk()
    root.geometry("1400x600+0+0")
    root.title("MAIN WINDOW")
    tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
    tops.pack(side=TOP)
    f1=Frame(root,width=800,height=700,bg="orange",relief=SUNKEN)
    f1.pack(side=LEFT)

    #==================================functions=====================
    def addProduct():
        newf1=Frame(root,width=1600,height=700,relief=SUNKEN)
        newf1.place(x=270,y=250)
        Label(newf1,bd=8).grid()
        Label(newf1,text='Product Name',bd=8,fg='black',padx=20,pady=5,font=('arial',10,'bold')).grid(row=0,column=0)
        name=Entry(newf1,width=50)
        name.grid(row=0,column=1)
        Label(newf1,text='HSN code',bd=8,fg='steel blue',padx=10,pady=5,font=('arial',10,'bold')).grid(row=1,column=0)
        hsn=Entry(newf1,width=50)
        hsn.grid(row=1,column=1)
        Label(newf1,text='SGST rate',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=2,column=0)
        sgst=Entry(newf1,width=50)
        sgst.grid(row=2,column=1)
        Label(newf1,text='CGST rate',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=3,column=0)
        cgst=Entry(newf1,width=50)
        cgst.grid(row=3,column=1)
        Label(newf1,text='IGST rate',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=4,column=0)
        igst=Entry(newf1,width=50)
        igst.grid(row=4,column=1)
        Label(newf1,text='description',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=5,column=0)
        desc=Entry(newf1,width=50)
        desc.grid(row=5,column=1)
        Label(newf1,text='price',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=6,column=0)
        pr=Entry(newf1,width=50)
        pr.grid(row=6,column=1)
        
        def save():
            a=name.get()
            b=hsn.get()
            c=sgst.get()
            d=cgst.get()
            e=igst.get()
            f=desc.get()
            g=pr.get()
            cur.execute("select HSN_code from product where HSN_code=?",(b,))
            fetch=cur.fetchall()
            
            if not fetch :
                cur.execute("insert into product values(?,?,?,?,?,?,?)",(a.upper(),b,c,d,e,f,g))
                con.commit()
                showinfo('info','YOUR DATA HAVE BEEN SUCCESSFULLY SUBMITTED') 
            else:
                showerror('oops','hsn code already exist or empty field')
                    
        def reset():
            name.delete(0,END)
            hsn.delete(0,END)
            sgst.delete(0,END)
            cgst.delete(0,END)
            igst.delete(0,END)
            desc.delete(0,END)
            pr.delete(0,END)
        Button(newf1,text='RESET',bg="orange",command=reset).grid(row=8,column=0)
        Button(newf1,text="SAVE",bg="orange",command=save).grid(row=8,column=1)    
    def addCust():
        newf2=Frame(root,width=1600,height=700,relief=SUNKEN)
        newf2.place(x=250,y=250)
        Label(newf2,text='Name',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=0,column=0)
        name=Entry(newf2,width=50)
        name.grid(row=0,column=1)
        Label(newf2,text='Address',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=1,column=0)
        add=Entry(newf2,width=50)
        add.grid(row=1,column=1)
        Label(newf2,text='State code',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=2,column=0)
        code=Entry(newf2,width=50)
        code.grid(row=2,column=1)
        Label(newf2,text='Shipping Address',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=3,column=0)
        Sadd=Entry(newf2,width=50)
        Sadd.grid(row=3,column=1)
        Label(newf2,text='Shipping state code',bd=8,fg='steel blue',padx=10,pady=5,font=('arial',10,'bold')).grid(row=4,column=0)
        scode=Entry(newf2,width=50)
        scode.grid(row=4,column=1)
        Label(newf2,text='Telephone',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=5,column=0)
        tele=Entry(newf2,width=50)
        tele.grid(row=5,column=1)
        Label(newf2,text='GSTIN',bd=8,fg='steel blue',padx=5,pady=5,font=('arial',10,'bold')).grid(row=6,column=0)
        tin=Entry(newf2,width=50)
        tin.grid(row=6,column=1)
        def save():
            a=name.get()
            b=add.get()
            c=code.get()
            d=Sadd.get()
            e=scode.get()
            f=tele.get()
            g=tin.get()
            cur.execute("select GSTIN from customer where GSTIN=?",(g,))
            fetch=cur.fetchall()
     
            if not fetch :
                cur.execute("insert into customer values(?,?,?,?,?,?,?)",(a.upper(),b,c,d,e,f,g))
                con.commit()
                showinfo("info","YOUR DATA HAVE BEEN SUCCESSFULLY SUBMITTED")
                        
            else:
                showerror('oops','GSTIN is already exist') 
                    
                               
        def clear():
            name.delete(0,END)
            add.delete(0,END)
            code.delete(0,END)
            Sadd.delete(0,END)
            scode.delete(0,END)
            tele.delete(0,END)
            tin.delete(0,END)
        Button(newf2,text="RESET",command=clear,bg='orange').grid(row=8,column=0)
        Button(newf2,text="SAVE",command=save,bg='orange').grid(row=8,column=1)
    
    def modify_Pro():
        newf4=Frame(root,width=1600,height=700,relief=SUNKEN)
        newf4.place(x=800,y=250)
        Label(newf4,text="HSN CODE",fg='orange',font=('arial',10,'bold')).grid(row=0,column=0)
        hsn=Entry(newf4)
        hsn.grid(row=0,column=1)
        Label(newf4,text="which detail you want to change",fg='orange',font=('arial',10,'bold')).grid(row=1,column=0)
        details=["SGST rate","CGST rate","IGST rate","Price"]
        variable=StringVar(newf4)
        variable.set(details[0])
        w=OptionMenu(newf4,variable,*details)
        w.grid(row=1,column=1)
        Label(newf4,text="Enter your MODIFIED detail",fg='orange',font=('arial',10,'bold')).grid(row=2,column=0)
        e=Entry(newf4,width=20)
        e.grid(row=2,column=1)
        def setDetail():
            if(variable.get()=="SGST rate"):
                
                
                cur.execute("UPDATE product SET SGST_rate=? WHERE HSN_code=?",(e.get(),hsn.get()))
                con.commit()
        
            if(variable.get()=="CGST rate"):
                
                cur.execute("UPDATE product SET CGST_rate=? WHERE HSN_code=?",(e.get(),hsn.get()))
                con.commit()
            if(variable.get()=="IGST rate"):
                
                cur.execute("UPDATE product SET IGST_rate=? WHERE HSN_code=?",(e.get(),hsn.get()))
                con.commit()
            if(variable.get()=="Price"):
                
                cur.execute("UPDATE product SET Price=? WHERE HSN_code=?",(e.get(),hsn.get()))
                con.commit()
        Button(newf4,text='exit',comman=newf4.destroy,font=('arial',10,'bold')).grid(row=3,column=0)
        Button(newf4,text='SUBMIT',command=setDetail,font=('arial',10,'bold')).grid(row=3,column=1)
        
    def proList():
        root=Toplevel()
        root.title("PRODUCT LIST")
        cur.execute("select * from product")
        details = cur.fetchall()
        height = 1
        
        for i in details:
            width = 0
            for j in i:
                e = Entry(root,justify='right')
                e.grid(row=height, column=width)
                e.insert(0,j)
                width+=1
            height+=1
        Button(root,text="EXIT",padx=5,pady=5,bd=8,font=('arial',10,'bold'),bg='orange',command=root.destroy).grid(row=height,column=7)
        Label(root,text='PRODUCT NAME',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=0)
        Label(root,text='HSN CODE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=1)
        Label(root,text='SGST RATE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=2)
        Label(root,text='CGST RATE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=3)
        Label(root,text='IGST RATE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=4)
        Label(root,text='DESCRIPTION',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=5)
        Label(root,text='PRICE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=6)
    def custList():
        root=Toplevel()
        root.title("CUSTOMER LIST")
        cur.execute("select * from customer")
        details = cur.fetchall()
        height = 1
        for i in details:
            width = 0
            for j in i:
                e = Entry(root,justify='right',width=28)
                e.grid(row=height, column=width)
                e.insert(0,j)
                width+=1
            height+=1
        Button(root,text="EXIT",command=root.destroy,bg='orange',font=('arial',10,'bold'),padx=5,pady=5,bd=8).grid(row=height,column=7)
        Label(root,text='CUSTOMER NAME',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=0)
        Label(root,text='ADDRESS',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=1)
        Label(root,text='STATE CODE',fg='steel blue',font=('arial',10,'bold'),padx=10,pady=5).grid(row=0,column=2)
        Label(root,text='SHIPPING ADDRESS',fg='steel blue',font=('arial',10,'bold'),padx=10,pady=5).grid(row=0,column=3)
        Label(root,text='SHIPPING STATE CODE',fg='steel blue',font=('arial',10,'bold'),padx=10,pady=5).grid(row=0,column=4)
        Label(root,text='MOBILE',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=5)
        Label(root,text='GSTIN',fg='steel blue',font=('arial',10,'bold')).grid(row=0,column=6) 
       
    #=========================database===============================
    con=sqlite3.Connection("mydb")
    cur=con.cursor()
    cur.execute("create table if not exists product(PName char(20),HSN_code number(10) PRIMARY KEY,SGST_rate number(5),CGST_rate number(5),IGST_rate number(5),Description varchar(30),Price number(10) NOT NULL)")
    cur.execute("create table if not exists customer(Cname char(20),address varchar(30),state_code number(10),shipping_address varchar(30),shipping_state_code number(10),Mobile_number number(10),GSTIN varchar(15) primary key)")
    con.commit()

    bt1=Button(f1,text='ADD CUSTOMER',command=addCust,padx=5,pady=5,bd=8,fg='black',font=('arial',8,'bold'),bg="powder blue",width=20).grid(row=0,column=0)
    bt4=Button(f1,text="ADD PRODUCT",command=addProduct,padx=5,pady=5,bd=8,fg='black',font=('arial',8,'bold'),bg="powder blue",width=20).grid(row=2,column=0)

    bt6=Button(f1,text="MODIFY PRODUCT",command=modify_Pro,padx=5,pady=5,bd=8,fg='black',font=('arial',8,'bold'),bg="powder blue",width=20).grid(row=4,column=0)
    bt8=Button(f1,text="CUSTOMER LIST",command=custList,padx=5,pady=5,bd=8,fg='black',font=('arial',8,'bold'),bg="powder blue",width=20).grid(row=5,column=0)
    bt9=Button(f1,text="PRODUCT LIST",command=proList,padx=5,pady=5,bd=8,fg='black',font=('arial',8,'bold'),bg="powder blue",width=20).grid(row=6,column=0)


    #=========================time==========================
    localtime=time.asctime(time.localtime(time.time()))
    #==========================info==========================
    image =PhotoImage(file="steel1.gif")
    Label(tops, image=image).grid(row=0,column=0)
    lblInfo=Label(tops,font=('arial',50,'bold'),text="IRON AND STEEL SUPPLIER ",fg="Steel Blue",bd=10,anchor='w')
    lblInfo.grid(row=0,column=1)

    lblInfo=Label(tops,font=('arial',20,'bold'),text=localtime,fg="orange",bd=10,anchor='w',bg='powder blue')
    lblInfo.grid(row=1,column=1)
    #===============================
    mainloop()
Button(master,text="GO TO MAIN WINDOW",command=main,bg="steel blue",padx=5,pady=5).grid(row=6,column=1)
master.mainloop()
