from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title("AI ChatBot")
        self.root.geometry("600x540+400+80")
        self.root.bind("<Return>",self.enter_func)

        #main frame
        main_frame=Frame(self.root,bd=4,bg="powder blue",width=530)
        main_frame.pack()

        #Bot Image
        img_chat=Image.open("college_images\chatbot-data.png")
        img_chat=img_chat.resize((100,70),Image.ANTIALIAS)
        self.pho_img=ImageTk.PhotoImage(img_chat)

        t_lbl=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=600,compound=LEFT,image=self.pho_img,text="     Hey!, How may I help you ?",font=("arial",20,"bold"),fg="green",bg="white")
        t_lbl.pack(side=TOP)


        #scroll bar
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=18,bd=4,fg="black",relief=RAISED,font=("arial",13),yscrollcommand=self.scroll_y.set)

        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        #button frame
        btn_frame=Frame(self.root,bd=4,bg="white",width=600)
        btn_frame.pack()


        label=Label(btn_frame,text="Type something here ...",font=("arial",13,"bold"),fg="green",bg="white")
        label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        #Entry box
        self.entry=StringVar()
        self.var_entry=ttk.Entry(btn_frame,textvariable=self.entry,width=38,font=("times new roman",14))
        self.var_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Button
        self.sendit=Button(btn_frame,text="Send",command=self.send,font=("arial",15,"bold"),width=8,bg="darkgreen",fg="white")
        self.sendit.grid(row=1,column=1,padx=260,pady=8,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clearit,font=("arial",15,"bold"),width=10,bg="red",fg="white")
        self.clear.grid(row=1,column=0,padx=15,pady=8,sticky=W)


        self.msg=""
        self.label11=Label(btn_frame,text=self.msg,font=("arial",13,"bold"),fg="red",bg="white")
        self.label11.grid(row=1,column=1,padx=5,pady=5,sticky=W)


    # Function for send
    def send(self):
        send="\n\t\t\t\t"+"You: "+ self.entry.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if (self.entry.get()==""):
            self.msg="Please enter you query"
            self.label11.config(text=self.msg,fg="red")
        else:
            self.msg=""
            self.label11.config(text=self.msg,fg="red")

        if (self.entry.get()=="Hello" or self.entry.get()=="hello" or self.entry.get()=="HELLO"):
            self.text.insert(END,"\n\n"+"Kachra : Hello Ji Namaste, I'm Kachra --version 0.1")
        elif (self.entry.get()=="hi" or self.entry.get()=="Hi" or self.entry.get()=="HI"):
            self.text.insert(END,"\n\n"+"Kachra : Hey Namaste, I'm Kachra --version 0.1")
        elif (self.entry.get()=="How are you ?" or self.entry.get()=="how are you ?"):
            self.text.insert(END,"\n\n"+"Kachra : I'm doing great sir, and a new version of\n \tmyself is in on the way, my creator is currently on it.\n \tHope you are having a nice day.")
        elif (self.entry.get()=="Who is your creator ?" or self.entry.get()=="who is your creator ?"):
            self.text.insert(END,"\n\n"+"Kachra : My creators is Subodh Kumar Ray")
        elif (self.entry.get()=="What is your name ?" or self.entry.get()=="tumhara naam kya hai ?"):
            self.text.insert(END,"\n\n"+"Kachra : My name is Er. Kachra :)")
        elif (self.entry.get()=="Can you speak hindi ?"):
            self.text.insert(END,"\n\n"+"Kachra : I'm still in learning phase, Mujhe Hindi\n \titne achi nhi ati hai ;( ")
        elif (self.entry.get()=="What is machine learning ?" or self.entry.get()=="What is ML ?"):
            self.text.insert(END,"\n\n"+"Kachra : Machine learning (ML) is the study of computer\n \t algorithms that improve automatically\n \tthrough experience and by the use of data. It is seen as a\n \tpart of artificial intelligence.\n \tMachine learning algorithms build a model\n \t based on sample data, known as training\n \tdata, in order to make predictions or decisions\n \t without being explicitly programmed to do so.\n \tMachine learning algorithms are used in a\n \twide variety of applications, such as in medicine,\n \t email filtering, and computer vision, where it is\n \tdifficult or unfeasible to develop conventional\n \talgorithms to perform the needed tasks.")
        else:
            self.text.insert(END,"\n\n"+"Kachra : Sorry :( , I couldn't understand, please try again :)")


    #Enter function
    def enter_func(self,event):
        self.sendit.invoke()
        self.entry.set("")



    #function for clear
    def clearit(self):
        self.text.delete("1.0",END)
        self.entry.set("")





if __name__ =="__main__":
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()
