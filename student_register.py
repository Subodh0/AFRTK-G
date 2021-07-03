from tkinter import *
from tkinter import ttk
from typing import cast
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import hashlib
import re







class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Registration")
        self.root.bind("<Return>",self.enter_func)


        #Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cont=StringVar()
        self.var_email=StringVar()
        self.var_SecQ=StringVar()
        self.var_SecA=StringVar()
        self.result=StringVar()
        self.var_conpass=StringVar()


        

        # Back ground image
        bg_img=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        bg_img=bg_img.resize((1366,750),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(bg_img)

        lbl_bg=Label(self.root,image=self.photoimage11)
        lbl_bg.place(x=0,y=0,width=1366,height=750)


        #left Image
        left_img=Image.open(r"college_images\1544601251919.png")
        left_img=left_img.resize((400,560),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(left_img)

        lbl_l=Label(self.root,image=self.photoimage1)
        lbl_l.place(x=90,y=80,width=400,height=560)

        #regis frame
        frame=Frame(self.root,bg="white")
        frame.place(x=490,y=80,width=770,height=560)

        regis_lbl=Label(frame,text="Students REGISTER HERE",font=("times new roman",22,"bold"),bg="white",fg="darkgreen")
        regis_lbl.place(x=25,y=10)

        #label entry
        first_lbl=Label(frame,text="First Name",font=("times new roman",17,"bold"),bg="white",fg="black")
        first_lbl.place(x=60,y=100)

        self.first_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16))
        self.first_entry.place(x=60,y=130,width=250)

        last_lbl=Label(frame,text="Last Name",font=("times new roman",17,"bold"),bg="white",fg="black")
        last_lbl.place(x=440,y=100)

        self.last_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16))
        self.last_entry.place(x=440,y=130,width=250)

        contact_lbl=Label(frame,text="Contact No.",font=("times new roman",17,"bold"),bg="white",fg="black")
        contact_lbl.place(x=60,y=180)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_cont,font=("times new roman",16))
        self.contact_entry.place(x=60,y=210,width=250)

        email_lbl=Label(frame,text="Email ID",font=("times new roman",17,"bold"),bg="white",fg="black")
        email_lbl.place(x=440,y=180)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16))
        self.email_entry.place(x=440,y=210,width=250)

        sec_ques_lbl=Label(frame,text="Security Question",font=("times new roman",17,"bold"),bg="white",fg="black")
        sec_ques_lbl.place(x=60,y=260)

        self.sec_ques_combo=ttk.Combobox(frame,textvariable=self.var_SecQ,font=("times new roman",13),width=25,state="readonly")
        self.sec_ques_combo["value"]=("Select Security Question","Birth Place","Favourite Sport","Ideal","Aim in life","Others")
        self.sec_ques_combo.current(0)
        self.sec_ques_combo.place(x=60,y=290)

        sec_ans_lbl=Label(frame,text="Securiy Answer",font=("times new roman",17,"bold"),bg="white",fg="black")
        sec_ans_lbl.place(x=440,y=260)

        self.sec_ans_entry=ttk.Entry(frame,textvariable=self.var_SecA,font=("times new roman",16))
        self.sec_ans_entry.place(x=440,y=290,width=250)


        pass_lbl=Label(frame,text="Password",font=("times new roman",17,"bold"),bg="white",fg="black")
        pass_lbl.place(x=60,y=340)

        self.pass_entry=ttk.Entry(frame,textvariable=self.result,font=("times new roman",16))
        self.pass_entry.place(x=60,y=370,width=250)

        # self.pass_code=hashlib.md5(str(self.pass_entry).encode('utf-8'))
        # self.pass_code=Entry(frame,textvariable=self.var_pass)


        con_pass_lbl=Label(frame,text="Confirm Password",font=("times new roman",17,"bold"),bg="white",fg="black")
        con_pass_lbl.place(x=440,y=340)

        self.con_pass_entry=ttk.Entry(frame,textvariable=self.var_conpass,show="*",font=("times new roman",16))
        self.con_pass_entry.place(x=440,y=370,width=250)

        #check button
        self.var_check=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",10),bg="white",onvalue=1,offvalue=0)
        check_btn.place(x=60,y=415)


        #Register button
        regis_img=Image.open(r"college_images\24984-6-register-button-file.png")
        regis_img=regis_img.resize((200,50),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(regis_img)

        self.lbl_img3=Button(frame,image=self.photoimage5,command=self.register_data,borderwidth=0,cursor="hand2")
        self.lbl_img3.place(x=450,y=440,width=200,height=50)


        # #Login button
        # login_img=Image.open(r"college_images\24831-6-member-login-button-clipart.png")
        # login_img=login_img.resize((200,60),Image.ANTIALIAS)
        # self.photoimage6=ImageTk.PhotoImage(login_img)

        # lbl_img4=Button(frame,image=self.photoimage6,borderwidth=0,cursor="hand2")
        # lbl_img4.place(x=445,y=455,width=200,height=60)

    #Function Declaration
    def register_data(self):
        regrex ='^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        reg_cont="(0/91)?[6-9][0-9]{9}"
        # if (re.search(regrex,self.var_email.get())):
        #     pass
        # else:
            


        if self.var_fname.get()=="":
            messagebox.showerror("Error","First name connot be empty!",parent=self.root)
        elif self.var_lname.get()=="":
            messagebox.showerror("Error","Last name cannot be empty!",parent=self.root)
        elif self.var_cont.get()=="":
            messagebox.showerror("Error","Contact number cannot be empty!",parent=self.root)
        elif not (re.search(reg_cont,self.var_cont.get())):
            messagebox.showerror("Error","Invalid mobile number",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("Error","Email address cannot be empty",parent=self.root)
        elif not (re.search(regrex,self.var_email.get())):
            messagebox.showerror("Error","Invalid email address",parent=self.root)
        elif self.var_SecQ.get()=="Select Security Question":
            messagebox.showerror("Error","Please select a question",parent=self.root)
        elif self.var_SecA.get()=="":
            messagebox.showerror("Error","Security answer cannot be empty!",parent=self.root)
        elif self.result.get()=="":
            messagebox.showerror("Error","Password field cannot be empty!",parent=self.root)
        elif self.var_conpass.get()=="":
            messagebox.showerror("Error","Confirm password cannot be empty!",parent=self.root)
        elif self.result.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Confirm Password should be the same as Password",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree with the terms and conditions!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from student_register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits,please try another email",parent=self.root)
            else:
                # self.result=hashlib.sha224(str(self.pass_entry).encode())
                my_cursor.execute("insert into student_register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_cont.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_SecQ.get(),
                                                                                    self.var_SecA.get(),
                                                                                    hashlib.sha224(self.result.get().encode('utf-8')).hexdigest()
                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration Successfull",parent=self.root)
                self.root.destroy()
            

    def enter_func(self,event):
        self.lbl_img3.invoke()

        






if __name__ =="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()

