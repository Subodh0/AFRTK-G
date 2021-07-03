from datetime import date
from time import time
from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Attendance Details")


        #Data Variables
        self.var_st_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

        # Image 1
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((455,190),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=455,height=190)

        #image2
        img1=Image.open(r"college_images\girl.jpeg")
        img1=img1.resize((455,190),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=455,y=0,width=455,height=190)

        #image3
        img2=Image.open(r"college_images\dev.jpg")
        img2=img2.resize((457,190),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=910,y=0,width=457,height=190)


        #Background Image
        img3=Image.open(r"college_images\BestFacialRecognition.jpg")
        img3=img3.resize((1366,560),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=190,width=1366,height=560)

        #Title
        title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",28,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1365,height=45)

        #main frame
        main_frame=Frame(bg_img,bd=3,bg="white")
        main_frame.place(x=10,y=50,width=1345,height=497)

        #Left Frame
        left_frmae=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12))
        left_frmae.place(x=10,y=5,width=600,height=477)


        #left image
        img_left=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_left=img_left.resize((585,170),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frmae,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=585,height=170)

        #left inside frame
        left_inside_frame=Frame(left_frmae,bd=3,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=180,width=580,height=265)



        #++++++++++++++Label ENTRY++++++++++++++++++++++
        #student ID
        student_id_lbl=Label(left_inside_frame,text="Student ID",font=("times new roman",11,"bold"),bg="white")
        student_id_lbl.grid(row=0,column=0,padx=10,pady=12,sticky=W)

        studend_id_entry=ttk.Entry(left_inside_frame,textvariable=self.var_st_id,width=18,font=("times new roman",11))
        studend_id_entry.grid(row=0,column=1,padx=10,pady=12,sticky=W)

        #student roll
        student_roll_lbl=Label(left_inside_frame,text="Roll. No.",font=("times new roman",11,"bold"),bg="white")
        student_roll_lbl.grid(row=0,column=2,padx=15,pady=12,sticky=W)

        student_roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=22,font=("times new roman",11))
        student_roll_entry.grid(row=0,column=3,padx=10,pady=12,sticky=W)

        #student NAME
        student_name_lbl=Label(left_inside_frame,text="Student Name",font=("times new roman",11,"bold"),bg="white")
        student_name_lbl.grid(row=1,column=0,padx=10,pady=12,sticky=W)

        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=18,font=("times new roman",11))
        student_name_entry.grid(row=1,column=1,padx=10,pady=12,sticky=W)

        #dept name
        dept_lbl=Label(left_inside_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        dept_lbl.grid(row=1,column=2,padx=5,sticky=W)

        dept_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_dept,font=("times new roman",11,),state="readonly")
        dept_combo["value"]=("Select Department","Agricultural Engineering","Biotechnology","Computer Science Engineering","Electronic Communication Engineering","Information Technology")
        dept_combo.current(0)
        dept_combo.grid(row=1,column=3,padx=10,pady=12,sticky=W)


        #Time
        time_lbl=Label(left_inside_frame,text="Time",font=("times new roman",11,"bold"),bg="white")
        time_lbl.grid(row=2,column=0,padx=10,pady=12,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=18,font=("times new roman",11))
        time_entry.grid(row=2,column=1,padx=10,pady=12,sticky=W)

        #Date
        date_lbl=Label(left_inside_frame,text="Date",font=("times new roman",11,"bold"),bg="white")
        date_lbl.grid(row=2,column=2,padx=15,pady=12,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_date,width=22,font=("times new roman",11))
        date_entry.grid(row=2,column=3,padx=10,pady=12,sticky=W)


        #attendance status
        attendance_lbl=Label(left_inside_frame,text="Attendance status",font=("times new roman",11,"bold"),bg="white")
        attendance_lbl.grid(row=3,column=0,padx=0,sticky=W)

        attendance_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_status,font=("times new roman",11,),state="readonly")
        attendance_combo["value"]=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=5,pady=12,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=431,height=45)

        # save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",14,"bold"),bg="blue",fg="white")
        # save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",16,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",16,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)

        #right frame
        right_frmae=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Attendance Details",font=("times new roman",12))
        right_frmae.place(x=635,y=5,width=695,height=477)

        #right inside frame
        table_frame=Frame(right_frmae,bd=3,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=3,width=670,height=440)


        #Scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_attendance_table=ttk.Treeview(table_frame,column=("Student's ID","Roll. No.","Student's Name","Department","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_attendance_table.xview)
        scroll_y.config(command=self.student_attendance_table.yview)

        self.student_attendance_table.heading("Student's ID",text="Student's ID")
        self.student_attendance_table.heading("Roll. No.",text="Roll. No.")
        self.student_attendance_table.heading("Student's Name",text="Student's Name")
        self.student_attendance_table.heading("Department",text="Department")
        self.student_attendance_table.heading("Time",text="Time")
        self.student_attendance_table.heading("Date",text="Date")
        self.student_attendance_table.heading("Status",text="Status") 
        self.student_attendance_table["show"]="headings"

        self.student_attendance_table.column("#0")
        self.student_attendance_table.column("#1",width=100)
        self.student_attendance_table.column("#2",width=100)
        self.student_attendance_table.column("#3",width=200)
        self.student_attendance_table.column("#4",width=200)
        self.student_attendance_table.column("#5",width=100)
        self.student_attendance_table.column("#6",width=100)
        self.student_attendance_table.column("#7",width=100)


        self.student_attendance_table.pack(fill=BOTH,expand=1)

        with open('attendance.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                # print(row)
                global myData
                st_id = row["si"]
                roll = row["roll"]
                name = row["name"]
                dept = row["dept"]
                time = row["time"]
                date = row["date"]
                status = row["status"]
                myData = self.student_attendance_table.insert("", 0, values=(st_id, roll, name, dept, time, date, status))

        self.student_attendance_table.bind("<ButtonRelease>",self.get_cursor)

        
        # self.fetch_data()
    
    
    #Fetch data
    def fetch_data(self,rows):
        self.student_attendance_table.delete(*self.student_attendance_table.get_children())
        for i in rows:
            self.student_attendance_table.insert("",END,values=i)
    
    #Import CSV file
    # def importCsv(self):
        # global myData
        # myData.clear()
        # fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        # with open(fln) as myfile:
        #     csvread=csv.reader(myfile, delimiter=",")
        #     for i in csvread:
        #         myData.append(i)
        #     self.fetch_data(myData)

    #Export CSV file
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data has been exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_attendance_table.focus()
        content=self.student_attendance_table.item(cursor_focus)
        data=content["values"]

        self.var_st_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_status.set(data[6])



    #Reset
    def reset_data(self):
        self.var_st_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("Select Department")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")










if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()