import re
import random
from tkinter import*
from tkinter.messagebox import *
from tkinter import ttk

''' if(len(Enter.get())==0 or ' ' in Enter.get() or any(Char.isdigit() for Char in Enter.get()) or any(Char in '#@!$%^&*~' for Char in Enter.get())):


Proepr Validations on Entry Box Data as for Password Context : 

1. Must Not be Any Space 
2. Must Not be Any Digit in context(Check made by using any Func)
3. Must Not be Any Special Charcater in Context (Check made by using any Func)
4. Must Not be Empty Context(As Empty Entry Widget)
5. Must Password Context Contain All Alphabets 
6. Must be Alteast 5 Chars Of Length Context and Upto 10 Chars Long '''

def Random_Generate_Password(Pass_Length,Context):
    
    Final_Pass = str()
    U,L,D,S,R = 0,0,0,0,0
    Temp_Len = Pass_Length

    if(Pass_Length>=6 and Pass_Length<=10):                 #Means It Can be Upto 25 Chars 
        
        
        if(len(Context)==5):            #For Differnet Gaps of Password Lengths there are Separate Logic for Generate Password Based upon the Length of Context Entered by user

            
            U,L,D,S=2,1,2,1
            
            R = max(0,Temp_Len-6)
            
        elif(len(Context)>5):
            U,L,D,S = 2,3,1,1
            R = max(0,Temp_Len-7)
            Final_Pass = Generate(U,L,D,S,R,Context)
        else: pass  

    elif(Pass_Length>10  and Pass_Length<=15):

        if(len(Context)==5):

            U,L,D,S = 3,2,2,2
            R = max(0,Temp_Len-9)
            Final_Pass = Generate(U,L,D,S,R,Context)
        elif(len(Context)>5):
            U,L,D,S = 3,3,2,2
            R = max(0,Temp_Len-10)
            Final_Pass = Generate(U,L,D,S,R,Context)
        else: pass

    elif(Pass_Length>15 and Pass_Length<=20):

        if(len(Context)==5):
            U,L,D,S = 3,2,4,4
            R = max(0,Temp_Len-13)
            Final_Pass = Generate(U,L,D,S,R,Context)
        elif(len(Context)>5):
            U,L,D,S = 3,3,4,4
            R = max(0,Temp_Len-14)
            Final_Pass = Generate(U,L,D,S,R,Context)
        else: pass
    elif(Pass_Length>20):   #May be Can Take Upto 25
        if(len(Context)==5):
            U,L,D,S = 3,2,5,5
            R = max(0,Temp_Len-15)
            Final_Pass = Generate(U,L,D,S,R,Context)
        elif(len(Context)>5):
            U,L,D,S = 3,3,5,5
            R = max(0,Temp_Len-16)
            Final_Pass = Generate(U,L,D,S,R,Context)
        else: pass
    else: pass

    return Final_Pass    

def Generate(Up,Lo,Dg,Spl,Rem,Context):        #This Part is Basically Resposible for Genarting the password BAsed Upon the Given Args that is Each Corresponding Componets of Password Like UpperCase, Lowercase , Spl , Digits
    Passwd = str()
    
    Upr = Context[:Up:].upper()
    Lwr = Context[Up:(Lo+Up):].lower()

    Rest = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(Rem)]
    Rest = ''.join(Rest)

    Dgts = [random.choice('0123456789') for _ in range(Dg)]
    Dgts = ''.join(Dgts)

    Sp = [random.choice('@#$%&~!') for _ in range(Spl)]
    Sp = ''.join(Sp)

    Passwd = Upr+Lwr+Rest+Dgts+Sp
    P = r'\b(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{10,}'

    #print(Passwd)
    try:
        if(re.search(P,Passwd)):
            return Passwd
    except Exception as E:
        print("Issue with Password")   
        
def Copy_To_Clip():    

    E1.select_range(0,END)  # Select all text
    E1.focus()
    E1.event_generate('<<Copy>>')  # Copy selected text to clipboard

    showinfo(title=' Copied Successfully ',message=' Password is Copied Successfully on the Screen ')
    Temp_Label = Label(W, text='Password Copied to Clipboard', font=('Times New Roman', 12), bg='khaki1', fg='black')
    Temp_Label.place(relx=0.5, rely=0.9, anchor='center')
    
    # Remove the label after 2 seconds
    W.after(1500, Temp_Label.destroy)

def Quit():                                             #Procdeure For Quit the Very last Weindow Hwere That generated Passsword is Displayed
    Res = askyesno('Quit Request','Are You Sure You Want to be Quit?')
    if Res:
        W.destroy()
    else: pass

