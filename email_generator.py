from os import pardir
from tkinter import *
from tkinter import ttk
from email import message
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import smtplib
from email.message import EmailMessage
import hashlib
import random
import string
import re



class Email_generate():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Pre-Registration for Admins")
        self.root.bind("<Return>",self.enter_func)



        # Background image
        b_img=Image.open(r"college_images\BestFacialRecognition.jpg")
        b_img=b_img.resize((1366,750),Image.ANTIALIAS)
        self.pho_img=ImageTk.PhotoImage(b_img)

        blbl=Label(self.root,image=self.pho_img)
        blbl.place(x=0,y=0,width=1366,height=750)

        

        #login frame
        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=345,height=420)


        #login icon
        image1=Image.open(r"college_images\Crystal_Project_Personal.png")
        image1=image1.resize((100,100),Image.ANTIALIAS)
        self.pho_img2=ImageTk.PhotoImage(image1)

        lblimg=Label(self.root,image=self.pho_img2,bg="black",borderwidth=0)
        lblimg.place(x=620,y=170,width=100,height=100)

        #get started
        gt_str=Label(frame,text="Only Admins",font=("times new roman",21,"bold"),bg="black",fg="white")
        gt_str.place(x=100,y=130)


        #Labels
        username=Label(frame,text="Email ID",font=("times new roman",15),bg="black",fg="white")
        username.place(x=45,y=200)

        self.var_user=StringVar()
        self.user_entry=ttk.Entry(frame,textvariable=self.var_user,width=20,font=("times new roman",12))
        self.user_entry.place(x=155,y=200)

        pass_word=Label(frame,text="Secret Key",font=("times new roman",15),bg="black",fg="white")
        pass_word.place(x=45,y=260)

        self.var_pass=StringVar()
        
        
        self.pass_entry=ttk.Entry(frame,show="*",textvariable=self.var_pass,width=20,font=("times new roman",12))
        self.pass_entry.place(x=155,y=260)
        # self.var_pass=hashlib.sha224(str(self.pass_entry).encode()).digest()

        

        #Icons for username and password
        user_icon=Image.open(r"college_images\usericon.png")
        user_icon=user_icon.resize((26,26),Image.ANTIALIAS)
        self.pho_img3=ImageTk.PhotoImage(user_icon)

        userlbl=Label(image=self.pho_img3,bg="black",borderwidth=0)
        userlbl.place(x=513,y=350,width=26,height=26)

        pass_icon=Image.open(r"college_images\password-icon-png-22.jpg")
        pass_icon=pass_icon.resize((26,26),Image.ANTIALIAS)
        self.pho_img4=ImageTk.PhotoImage(pass_icon)

        passlbl=Label(image=self.pho_img4,bg="black",borderwidth=0)
        passlbl.place(x=513,y=408,width=26,height=26)

        #login Button
        self.login_btn=Button(frame,text="Submit",font=("times new roman",15),command=self.register_data,bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        self.login_btn.place(x=200,y=320,width=100,height=30)

        # #register button
        # regis_btn=Button(frame,text="New User Register!",font=("times new roman",10),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        # regis_btn.place(x=20,y=350,width=120)

        # #forgot pass
        # fpass_btn=Button(frame,text="Forgot Password?",font=("times new roman",10),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        # fpass_btn.place(x=20,y=370,width=120)


        u=string.ascii_uppercase
        l=string.ascii_lowercase
        d=string.digits
        s=string.punctuation
        self.p=random.choice(u)+random.choice(l)+random.choice(d)+random.choice(s)

        mess=hashlib.sha512(str(self.var_user.get()).encode('utf-8')).hexdigest()
        # pass_sec_code="key123"
        mess1=hashlib.sha512(str(self.var_pass.get()).encode('utf-8')).hexdigest()
        for i in range(20):
            self.p=self.p+random.choice(mess+mess1)

        

    def register_data(self):
        regrex ='^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not (re.search(regrex,self.var_user.get())):
            messagebox.showerror("Error","Invalid email address",parent=self.root)
        elif self.var_user.get()=="":
            messagebox.showerror("Error","Email address cannot be empty",parent=self.root)
        elif self.var_pass.get()=="":
            messagebox.showerror("Error","Secret key cannot be empty")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from preregister where email_id=%s")
            value=(self.var_user.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits,please try another email",parent=self.root)
            else:
                # self.result=hashlib.sha224(str(self.pass_entry).encode())
                my_cursor.execute("insert into preregister values(%s,%s,%s)",(

                                                                                    self.var_user.get(),
                                                                                    self.var_pass.get(),
                                                                                    # hashlib.sha224(self.result.get().encode('utf-8')).hexdigest()
                                                                                    self.p
                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration Successfull",parent=self.root)
                # self.root.destroy()

                msg="Your Secret key for login is  "+self.p+"  please do not share it with anyone!!!"
                # print (msg)


                server = smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("","")  #username,passwaord of your email
                email= EmailMessage()
                email["From"]=""
                email["To"]=self.var_user.get()
                email["Subject"]="Log In pin of Face Attendance System"
                email.set_content(msg)
                server.send_message(email)
                


    def enter_func(self,event):
        self.login_btn.invoke()
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)





if __name__ =="__main__":
    root=Tk()
    app=Email_generate(root)
    root.mainloop()
