from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strptime
import datetime
from time import strftime
# from train import Train


class Students:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Student Details")
        # self.root.bind("<Return>",self.enter_func)

        #Data Variables
        self.var_st_id=StringVar()
        self.var_dept=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        # self.var_teacher=StringVar()


        # Image 1
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((455,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=455,height=130)

        #image2
        img1=Image.open(r"college_images\girl.jpeg")
        img1=img1.resize((455,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=455,y=0,width=455,height=130)

        #image3
        img2=Image.open(r"college_images\dev.jpg")
        img2=img2.resize((457,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=910,y=0,width=457,height=130)


        #Background Image
        img3=Image.open(r"college_images\BestFacialRecognition.jpg")
        img3=img3.resize((1365,625),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1365,height=625)

        #Title
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",28,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1365,height=45)

        #Time
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=("times new roman",16),bg="white",fg="blue")
        lbl.place(x=40,y=0,width=120,height=45)
        time()


        main_frame=Frame(bg_img,bd=3,bg="white")
        main_frame.place(x=10,y=55,width=1345,height=550)

        #Left Frame
        left_frmae=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Enter Student Details",font=("times new roman",12))
        left_frmae.place(x=10,y=10,width=635,height=530)

        img_left=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_left=img_left.resize((620,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frmae,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=620,height=130)

        #Current Course Details
        current_frame=LabelFrame(left_frmae,bd=2,bg="white" ,relief=RIDGE,text="Current Course Information",font=("times new roman",12))
        current_frame.place(x=0,y=135,width=630,height=100)

        #student ID
        student_id_lbl=Label(current_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_id_lbl.grid(row=0,column=0,padx=5,pady=4,sticky=W)

        studend_id_entry=ttk.Entry(current_frame,textvariable=self.var_st_id,width=22,font=("times new roman",12))
        studend_id_entry.grid(row=0,column=1,padx=5,pady=4,sticky=W)

        #dept name
        dept_lbl=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_lbl.grid(row=0,column=2,padx=5,sticky=W)

        dept_combo=ttk.Combobox(current_frame,textvariable=self.var_dept,font=("times new roman",12,),state="readonly")
        dept_combo["value"]=("Select Department","Agricultural Engineering","Biotechnology","Computer Science Engineering","Electronic Communication Engineering","Information Technology")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=3,padx=25,pady=5,sticky=W) 

        #year details
        year_lbl=Label(current_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=25,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,),state="readonly")
        year_combo["value"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,sticky=W)

        #Semester details
        sem_lbl=Label(current_frame,text="Semester",font=("times new roman",14,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=5,sticky=W)

        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12,),state="readonly")
        sem_combo["value"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=25,pady=5,sticky=W) 

        #Stdent Details
        student_frame=LabelFrame(left_frmae,bd=2,bg="white" ,relief=RIDGE,text="Class Student Information",font=("times new roman",12))
        student_frame.place(x=0,y=240,width=630,height=265)


        #roll no
        student_rollno_lbl=Label(student_frame,text="Roll. No.",font=("times new roman",12,"bold"),bg="white")
        student_rollno_lbl.grid(row=0,column=0,padx=5,pady=4,sticky=W)

        student_roll_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=22,font=("times new roman",12))
        student_roll_entry.grid(row=0,column=1,padx=5,pady=4,sticky=W)

        #Name no
        student_name_lbl=Label(student_frame,text="Student's Name",font=("times new roman",12,"bold"),bg="white")
        student_name_lbl.grid(row=0,column=2,padx=15,pady=4,sticky=W)

        student_name_entry=ttk.Entry(student_frame,textvariable=self.var_name,width=20,font=("times new roman",12))
        student_name_entry.grid(row=0,column=3,padx=10,pady=4,sticky=W)

        #gender no
        student_gender_lbl=Label(student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        student_gender_lbl.grid(row=1,column=0,padx=5,pady=4,sticky=W)

        students_gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gen,font=("times new roman",12,),state="readonly")
        students_gender_combo["value"]=("Select Gender","Male","Female","Others")
        students_gender_combo.current(0)
        students_gender_combo.grid(row=1,column=1,padx=5,pady=4,sticky=W)


        #DOB no
        student_dob_lbl=Label(student_frame,text="Student's DOB",font=("times new roman",12,"bold"),bg="white")
        student_dob_lbl.grid(row=1,column=2,padx=15,pady=4,sticky=W)

        student_dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        student_dob_entry.grid(row=1,column=3,padx=10,pady=4,sticky=W)

        #Email no
        student_gender_lbl=Label(student_frame,text="Email ID",font=("times new roman",12,"bold"),bg="white")
        student_gender_lbl.grid(row=2,column=0,padx=5,pady=4,sticky=W)

        student_email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=22,font=("times new roman",12))
        student_email_entry.grid(row=2,column=1,padx=8,pady=4,sticky=W)
        
        #Phone no
        student_phoneno_lbl=Label(student_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        student_phoneno_lbl.grid(row=2,column=2,padx=15,pady=4,sticky=W)

        student_phoneno_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        student_phoneno_entry.grid(row=2,column=3,padx=10,pady=4,sticky=W)

        #Address 
        student_address_lbl=Label(student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        student_address_lbl.grid(row=3,column=0,padx=5,pady=4,sticky=W)

        student_address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=22,font=("times new roman",12))
        student_address_entry.grid(row=3,column=1,padx=8,pady=4,sticky=W)
        
        # #Teacher's name no
        # teachers_name_lbl=Label(student_frame,text="Teacher's Name",font=("times new roman",12,"bold"),bg="white")
        # teachers_name_lbl.grid(row=3,column=2,padx=15,pady=4,sticky=W)

        # teachers_name_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12))
        # teachers_name_entry.grid(row=3,column=3,padx=10,pady=4,sticky=W)

        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Sample Photo",value="Yes")
        radiobtn1.grid(row=5,column=1,padx=20,pady=4)

        radiobtn2=ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Sample Photo",value="No")
        radiobtn2.grid(row=5,column=2,padx=20,pady=4)

        #button frame
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=170,width=620,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # #photo btn frame
        btn_photo_frame=Frame(student_frame,bd=2,relief=RIDGE)
        btn_photo_frame.place(x=3,y=205,width=620,height=35)

        take_photo_btn=Button(btn_photo_frame,text="Take Photo Sample",command=self.generate_dataset,width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        # upadte_photo_btn=Button(btn_photo_frame,text="Update Photo Sample",command=self.training,width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.b1=Button(btn_photo_frame,text="Train model",command=self.train_classifier,width=30,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.b1.grid(row=0,column=1)




        #Right Frame
        right_frmae=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Display Student's Details",font=("times new roman",12))
        right_frmae.place(x=655,y=10,width=675,height=530)

        img_right=Image.open(r"college_images\facialrecognition.png")
        img_right=img_right.resize((662,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frmae,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=662,height=130)


        #Searching System
        searching_frame=LabelFrame(right_frmae,bd=2,bg="white" ,relief=RIDGE,text="Searching System",font=("times new roman",12))
        searching_frame.place(x=0,y=135,width=670,height=60)

        searchby_lbl=Label(searching_frame,text="Search By",font=("times new roman",12,"bold"),bg="white")
        searchby_lbl.grid(row=0,column=0,padx=5,pady=4,sticky=W)

        # searchby_combo=ttk.Combobox(searching_frame,font=("times new roman",12,),state="readonly")
        # searchby_combo["value"]=("Select","Roll. No.","Phone No.")
        # searchby_combo.current(0)
        # searchby_combo.grid(row=0,column=1,padx=5,pady=4,sticky=W)

        self.search_entry=ttk.Entry(searching_frame,width=22,font=("times new roman",12))
        self.search_entry.grid(row=0,column=1,padx=10,pady=4,sticky=W)

        self.search_btn=Button(searching_frame,text="Search",command=self.search_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        self.search_btn.grid(row=0,column=2,padx=5)

        self.showall_btn=Button(searching_frame,text="Show All",command=self.fetch_data,width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        self.showall_btn.grid(row=0,column=3,padx=5)


        #Table Frame
        table_frame=Frame(right_frmae,bd=2,bg="white" ,relief=RIDGE)
        table_frame.place(x=0,y=195,width=670,height=310)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("st_id","dept","year","sem","roll","name","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("st_id",text="Student's ID")
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll",text="Roll. No.")
        self.student_table.heading("name",text="Student's Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Student's DOB")
        self.student_table.heading("email",text="Email ID")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        # self.student_table.heading("teacher",text="Teacher's Name")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"


        self.student_table.column("st_id",width=100)
        self.student_table.column("dept",width=200)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=200)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        # self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # def add_data(self):
    #     if self.var_dept.get()=="Select Department":
    #         messagebox.showerror("error","All field are required")
    #     else:
    #         pass


    #Function Declaraction
    def add_data(self):
        if self.var_st_id.get()=="":
            messagebox.showerror("Error","Student's ID field is empty",parent=self.root)
        elif self.var_dept.get()=="Select Department":
            messagebox.showerror("error","Department field is empty",parent=self.root)
        elif self.var_year.get()=="Select Year":
            messagebox.showerror("error","Year field is empty",parent=self.root)
        elif self.var_sem.get()=="Select Semester":
            messagebox.showerror("error","Semester field is empty",parent=self.root)
        elif self.var_roll.get()=="":
            messagebox.showerror("error","Roll. No. field is empty",parent=self.root)
        elif self.var_name.get()=="":
            messagebox.showerror("error","Student's name field is empty",parent=self.root)
        elif self.var_gen.get()=="Select Gender":
            messagebox.showerror("error","Gender field is empty",parent=self.root)
        elif self.var_dob.get()=="":
            messagebox.showerror("error","Student's DOB field is empty",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("error","Email ID field is empty",parent=self.root)
        elif self.var_phone.get()=="":
            messagebox.showerror("error","Phone No. field is empty",parent=self.root)
        elif self.var_address.get()=="":
            messagebox.showerror("error","Address field is empty",parent=self.root)
        # elif self.var_teacher.get()=="":
        #     messagebox.showerror("error","Teacher's name field is empty",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(


                                                                                            self.var_st_id.get(),
                                                                                            self.var_dept.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_gen.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            # self.var_teacher.get(),
                                                                                            self.var_radio1.get()

                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student data has been inserted successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
        my_cursor=conn.cursor()
        # my_cursor.execute("select * from students where st_id=%s",(
        #                                                                             self.search_entry.get(),

        #                                                                                 ))
        query=("select * from students where roll=%s or name=%s or st_id=%s")
        value=(self.search_entry.get(),self.search_entry.get(),self.search_entry.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in row:
                self.student_table.insert("",END,values=i)
            conn.commit()
        else:
            messagebox.showerror("Error","Invalid input, please provide a valid Roll number")
        conn.close()

    #fetch data from the database
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_st_id.set(data[0]),
        self.var_dept.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gen.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        # self.var_teacher.set(data[11]),
        self.var_radio1.set(data[11])

    #Update function
    def update_data(self):
        if self.var_st_id.get()=="":
            messagebox.showerror("Error","Student's ID field is empty",parent=self.root)
        elif self.var_dept.get()=="Select Department":
            messagebox.showerror("error","Department field is empty",parent=self.root)
        elif self.var_year.get()=="Select Year":
            messagebox.showerror("error","Year field is empty",parent=self.root)
        elif self.var_sem.get()=="Select Semester":
            messagebox.showerror("error","Semester field is empty",parent=self.root)
        elif self.var_roll.get()=="":
            messagebox.showerror("error","Roll. No. field is empty",parent=self.root)
        elif self.var_name.get()=="":
            messagebox.showerror("error","Student's name field is empty",parent=self.root)
        elif self.var_gen.get()=="Select Gender":
            messagebox.showerror("error","Gender field is empty",parent=self.root)
        elif self.var_dob.get()=="":
            messagebox.showerror("error","Student's DOB field is empty",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("error","Email ID field is empty",parent=self.root)
        elif self.var_phone.get()=="":
            messagebox.showerror("error","Phone No. field is empty",parent=self.root)
        elif self.var_address.get()=="":
            messagebox.showerror("error","Address field is empty",parent=self.root)
        # elif self.var_teacher.get()=="":
        #     messagebox.showerror("error","Teacher's name field is empty",parent=self.root)
        else:
            try:
                update_mess=messagebox.askyesno("Update","Do you want to update this Student deatils",parent=self.root)
                if update_mess>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update students set Dep=%s,Year=%s,sem=%s,roll=%s,name=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,Photosample=%s where st_id=%s",(

                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_name.get(),
                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                    self.var_address.get(),
                                                                                                                                                    # self.var_teacher.get(),
                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                    self.var_st_id.get(),

                                                                                                                                                                ))
                else:
                    if not update_mess:
                        return
                messagebox.showinfo("Success","Student details has been updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #Delete Function
    def delete_data(self):
        if self.var_st_id.get()=="":
            messagebox.showerror("Error","Student's ID is required for performing this action",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete student details","Do you wnat to delete this student details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from students where st_id=%s"
                    val=(self.var_st_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #Reset
    def reset_data(self):
        self.var_st_id.set("")
        self.var_dept.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        # self.var_teacher.set("")
        self.var_radio1.set("")


    #Generate Data set or take a photo
    def generate_dataset(self):
        if self.var_st_id.get()=="":
            messagebox.showerror("Error","Student's ID field is empty",parent=self.root)
        elif self.var_dept.get()=="Select Department":
            messagebox.showerror("error","Department field is empty",parent=self.root)
        elif self.var_year.get()=="Select Year":
            messagebox.showerror("error","Year field is empty",parent=self.root)
        elif self.var_sem.get()=="Select Semester":
            messagebox.showerror("error","Semester field is empty",parent=self.root)
        elif self.var_roll.get()=="":
            messagebox.showerror("error","Roll. No. field is empty",parent=self.root)
        elif self.var_name.get()=="":
            messagebox.showerror("error","Student's name field is empty",parent=self.root)
        elif self.var_gen.get()=="Select Gender":
            messagebox.showerror("error","Gender field is empty",parent=self.root)
        elif self.var_dob.get()=="":
            messagebox.showerror("error","Student's DOB field is empty",parent=self.root)
        elif self.var_email.get()=="":
            messagebox.showerror("error","Email ID field is empty",parent=self.root)
        elif self.var_phone.get()=="":
            messagebox.showerror("error","Phone No. field is empty",parent=self.root)
        elif self.var_address.get()=="":
            messagebox.showerror("error","Address field is empty",parent=self.root)
        # elif self.var_teacher.get()=="":
        #     messagebox.showerror("error","Teacher's name field is empty",parent=self.root)
        else:
            try:        
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from students")
                my_result=my_cursor.fetchall()
                id=0
                for i in my_result:
                    id+=1
                my_cursor.execute("update students set Dep=%s,Year=%s,sem=%s,roll=%s,name=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,Photosample=%s where st_id=%s",(

                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                    self.var_name.get(),
                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                    self.var_email.get(),
                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                    self.var_address.get(),
                                                                                                                                                    # self.var_teacher.get(),
                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                    self.var_st_id.get()==id+1

                                                                                                                                                                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #Load predefined data on frontal face opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3 = default hota hai
                    #Minimum neighbours=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set has been completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    #train
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")   #converts into grayscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training data",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #Train the classifier and Save it
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset has been Completed!!!")

    # def enter_func(self,event):
    #     self.b1.invoke()



    # def training(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Train(self.new_window)






if __name__ =="__main__":
    root=Tk()
    obj=Students(root)
    root.mainloop()