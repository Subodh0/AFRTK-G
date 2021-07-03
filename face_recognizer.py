from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1365x755+0+0")
        self.root.title("Face Recognizer")
        self.root.bind("<Return>",self.enter_func)

        #title for training model
        title_lbl=Label(self.root, text="Face Recognizer", font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1365,height=60)

        #right image
        img_right=Image.open(r"college_images\face_detector1.jpg")
        img_right=img_right.resize((620,683),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl1=Label(self.root,image=self.photoimg_right)
        f_lbl1.place(x=0,y=60,width=620,height=683)

        #left image
        img_left=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_left=img_left.resize((746,683),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=620,y=60,width=746,height=683)


        #buttton
        self.b1=Button(f_lbl,text="Detect Face",cursor="hand2",command=self.face_recog,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        self.b1.place(x=315,y=603,width=120,height=40)

    ##Attendaence
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

    def enter_func(self,event):
        self.b1.invoke()





if __name__ =="__main__":
    root=Tk()
    obj=Face_recognizer(root)
    root.mainloop()