def Display_Password(Length,Context,Passwd):     #Correspondong Part is respobile for the Dipalying of the Actual password After Genarted Based Upon user's Given Paraamters ike Length, Pltform, and Context for the Password 


    global E1
    global W
    W = Tk()
    W.iconbitmap('PassIcon.ico')
    W.config(background='khaki1')
    W.geometry('500x400+500+90')
    W.title(" -- Pass Forge🔐 --")
    W.resizable(False,False)

    L1 = Label(W,text=' ** Password Generated Successfully **',font=('Times New Roman',15,'bold'),bg='khaki1',fg='black',bd=5,highlightbackground='maroon',highlightthickness=5,relief='groove')


    L2 = Label(W,text=f' Password Platform : {Platform} \n\n Password Length {Length} With Followed All Rules \n of Uppercase , Lowercase, Digits and Special Characters  ',font=('Times New Roman',13,'bold'),bg='khaki1',fg='black',bd=5,highlightbackground='maroon',highlightthickness=5,relief='groove')


    # L3 = Label(W,text=" <:> Generated Password <:> ",fg='darkslategray',bg='#FCE6C9',font=('Times New Roman',15,'bold'),bd = 8,highlightthickness=8,highlightbackground='lightcyan4',cursor='hand1',relief='sunken')

    E1 = Entry(W,font=('Calibri',17,'bold'),justify='center',selectbackground='blue',selectforeground='papayawhip',selectborderwidth=6,cursor='hand2',bd=7,highlightbackground='grey21',relief='sunken',highlightthickness=7)

    E1.insert(0,Passwd)
    E1.config(state='readonly',width=30,justify='center')

    copy_icon = PhotoImage(file='Copy.png')
    Copy_button = Button(W,font=('Times New Roman',2), image=copy_icon, command=Copy_To_Clip, bd=0, highlightthickness=0, cursor='hand2',bg='khaki1',activebackground='khaki4')

    #Write a Quit Button
    Quit_Button = Button(W,text='Quit',font=('Times New Roman',15,'bold'),bd=5,highlightbackground='maroon',highlightthickness=5,relief='groove',bg='red',fg='black',command=Quit)

    L1.place(x=70,y=10)
    L2.place(x=22,y=51)
    E1.place(relx=0.12,rely=0.50)
    Copy_button.place(relx=0.5, rely=0.8, anchor='center')  # Center the button
    Quit_Button.place(relx=0.9, rely=0.9, anchor='center')


    W.mainloop()


def Generate_Password(Context,Platform,Win):  #For Actually Invocation for the generating passsword and also for the Actyal Disply of Window to Show Generated Password
    Length= int(Spin.get())
    #print('\n\t Data Recieved : ',Length,Context,Platform)

    Window.destroy()
    Win.destroy()
    
    Pass_Wd = Random_Generate_Password(Length,Context)
    Display_Password(Length,Platform,Pass_Wd)
    
    

    #print(Random_Pass)
def Generate_Password_Window(Platform,Current_Index_Platform,Context_Pass):     #procdeure for Suring About the length based upoun the Platfrm and alse for AskinG actual Length of PAssword they Wanna Generate 
    
    global Length
    global Spin
    Win = Tk()
    Win.iconbitmap('PassIcon.ico')
    Win.config(background='khaki3')
    Win.geometry('450x350+500+90')
    Win.title(" -- Pass Forge🔐 --")
    Win.resizable(False,False)
    
    Detail = [f' Choosen Platform : {Platform} ',f'According to the Rules of the {Platform} \n Password  Must be at Least {Password_Details(Current_Index_Platform)} \n Characters  Long.']

    LL1 = Label(Win,text=Detail[0],font=('Times New Roman',15),highlightbackground='#EEE8AA',highlightthickness=3,bd=3,relief='groove',bg='#8B5742',fg='#FFFFE0')

    LL2 = Label(Win,text=Detail[1],font=('Time New Roman',15),highlightbackground='#EEE8AA',highlightthickness=3,bd=3,bg='khaki3',justify='center',relief='groove',fg='grey2')

    LL3 = Label(Win,text='Choose the Password Length Ahead Rules ⬇️',font=('Verdana',12,'bold'),bg='khaki3')

    
    Spin = Spinbox(Win,from_= Password_Details(Current_Index_Platform),to=25,font=('Times New Roman',16,'bold'))

    # print('\n Windpow Wale ke Andar : Length Hai - {} and Context Hai - {}'.format(Length,Context_Pass))
    
    Gen = Button(Win,font=('Montserrat',14,'bold'),text=" Generate Password ✔️",fg='beige',bg='darkorange4',highlightthickness=6,bd=6,highlightbackground='black',relief='sunken',activebackground='blue',activeforeground='papayawhip',command=lambda: Generate_Password(Context_Pass,Platform,Win))

    LL1.place(x=95,y=10)
    LL2.place(relx=0.09,rely=0.15)
    LL3.place(relx=0.075,rely=0.45)
    Spin.place(relx=0.25,rely=0.55)
    Gen.place(relx=0.21,rely=0.73)
    Win.mainloop()

