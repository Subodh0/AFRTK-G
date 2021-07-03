from codecs import encode
from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from admin_register import Register
from main import Face_Recognition_System
import hashlib


class Login_window_admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Login")
        self.root.bind("<Return>",self.enter_func1)


        self.var_pass=StringVar()

        # Background image
        b_img=Image.open(r"college_images\woman.jpg")
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
        gt_str=Label(frame,text="Admin login",font=("times new roman",21,"bold"),bg="black",fg="white")
        gt_str.place(x=100,y=130)


        #Labels
        username=Label(frame,text="Username",font=("times new roman",15),bg="black",fg="white")
        username.place(x=45,y=200)

        self.var_user=StringVar()
        self.user_entry=ttk.Entry(frame,textvariable=self.var_user,width=16,font=("times new roman",15))
        self.user_entry.place(x=155,y=200)

        pass_word=Label(frame,text="Password",font=("times new roman",15),bg="black",fg="white")
        pass_word.place(x=45,y=260)

        # self.var_pass=StringVar()
        
        
        self.pass_entry=ttk.Entry(frame,show="*",width=16,font=("times new roman",15))
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
        self.login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        self.login_btn.place(x=200,y=320,width=100,height=30)

        #register button
        regis_btn=Button(frame,text="New User Register!",command=self.regis_data,font=("times new roman",10),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        regis_btn.place(x=20,y=350,width=120)

        #forgot pass
        fpass_btn=Button(frame,text="Forgot Password?",command=self.forgot_pass_window,font=("times new roman",10),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        fpass_btn.place(x=20,y=370,width=120)


    # def hasing(self):
    #     self.pass_entry=hashlib.sha224(str(self.pass_entry.get()).encode()).hexdigest()

    

    def login(self):
        # self.pass_entry=hashlib.sha224(str(self.pass_entry).encode()).hexdigest()
        if self.var_user.get()=="":
            messagebox.showerror("Error","Username cannot be empty",parent=self.root)
        elif self.pass_entry.get()=="":
            print(self.pass_entry.get())
            messagebox.showerror("Error","Password cannot be empty",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from admin_register where email=%s and password=%s",(
                                                                                        self.var_user.get(),
                                                                                        hashlib.sha224(str(self.pass_entry.get()).encode()).hexdigest()

                                                                                    ))
                                                                                  
            row=my_cursor.fetchone()
            # print(row)
            # print(self.pass_entry.get())
            # print(hashlib.sha224(str(self.pass_entry.get()).encode()).hexdigest())
            if row==None:
                messagebox.showerror("Error","Invaild Username or Password")
                # open_main=messagebox.askyesno("Alert","The Data inside are very sensitive, Are you an Admin ?")
                # if open_main>0:
                #     self.root=Toplevel(self.root)
                #     self.app=Face_Recognition_System(self.root)
                # else:
                #     if not open_main:
                #         return
            else:
                # messagebox.showerror("Error","Invaild Username or Password")
                
                # self.root=Toplevel(self.root)
                # self.app=Face_Recognition_System(self.root)
                self.root.withdraw() #Do NOT call destroy as you need the root to be 
                                        #active for Toplevel
                self.newWindow = Toplevel(self.root)
                self.newWindow.protocol("WM_DELETE_WINDOW", self.on_closing) #And add this

                self.app = Face_Recognition_System(self.newWindow)
                

                
                # open_main=messagebox.askyesno("Alert","The Data inside are very sensitive, Are you an Admin ?")
                # if open_main>0:
                    
                # else:
                #     if not open_main:
                #         return
            
            conn.commit()
            conn.close()
            
            # self.root.destroy()

    #reset password
    def reset_pass(self):
        if self.sec_ques_combo.get()=="Select Security Question":
            messagebox.showerror("Error","Please select the security question")
        elif self.sec_ans_entry.get()=="":
            messagebox.showerror("Error","Security answer cannot be empty")
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter new password")
        elif self.new_con_pass_entry.get()=="":
            messagebox.showerror("Error","Confirm password cannot be empty!")
        elif self.new_pass_entry.get()!=self.new_con_pass_entry.get():
            messagebox.showerror("Error","Confirm Password should be the same as New Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from admin_register where email=%s and sec_ques=%s and sec_ans=%s")
            value=(self.user_entry.get(),self.sec_ques_combo.get(),self.sec_ans_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct inputs")
            else:
                # self.new_pass_entry.get()
                Query=("update admin_register set password=%s where email=%s")
                Value=(hashlib.sha224(self.new_pass_entry.get().encode('utf-8')).hexdigest(),self.user_entry.get())
                my_cursor.execute(Query,Value)


                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been successfully reseted, please login with new password")
                self.root2.destroy()


        



    #forgot password
    def forgot_pass_window(self):
        if self.user_entry.get()=="":
            messagebox.showerror("Error","Please enter the correct email address to reset the password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from admin_register where email=%s")
            value=(self.user_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            

            if row==None:
                messagebox.showerror("Error","Please enter the valid username/email id")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("345x420+500+150")
                self.root2.bind("<Return>",self.enter_func)

                l=Label(self.root2,text="Forgot Password",font=("times new roman",21,"bold"),bg="white",fg="red")
                l.place(x=0,y=12,relwidth=1)


                sec_ques_lbl=Label(self.root2,text="Security Question",font=("times new roman",16,"bold"),bg="white",fg="black")
                sec_ques_lbl.place(x=40,y=70)

                self.sec_ques_combo=ttk.Combobox(self.root2,font=("times new roman",14),width=25,state="readonly")
                self.sec_ques_combo["value"]=("Select Security Question","Birth Place","Favourite Sport","Ideal","Aim in life","Others")
                self.sec_ques_combo.current(0)
                self.sec_ques_combo.place(x=40,y=100)

                sec_ans_lbl=Label(self.root2,text="Securiy Answer",font=("times new roman",16,"bold"),bg="white",fg="black")
                sec_ans_lbl.place(x=40,y=140)

                self.sec_ans_entry=ttk.Entry(self.root2,font=("times new roman",14))
                self.sec_ans_entry.place(x=40,y=170,width=250)


                pass_lbl=Label(self.root2,text="New Password",font=("times new roman",16,"bold"),bg="white",fg="black")
                pass_lbl.place(x=40,y=210)

                self.new_pass_entry=ttk.Entry(self.root2,show="*",font=("times new roman",14))
                self.new_pass_entry.place(x=40,y=240,width=250)

                con_pass_lbl=Label(self.root2,text="Confirm Password",font=("times new roman",16,"bold"),bg="white",fg="black")
                con_pass_lbl.place(x=40,y=280)

                self.new_con_pass_entry=ttk.Entry(self.root2,show="*",font=("times new roman",14))
                self.new_con_pass_entry.place(x=40,y=310,width=250)


                self.btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",16),fg="white",bg="green")
                self.btn.place(x=70,y=350,width=200)



    #Function for register
    def regis_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def enter_func(self,event):
        self.btn.invoke()

    def enter_func1(self,event):
        self.login_btn.invoke()
        # self.login_btn.destroy()
    def on_closing(self): #Add this event handler
        self.root.destroy()
  





if __name__ =="__main__":
    root=Tk()
    app=Login_window_admin(root)
    root.mainloop()
