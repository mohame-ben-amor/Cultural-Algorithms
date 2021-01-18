import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sqlite3
import os
import subprocess, sys
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

plt.show()

global filename

class Login():
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.master = master
        self.master.geometry("517x265+373+170")
        self.master.title("Formulaire de Connexion")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.master)
        self.Entry1.place(relx=0.387, rely=0.415,height=20, relwidth=0.317)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.master)
        self.Entry2.place(relx=0.387, rely=0.604,height=20, relwidth=0.317)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(show="*")

        self.Message1 = tk.Message(self.master)
        self.Message1.place(relx=0.329, rely=0.113, relheight=0.238, relwidth=0.426)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font="-family {Times New Roman} -size 19 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Se Connecter''')
        self.Message1.configure(width=220)

        self.Message2 = tk.Message(self.master)
        self.Message2.place(relx=0.155, rely=0.415, relheight=0.087, relwidth=0.193)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Nom d'utilisateur:''')
        self.Message2.configure(width=100)

        self.Button1 = tk.Button(self.master)
        self.Button1.place(relx=0.503, rely=0.755, height=24, width=66)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Connecter''')
        self.Button1.configure(command= self.gotoSysteme)

        self.Message3 = tk.Message(self.master)
        self.Message3.place(relx=0.174, rely=0.604, relheight=0.087, relwidth=0.168)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Mot de passe:''')
        self.Message3.configure(width=87)
    def finishPage(self):
        self.master.destroy()

    def gotoSysteme(self):
        username = self.Entry1.get()
        password = self.Entry2.get()
        connection = sqlite3.connect("BaseDeDonnee.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (str(username), str(password)))
        if (len(result.fetchall()) > 0):
            print("User Found ! ")
            root2 = Toplevel(self.master)
            myGUI = Systeme(root2)
        else:
            print("User Not Found !")

        connection.close()

        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')


class Systeme():
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92

        self.master = master
        self.master.geometry("581x337+386+166")
        self.master.title("Application de Système")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.Message1 = tk.Message(self.master)
        self.Message1.place(relx=0.258, rely=0.0, relheight=0.246, relwidth=0.551)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font="-family {Monotype Corsiva} -size 16 -slant italic")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''CATALYST''')
        self.Message1.configure(width=320)
        self.Button3 = tk.Button(self.master)
        self.Button3.place(relx=0.327, rely=0.267, height=41, width=221)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Times New Roman} -size 13")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Add your DataSet ''')
        self.Button3.configure(command= self.gotoDataBase)

        self.Button4 = tk.Button(self.master)
        self.Button4.place(relx=0.327, rely=0.475, height=41, width=221)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Times New Roman} -size 13")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text=''' Normal Visualization ''')
        self.Button4.configure(command= self.gotoMethodeRecognition)

        self.Button5 = tk.Button(self.master)
        self.Button5.place(relx=0.327, rely=0.712, height=41, width=221)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Times New Roman} -size 13")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Simulation of C.A''')
        self.Button5.configure(command= self.afficherourSolution)

        self.Button7 = tk.Button(self.master)
        self.Button7.place(relx=0.775, rely=0.89, height=24, width=87)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Times New Roman} -size 11")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Exit''')
        self.Button7.configure(command= self.finish)

    def gotoDataBase(self):
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\azus\\AppData\\Local\\Programs\\Python\\Python39", title="Select A file", filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
        print(filename1)

    def gotoMethodeRecognition(self):
        root2 = Toplevel(self.master)
        myGUI = presentationErreur(root2)

    def gotoMarquage(self):
        root2 = Toplevel(self.master)
        myGUI = ourSoution(root2)

    def finish(self):
        self.master.destroy()

    def afficherourSolution(self):
        df = pd.read_csv('College_Data',index_col=0)

        sns.set_style('whitegrid')
        sns.lmplot(x='Room.Board',y='Grad.Rate',data=df, hue='Private',
                   palette='coolwarm',height=6,fit_reg=False)


        sns.set_style('darkgrid')
        g = sns.FacetGrid(df,hue="Private",palette='coolwarm',height=6,aspect=2)
        g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=1).fig.show()

        kmeans = KMeans(n_clusters=4)

        y_predicted = kmeans.fit_predict(df[['Apps','Accept']])

        kmeans.cluster_centers_
        df['cluster'] = y_predicted

        df1 = df[df.cluster==0]
        df2 = df[df.cluster == 1]
        df3 = df[df.cluster == 2]

        plt.scatter(df1.Apps,df1['Accept'],color='green')
        plt.scatter(df2.Apps,df2['Accept'],color='red')
        plt.scatter(df3.Apps,df1['Accept'],color='blue')

        df1 = df[df.cluster==0]
        df2 = df[df.cluster == 1]
        df3 = df[df.cluster == 2]

        plt.scatter(df1.Apps,df1['Accept'],color='green')
        plt.scatter(df2.Apps,df2['Accept'],color='red')
        plt.scatter(df3.Apps,df1['Accept'],color='blue')