def Password_Details(Current_Index_Platform):
    if(Current_Index_Platform==1 or Current_Index_Platform==2):
        return 8
    elif(Current_Index_Platform==3):
        return 6
    elif(Current_Index_Platform==4):
        return 10
    elif(Current_Index_Platform==5):
        return 12
    else: 
        pass

def Submit(event=None):                    #Validations for Context and the Choosen Platform  and also Including the Invocation of Genarte the Next Window to Ask the Length for PAssword based upon Chosen Platform 

    global Context_Pass
    global Platform

    Current_Index_Platform = Box.current()
    if(Current_Index_Platform==0):
        showerror('Invalid Platform','Please Must Select a Platform')
    elif(len(Enter.get())==0):
        showerror('Invalid Context','Please Must Enter a Context for Password')
    elif(' ' in Enter.get()):
        showerror('Invalid Context','Please Must Not Enter a Space in Context for Password')
    elif any(Char.isdigit() for Char in Enter.get()):
        showerror('Invalid Context','Please Must Not Enter a Digit in Context for Password')
    elif any(Char in '!@#$%^&*()~' for Char in Enter.get()):
        showerror('Invalid Context','Please Must Not Enter a Special Character in Context for Password')
    elif(len(Enter.get())<5 or (len(Enter.get())>10)):
        showerror('Invalid Context','Please Must Enter Context of Password of At Least  5 Characters or Long Upto 10 Characters')
    else:
        Platform = Box.get()
        Context_Pass = Enter.get()           #Getting the Context from the Entry Box 
        Generate_Password_Window(Platform,Current_Index_Platform,Context_Pass)
        
Window = Tk()
Window.title("  ---    PASS FORGE (One Place for Generating Strong Passwords🔐   --- ")

#Data_Context = StringVar()

Window.geometry('610x680+500+90')
Window.iconbitmap('PassIcon.ico')    
Window.config(background='khaki')     
Window.resizable(False,False)

L1 = Label(Window,text="   PASS FORGE   ",font=('Times New Roman',38,'bold'),bg='peru',fg='black',bd=8,highlightbackground='#6B6B6B',highlightthickness=8,relief='raised',cursor='dotbox')

L2 = Label(Window,text=' One Place for Strong Passwords According to  \n your given Passwords Contexts ',font=('L1.place(X=100,Y=10)',18,'bold','italic'),justify='center',bg='khaki3')
#jutsify Attribute of thnter haing three DIff values: left,center,right


L3 = Label(Window,text=' Choose One Platform - for Which Want Password ⬇️',font=('Georgia',15,'bold'),bg='khaki',fg='gray20')

Box = ttk.Combobox(Window,font=('Times New Roman',15,'bold'),values=['     ------  Select a Platform  ------     ','Facebook','Instagram','Snapchat','Twitter (X)','Other(General)'],width=35,justify='center',state='readonly')
Box.current(0)

L4 = Label(Window,text=' Enter the Context You Want to Follow in Password : ', font=('Georgia',15,'bold'),bg='khaki',fg='gray20')
Enter = Entry(Window,font=('Times New Roman',16,'bold'),selectbackground='blue',width=33,bd=3,selectforeground='pink',highlightthickness=3,highlightbackground='grey25')

#Context is the word or phrase that you want to follow in your password. For example, ifvyou want to follow the word "password" in your password, then you can enter "password" as the context. The password generator will then generate a password that contains the word "password"


Sub = Button(Window,text=' Next ▶️',bg='#5E2612',font=('DejaVu Sans',20,'bold'),fg='#F4F4F4',bd=8,highlightbackground='seashell4',highlightthickness=8,relief='ridge',activebackground='blue',activeforeground='white',command=Submit,cursor='hand2')

L1.place(x=90,y=10)

L2.place(relx=0.035,rely=0.2)
L3.place(relx=0.04,rely=0.42)
Box.place(relx=0.2,rely=0.48)
L4.place(relx=0.04,rely=0.6)
Enter.place(relx=0.2,rely=0.65)
Sub.place(relx=0.37,rely=0.8)

Window.bind("<Return>",lambda event=None: Submit())          #Aslo All Details Submitted Even Even You Just preee Enter 


Window.mainloop()