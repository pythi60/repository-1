#importing tkinter module
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from datetime import date
import csv
#function for message after issuing book and going to exit page
def popup2():
    msg=Message(new,text="Book returned successfully")
    msg.pack()
    new4=Toplevel(app)
    new4.title("EXIT")
    new.geometry("400x250")
    chose_book = Label(new4, text = 'To exit, click here').place(x = 30, y = 150)
    exit_button2 = tk.Button(new4, text="Exit",command=app.destroy).place(x=30,y=200)
#function for collecting account info
def Ssubmit():
    NAME=name_var.get()
    USERNAME=username_var.get()
    PASSWORD=password_var.get()
    f=open('account.csv','a')
    w=csv.writer(f)
    w.writerow([NAME,USERNAME,PASSWORD])
    f.close()
    name_var.set("")
    username_var.set("")
    password_var.set("")
#function for checking account info to log in
def Lsubmit():
   #NAME=nam_var.get()
   USERNAME=usernam_var.get()
   PASSWORD=passwo_var.get()
   f=open('account.csv','r',newline='\r\n')
   r=csv.reader(f)
   for i in r:
       if i[1]==USERNAME:
           if i[2]==PASSWORD:
               books()
               break
           else:
               msg=Message(new2,text="Password wrong")
               msg.pack()
               break
   else:
        msg=Message(new2,text="No such account")
        msg.pack()
   f.close()
#function for collecting chosen book and adding to csv file and checking if the book has already been borrowed
def choose():
    Cbook=chosenbook_var.get()
    fr=open('booksinfo.csv','r',newline='\r\n')
    r=csv.reader(fr)
    for i in r:
        if Cbook==i[0]:
            msg=Message(new,text="This book has already been borrowed")
            msg.pack()
            print("borrowed")
            fr.close()
            break
    else:
     f=open('booksinfo.csv','a')
     w=csv.writer(f)
     w.writerow([Cbook,str(date.today())])
     f.close()
     chosenbook_var.set("")
     msg=Message(new,text="Book issued successfully")
     msg.pack()
    new3=Toplevel(app)
    new3.title("EXIT")
    new.geometry("400x250")
    chosebutton = Label(new3, text = 'To exit, click here').place(x = 30, y = 150)
    exit_button1 = tk.Button(new3, text="Exit",command=app.destroy).place(x=30,y=200)
#function for displaying the read books
def readbooks():
    f=open('booksinfo.csv','r',newline='\r\n')
    r=csv.reader(f)
    for i in r:
        print(i[0])
#function for displaying overdue books
def overdue():
    d=str(date.today())
    print('Current date',d)
    f=open('booksinfo.csv','r',newline='\r\n')
    r=csv.reader(f)
    c=0
    for i in r:
        if i[1][3]<d[3]:
            print('Book:',i[0],' Date of issue:',i[1])
            continue
            c+=1
        elif i[1][5]<d[5]:
            print('Book:',i[0],' Date of issue:',i[1])
            continue
            c+=1
        elif i[1][6]<d[6]:
            print('Book:',i[0],' Date of issue:',i[1])
            continue
            c+=1
        elif i[1][8]<d[8]:
            print('Book:',i[0],' Date of issue:',i[1])
            continue
            c+=1
        elif i[1][9]<d[9]:
            print('Book:',i[0],' Date of issue:',i[1])
            continue
            c+=1
    if c!=0:
        msg=Message(new,text="No overdue books")
        msg.pack()
