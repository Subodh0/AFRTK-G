from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
import cv2
import mysql.connector
from tkinter import messagebox
from students import Students
from train import Train
from face_recognizer import Face_recognizer
from attendance import Attendance
from chatbot import Chatbot

class Face_Recognition_System_student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Face Recognition System")

        # Image 1
        img=Image.open(r"college_images\facialrecognition.png")
        img=img.resize((455,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=455,height=130)

        #image2
        img1=Image.open(r"college_images\images.jpg")
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
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1365,height=45)

        #Time
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=("times new roman",14),bg="white",fg="blue")
        lbl.place(x=5,y=0,width=120,height=50)
        time()

        # #Students button
        # img4=Image.open(r"college_images\student.jpg")
        # img4=img4.resize((180,180),Image.ANTIALIAS)
        # self.photoimg4=ImageTk.PhotoImage(img4)

        # b1=Button(bg_img,image=self.photoimg4,command=self.student_detail,cursor="hand2")
        # b1.place(x=200,y=100,width=180, height=180)

        # b1_1=Button(bg_img,text="Student Details",command=self.student_detail,cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=200,y=280,width=180,height=30)

        #Detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recog)
        b2.place(x=200,y=100,width=180, height=180)

        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=200,y=280,width=180,height=30)


        #Attendance face button
        img6=Image.open(r"college_images\girl.jpeg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attend)
        b3.place(x=450,y=100,width=180, height=180)

        b3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attend,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=450,y=280,width=180,height=30)


        #Help button
        img7=Image.open(r"college_images\NyftyBot_small_512x512.webp")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chat_box)
        b4.place(x=700,y=100,width=180, height=180)

        b4_4=Button(bg_img,text="Help Desk",cursor="hand2",command=self.chat_box,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=700,y=280,width=180,height=30)

        # #Train Face button
        # img8=Image.open(r"college_images\images.jpg")
        # img8=img8.resize((180,180),Image.ANTIALIAS)
        # self.photoimg8=ImageTk.PhotoImage(img8)

        # b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        # b5.place(x=200,y=350,width=180, height=180)

        # b5_5=Button(bg_img,text="Train Data Model",cursor="hand2",command=self.train_data,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        # b5_5.place(x=200,y=530,width=180,height=30)

        # #Photos button
        # img9=Image.open(r"college_images\clg.jpg")
        # img9=img9.resize((180,180),Image.ANTIALIAS)
        # self.photoimg9=ImageTk.PhotoImage(img9)

        # b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_images)
        # b6.place(x=200,y=350,width=180, height=180)

        # b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_images,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        # b6_6.place(x=200,y=530,width=180,height=30)


        #Dev page button
        # img10=Image.open(r"college_images\dev.jpg")
        # img10=img10.resize((180,180),Image.ANTIALIAS)
        # self.photoimg10=ImageTk.PhotoImage(img10)

        # b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        # b7.place(x=950,y=100,width=180, height=180)

        # b7_7=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        # b7_7.place(x=950,y=280,width=180,height=30)

        #Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=200,y=350,width=180, height=180)

        b8_8=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=200,y=530,width=180,height=30)


    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_List=[]
            for line in myDatalist:
                entry=line.split((","))
                name_List.append(entry[0])
            if ((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    



    #=================Face Recogniton===============
    def face_recog(self):
        def draw_boundary(img,classifier,ScaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,ScaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from students where st_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from students where st_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from students where st_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select st_id from students where st_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>77:
                    cv2.putText(img,f"Student's ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Roll. No.:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognizer",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    #exit
    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Exit","Are you sure you want exit?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    #Open images
    def open_images(self):
        os.startfile("data")


    #Function Buttons
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Students(self.new_window)

    # def train_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Train(self.new_window)

    # def face_detect(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_recognizer(self.new_window)

    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def chat_box(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)



    






if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System_student(root)
    root.mainloop()