class presentationErreur():
    df = pd.read_csv('College_Data',index_col=0)

    def __init__(self, master):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Monotype Corsiva} -size 18 -weight normal "  \
        "-slant italic -underline 0 -overstrike 0"
        self.master = master
        self.master.geometry("517x265+373+170")
        self.master.title("Visualization")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.Button3 = tk.Button(self.master)
        self.Button3.place(relx=0.328, rely=0.221, height=41, width=221)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Times New Roman} -size 13")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Visualization 1 ''')
        self.Button3.configure(command=self.afficherErreur1)


        self.Button4 = tk.Button(self.master)
        self.Button4.place(relx=0.328, rely=0.650, height=41, width=221)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Times New Roman} -size 13")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Visualization 2''')
        self.Button4.configure(command=self.afficherErreur2)

        
    def afficherErreur1(self):
        #print(filename)
        sns.set_style('whitegrid')
        sns.lmplot(x='Room.Board',y='Grad.Rate',data=self.df, hue='Private', palette='coolwarm',height=6,fit_reg=False).fig.show()

    def afficherErreur2(self):
        sns.set_style('darkgrid')
        g = sns.FacetGrid(self.df,hue="Private",palette='coolwarm',height=6,aspect=2)
        g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=1).fig.show()


    def finish(self):
        self.master.destroy()


class ourSoution():
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Monotype Corsiva} -size 18 -weight normal "  \
        "-slant italic -underline 0 -overstrike 0"

        self.master = master
        self.master.geometry("463x319+386+166")
        self.master.title("Notre Solution")
        self.master.configure(background="#d9d9d9")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.Message1 = tk.Message(self.master)
        self.Message1.place(relx=0.022, rely=-0.031, relheight=0.323, relwidth=0.929)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Buuton''')
        self.Message1.configure(width=430)

        self.Button4 = tk.Button(self.master)
        self.Button4.place(relx=0.328, rely=0.393, height=41, width=221)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Times New Roman} -size 13")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Erreur2''')
        self.Button4.configure(command=self.afficherOurSolution)
               
    def finish(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    myGUI = Login(root)
    root.mainloop()
import sqlite3

def createTable():
    connection = sqlite3.connect('BaseDeDonnee.db')

    connection.execute("CREATE TABLE IF NOT EXISTS USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)")

    connection.execute("CREATE TABLE IF NOT EXISTS ETUDIANT(IDETUDIANT TEXT NOT NULL,ETUDIANTNAME TEXT ,MATRICULE TEXT,CLASSE TEXT,IMAGE BLOP)")

    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('admin','admin','admin'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")
    
    for data in result:
        print("Username : ",data[0])
        print("Email : ",data[1])
        print("Password :",data[2])

    connection.close()

createTable()

if __name__  == '__main__':
    main()