#MAIN LIBRARY FUNCTION
def books():
    global new
    global chosenbook_var
    f=open('books.txt','a+')
    new=Toplevel(app)
    new.title('books')
    new.geometry("400x250")
    '''listbox = Listbox(new, height = 20, 
                  width = 120, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
    label = Label(new, text = "BOOKS")
    listbox.insert(1, "A. Fiction")
    listbox.pack()'''
    chosenbook_var=tk.StringVar()
    returnbook_var=tk.StringVar()
    read_book = Label(new, text = 'All books read').place(x = 30, y = 500)
    books_read = tk.Button(new,text='Enter',command=readbooks).place(x=140,y=500)
    chose_book = Label(new, text = 'Choose your book').place(x = 30, y = 600)
    over_due=Label(new, text = 'Overdue books').place(x = 30, y = 400)
    books_overdue = tk.Button(new,text='Enter',command=overdue).place(x=140,y=400)
    bookchoose = Entry(new,textvariable=chosenbook_var).place(x = 140,y = 600)
    enter_chosen_book = tk.Button(new, text="Enter",command=choose).place(x=30,y=650)
    returned_book = Label(new, text = 'Return a book').place(x = 30, y = 700)
    bookreturn = Entry(new,textvariable=returnbook_var).place(x = 140,y = 700)
    enter_returned_book = tk.Button(new, text="Enter",command=popup2).place(x=30,y=750)
    print('''A.Fiction
A1. "To Kill a Mockingbird" by Harper Lee
A2. "1984" by George Orwell
A3. "The Great Gatsby" by F. Scott Fitzgerald
A4. "Pride and Prejudice" by Jane Austen
A5. "The Catcher in the Rye" by J.D. Salinger
A6. "The Lord of the Rings" by J.R.R. Tolkien
A7. "Harry Potter and the Sorcerer's Stone" by J.K. Rowling
A8. "The Hobbit" by J.R.R. Tolkien
A9. "The Hunger Games" by Suzanne Collins
A10. "The Da Vinci Code" by Dan Brown

B.Children’s lit
B1. "Charlotte's Web" by E.B. White
B2. "Harry Potter and the Philosopher's Stone" by J.K. Rowling
B3. "Alice's Adventures in Wonderland" by Lewis Carroll
B4. "The Chronicles of Narnia" series by C.S. Lewis
B5. "Where the Wild Things Are" by Maurice Sendak
B6. "Matilda" by Roald Dahl
B7. "The Secret Garden" by Frances Hodgson Burnett
B8. "Winnie-the-Pooh" by A.A. Milne
B9. "The Very Hungry Caterpillar" by Eric Carle
B10. "Charlie and the Chocolate Factory" by Roald Dahl

C.History
C1. "The Pillars of the Earth" by Ken Follett
C2. "All the Light We Cannot See" by Anthony Doerr
C3. "The Book Thief" by Markus Zusak
C4. "Wolf Hall" by Hilary Mantel
C5. "Memoirs of a Geisha" by Arthur Golden
C6. "The Kite Runner" by Khaled Hosseini
C7. "Gone with the Wind" by Margaret Mitchell
C8. "The Nightingale" by Kristin Hannah
C9. "The Help" by Kathryn Stockett
C10. "The Underground Railroad" by Colson Whitehead

D.Graphic novel 
D1. "Watchmen" by Alan Moore and Dave Gibbons
D2. "Maus" by Art Spiegelman
D3. "Persepolis" by Marjane Satrapi
D4. "Sandman" series by Neil Gaiman
D5. "V for Vendetta" by Alan Moore and David Lloyd
D6. "Saga" by Brian K. Vaughan and Fiona Staples
D7. "Blankets" by Craig Thompson
D8. "Batman: The Dark Knight Returns" by Frank Miller
D9. "Fun Home" by Alison Bechdel
D10. "Y: The Last Man" by Brian K. Vaughan and Pia Guerra

E. Autobiography
E1.   “The Diary of a Young Girl” by Anne Frank
E2. “Long Walk to Freedom” by Nelson Mandela
E3. “The Autobiography of Benjamin Franklin” by Benjamin Franklin
E4. “The Autobiography of Malcolm X” by Alex Haley
E5. “I Am Malala” by Christina Lamb and Malala Yousafzai
E6.  “Agatha Christie: An Autobiography” by Agatha Christie
E7.  “Becoming” by Michelle Obama
E8.  “Wings of Fire” by Dr. APJ Abdul Kalam
E9. “Dreams From My Father” by Barack Obama
E10.  “Mein Kampf” by Adolf Hitler

F. Biography   
 
F1. “Steve Jobs’’ by Walter Isaacton
F2. “A Beautiful Mind” by Sylvia Nasar
F3. “Frida” by Hayden Herrera 
F4. “Alan Turing: The Enigma’ by Andrew Hodges
F5. “Prairie Fires’ by Caroline Fraser
F6. “Will in the World: How Shakespeare Became Shakespeare” by Stephen Greenblatt
F7. “Alexander Hamilton” by Ron Chernow
F8. “Radioactive: Marie and Pierre Curie: A Tale of Love and Fallout” by Lauren     Redniss             
F9. “Napoleon: A Life” by Andrew Roberts
F10. “Joan of Arc: A History” by Helen Castor

G. Philosophy
G1. “Meditations” by Marcus Aurelius
G2. “Critique of Pure Reason” by Immanuel Kant
G3. “Beyond Good and Evil: Prelude to a Philosophy of the Future’ by Friedrich Nietzsche 
G4. “Meditations of First Philosophy” by Rene Descartes
G5. “Nichomachean Ethics” by Aristotle
G6. “Indian Philosophy’ by Sarvapalli Radhakrishnan
G7. “The Art of War” by Sun tzu
G8. “The Social Contract’ by Jean-Jacques Rosseau 
G9. “Confessions’ by Augustine of Hippo
G10. “Republic” by Plato
H. Horror
H1.“Frankenstein” by Mary Shelley 
H2. “The Narrative of Arthur Gordon Pym of Nantucket” by Edgar Allan Poe
H3. “The Fall of the House of Usher and Other Tales” by Edgar Allan Poe
H4. “Gothic Tales” by Elizabeth Gaskell
H5. “Carmilla” by J. Sheridan Le Fanu
H6. “Dracula” by Bram Stoker
H7. “The Turn of the Screw” by Henry James
H8. “The Exorcist” by William Peter Blatty
H9. “Coraline” by Neil Gaiman
H10. “Heart-Shaped Box” by Joe Hill 
I. Romance 
I1. “Jane Eyre” by Charlotte Brontë
I2. “Anna Karenina” by Leo Tolstoy
I3. “Pride and Prejudice” by Jane Austen
I4. “Emma” by Jane Austen
I5. “Romeo and Juliet” by William Shakespeare
I6. “The Notebook” by Nicholas Sparks
I7. “Indigo” by Beverly Jenkins
I8. “The Hating Game” by Sally Thorne
I9. “Normal People” by Sally Rooney
I10. “Twilight” by Stephenie Meyer
J. Mystery
J1. “And Then There Were None” by Agatha Christie
J2. “The Big Sleep” by Raymond Chandler
J3. “Gone Girl” by Gillian Flynn
J4. “The Postman Always Rings Twice” by James M. Cain
J5. “In Cold Blood” by Truman Capote
J6. “Woman in White” by Wilkie Collins
J7. “Anatomy of a Murder” by Robert Traver
J8. “The Da Vinci Code” by Dan Brown
J9. “The Girl with the Dragon Tattoo” by Stieg Larsson
J10. “The Daughter of Time” by Josephine Tey''')
#function for signing in
def sign_in():
   global name_var
   global username_var
   global password_var
   newWindow = Toplevel(app)
   newWindow.title("sign in")
   newWindow.geometry("400x250")
   name_var=tk.StringVar()
   username_var=tk.StringVar()
   password_var=tk.StringVar()
   name = Label(newWindow, text = "Name").place(x = 30,y = 50)  
   username = Label(newWindow, text = "Username").place(x = 30, y = 90)
   password = Label(newWindow, text = "Password").place(x = 30, y = 130)  
   e1 = tk.Entry(newWindow,textvariable=name_var).place(x = 80, y = 50)  
   e2 = tk.Entry(newWindow,textvariable=username_var).place(x = 95, y = 90)
   e3 = tk.Entry(newWindow,textvariable=password_var).place(x = 95, y = 130)
   enter_button = tk.Button(newWindow, text="Enter", command=books)
   enter_button.pack()
   submit_button = tk.Button(newWindow, text="Submit", command=Ssubmit) 
   submit_button.pack()
   #f.write(e1)
