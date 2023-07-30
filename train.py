from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Панель Обучения")

        # Эта часть является началом настройки меток изображений.
        # первое изображение заголовка  
        img=Image.open(r"C:\Users\ikbol\OneDrive\Рабочий стол\Python-FYP\Python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # установить изображение в качестве метки
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # изображение на заднем плане
        bg1=Image.open(r"C:\Users\ikbol\OneDrive\Рабочий стол\Python-FYP\Python_Test_Projects\Images_GUI\t_bg1.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # установить изображение в качестве метки
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #раздел заголовка
        title_lb1 = Label(bg_img,text="Добро пожаловать в панель обучения",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Создайте кнопки под разделом
        # ------------------------------------------------------------------------------------------------------------------- 
        # Кнопка обучения 1
        std_img_btn=Image.open(r"C:\Users\ikbol\OneDrive\Рабочий стол\Python-FYP\Python_Test_Projects\Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Обучение данным",cursor="hand2",font=("tahoma",13,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)

    # ==================Создать функцию обучения===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # преобразовать в оттенки серого
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
                                    
            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Классификатор обучения=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Результат","Набор обучающих данных собран!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()