#function for logging in
def log_in():
    #global nam_var
    global usernam_var
    global passwo_var
    global new2
    new2 = Toplevel(app)
    new2.title("log in")
    new2.geometry("400x250")
    #nam_var=tk.StringVar()
    usernam_var=tk.StringVar()
    passwo_var=tk.StringVar()
    #name = Label(new2, text = "Name").place(x = 30,y = 50)  
    username = Label(new2, text = "Username").place(x = 30, y = 90)
    password = Label(new2, text = "Password").place(x = 30, y = 130)  
    #e1 = Entry(new2,textvariable=nam_var).place(x = 80, y = 50)  
    e2 = Entry(new2,textvariable=usernam_var).place(x = 95, y = 90)
    e3 = Entry(new2,textvariable=passwo_var).place(x = 95, y = 130)
    enter_button = tk.Button(new2, text="Enter", command=books)
    enter_button.pack()
    submit_button = tk.Button(new2, text="Submit", command=Lsubmit) 
    submit_button.pack()
#main code
app = tk.Tk()
app.title("LIBRARY")
# creating sign in button
signin = Label(app, text = "Don't have an account? Click here to sign in").place(x = 650, y = 10)
signin_button = tk.Button(app, text="Sign in", command=sign_in).place(x=750,y=30)
#creating log in button
login = Label(app, text = "Already have an account? Click here to log in").place(x = 650, y = 70)
login_button = tk.Button(app, text="Log in", command=log_in).place(x=750,y=90)
