from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import customtkinter
import mysql.connector
import ttkthemes


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


window=Tk()
window.title("TUK LOG IN PAGE")
window.resizable(FALSE,FALSE)
window.geometry('800x600')

def open():
    
    global img
    if e_user.get() == "admin" and e_password.get() == "12345":
        window.withdraw()
        top=Toplevel()
        top.title("my second window")
        top.geometry("1000x800")
       


        def wexit():
            results=messagebox.askyesno('confirmation','Do you want to exit?')
            if results:
                top.destroy()
            else:
                pass

        def updatestudent():
            uwindow=Toplevel()
            uwindow.title("Update student")
            uwindow.grab_set()
            
            def update():
                query= 'Update class set Name=%s,contact=%s,Gender=%s,Date_of_Birth=%s,Status=%s where Admission_number=%s'
                mycursor.execute(query,(entryname.get(),entrycontact.get(),entrygender.get(),entrybirthday.get(),entrystatus.get(),entryadm.get()))
                db.commit()
                messagebox.showinfo('success','update successfull',parent=uwindow)
                uwindow.destroy()
                showall()

            labl1=Label (uwindow,text="Addmision number",font=("Times New Roman",16,"bold"))
            labl1.grid(row=0,column=0,pady=20,padx=30,sticky=W)
            labl2=Label(uwindow,text="Name",font=("Times New Roman",16,"bold"))
            labl2.grid(row=1,column=0,pady=20,padx=30,sticky=W)
            labl3=Label(uwindow,text="Contact",font=("Times New Roman",16,"bold"))
            labl3.grid(row=2,column=0,pady=20,padx=30,sticky=W)
            labl4=Label(uwindow,text="Gender",font=("Times New Roman",16,"bold"))
            labl4.grid(row=3,column=0,pady=20,padx=30,sticky=W)
            labl5=Label(uwindow,text="Date of birth",font=("Times New Roman",16,"bold"))
            labl5.grid(row=4,column=0,pady=20,padx=30,sticky=W)
            labl6=Label(uwindow,text="Status",font=("Times New Roman",16,"bold"))
            labl6.grid(row=5,column=0,pady=20,padx=30,sticky=W)

            entryadm=Entry(uwindow,width=20,font=("Times New Roman",16))
            entryadm.grid(row=0,column=1,pady=20,padx=30)
            entryname=Entry(uwindow,width=20,font=("Times New Roman",16))
            entryname.grid(row=1,column=1,pady=20,padx=30)
            entrycontact=Entry(uwindow,width=20,font=("Times New Roman",16))
            entrycontact.grid(row=2,column=1,pady=20,padx=30)
            entrygender=Entry(uwindow,width=20,font=("Times New Roman",16))
            entrygender.grid(row=3,column=1,pady=20,padx=30)
            entrybirthday=Entry(uwindow,width=20,font=("Times New Roman",16))
            entrybirthday.grid(row=4,column=1,pady=20,padx=30)
            entrystatus=Entry(uwindow,width=20,font=("Times New Roman",16))
            entrystatus.grid(row=5,column=1,pady=20,padx=30)

            updatebtn=Button(uwindow,text="UPDATE",font=("Helvetica",15),bg="#7F7FFF",fg="White",bd=4,command=update)
            updatebtn.grid(row=6,columnspan=2,pady=15)

            index=studenttable.focus()
            content=studenttable.item(index)
            listdata=content['values']
            entryadm.insert(0,listdata[0])
            entryname.insert(0,listdata[1])
            entrycontact.insert(0,listdata[2])
            entrygender.insert(0,listdata[3])
            entrybirthday.insert(0,listdata[4])
            entrystatus.insert(0,listdata[5])



        def deletestudent():

            index=studenttable.focus()
            content=studenttable.item(index)
            content_id=content['values'][0]
            q3='delete from class where Admission_number=%s'
            mycursor.execute(q3,(content_id,))
            db.commit()
            messagebox.showinfo('success',f'student id {content_id} has been deleted from database')
            fetched=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for data in fetched:
                datalist=list(data)
                studenttable.insert('',END,values=datalist)


        def showall():
             q2='SELECT * FROM class'
             mycursor.execute(q2)
             fetched=mycursor.fetchall()
             #statement below is used to prevent duplication of all records when one is added in the tree view
             studenttable.delete(*studenttable.get_children())
             for data in fetched:
                datalist=list(data)
                studenttable.insert('',END,values=datalist)


        def searchstudent():
            
            s_window=Toplevel()
            s_window.resizable(False,False)
            s_window.grab_set()

            def searchdata():
                 q3='select * from class where Admission_number=%s or Name=%s'
                 mycursor.execute(q3,(entryadm1.get(),entryname1.get()))
                 fetched=mycursor.fetchall()
                 studenttable.delete(*studenttable.get_children())
                 for data in fetched:
                   datalist=list(data)
                   studenttable.insert('',END,values=datalist)


            labl1=Label (s_window,text="Enter Addmision number",font=("Times New Roman",16,"bold"))
            labl1.grid(row=0,column=0,pady=20,padx=30,sticky=W)
            labl1=Label (s_window,text="Enter name",font=("Times New Roman",16,"bold"))
            labl1.grid(row=2,column=0,pady=20,padx=30,sticky=W)

            entryadm1=Entry(s_window,width=20,font=("Times New Roman",16))
            entryadm1.grid(row=1,column=0,pady=20,padx=30)
            entryname1=Entry(s_window,width=20,font=("Times New Roman",16))
            entryname1.grid(row=3,column=0,pady=20,padx=30)

            searchbtn=Button(s_window,text="search",font=("Helvetica",15),bg="#7F7FFF",fg="White",bd=4,command=searchdata)
            searchbtn.grid(row=4,column=0,pady=15,sticky=NSEW)
            

        def add():
            add_window=Toplevel()
            add_window.resizable(False,False)
            add_window.grab_set()
            def addstudent():
                if entryadm.get() =='' or entryname.get() == '' or entrygender.get() == '' or entrycontact.get() == '' or entrybirthday.get() == '' or entrystatus.get() == '':
                    messagebox.showwarning('warning','All fields require entry',parent=add_window)
                else:
                    query= 'INSERT INTO class VALUES(%s,%s,%s,%s,%s,%s)'
                    mycursor.execute(query,(entryadm.get(),entryname.get(),entrycontact.get(),entrygender.get(),
                                            entrybirthday.get(),entrystatus.get()))
                    db.commit()
                    results=messagebox.askquestion('Adding student succesfull','Action succesfull. clear the form?',parent=add_window)
                    if results:
                        entryadm.delete(0,END)
                        entryname.delete(0,END)
                        entrycontact.delete(0,END)
                        entrygender.delete(0,END)
                        entrybirthday.delete(0,END)
                        entrystatus.delete(0,END)
                    else:
                        pass
                    q2='SELECT * FROM class'
                    mycursor.execute(q2)
                    fetched=mycursor.fetchall()
                    #statement below is used to prevent duplication of all records when one is added in the tree view
                    studenttable.delete(*studenttable.get_children())
                    for data in fetched:
                        datalist=list(data)
                        studenttable.insert('',END,values=datalist)

            labl1=Label (add_window,text="Addmision number",font=("Times New Roman",16,"bold"))
            labl1.grid(row=0,column=0,pady=20,padx=30,sticky=W)
            labl2=Label(add_window,text="Name",font=("Times New Roman",16,"bold"))
            labl2.grid(row=1,column=0,pady=20,padx=30,sticky=W)
            labl3=Label(add_window,text="Contact",font=("Times New Roman",16,"bold"))
            labl3.grid(row=2,column=0,pady=20,padx=30,sticky=W)
            labl4=Label(add_window,text="Gender",font=("Times New Roman",16,"bold"))
            labl4.grid(row=3,column=0,pady=20,padx=30,sticky=W)
            labl5=Label(add_window,text="Date of birth",font=("Times New Roman",16,"bold"))
            labl5.grid(row=4,column=0,pady=20,padx=30,sticky=W)
            labl6=Label(add_window,text="Status",font=("Times New Roman",16,"bold"))
            labl6.grid(row=5,column=0,pady=20,padx=30,sticky=W)

            entryadm=Entry(add_window,width=20,font=("Times New Roman",16))
            entryadm.grid(row=0,column=1,pady=20,padx=30)
            entryname=Entry(add_window,width=20,font=("Times New Roman",16))
            entryname.grid(row=1,column=1,pady=20,padx=30)
            entrycontact=Entry(add_window,width=20,font=("Times New Roman",16))
            entrycontact.grid(row=2,column=1,pady=20,padx=30)
            entrygender=Entry(add_window,width=20,font=("Times New Roman",16))
            entrygender.grid(row=3,column=1,pady=20,padx=30)
            entrybirthday=Entry(add_window,width=20,font=("Times New Roman",16))
            entrybirthday.grid(row=4,column=1,pady=20,padx=30)
            entrystatus=Entry(add_window,width=20,font=("Times New Roman",16))
            entrystatus.grid(row=5,column=1,pady=20,padx=30)

            addbtn=Button(add_window,text="Add",font=("Helvetica",15),bg="#7F7FFF",fg="White",bd=4,command=addstudent)
            addbtn.grid(row=6,columnspan=2,pady=15)

            

        def db_connect():
            dbconnection=Toplevel()
            dbconnection.grab_set()
            dbconnection.title("Database details")
            dbconnection.geometry("470x260+730+230")
            dbconnection.resizable(0,0)
            

            def connect():
                global mycursor
                global db
                try:
                  db=mysql.connector.connect(host=entryhost.get(),
                                             user=entryusername.get(),
                                             passwd=entrypasswd.get(),
                                             database="studentsabmi2020")
                  mycursor=db.cursor()
                  messagebox.showinfo('Database','You are connected to the database',parent=dbconnection)
                except:
                   messagebox.showerror('error','wrong entries',parent=dbconnection)

                butt1.config(state="normal")
                butt2.config(state="normal")
                butt3.config(state="normal")
                butt4.config(state="normal")
                butt5.config(state="normal")

                dbconnection.destroy()


            lbl=Label(dbconnection,text="Enter host",font=("Times New Roman",16,"bold"))
            lbl.grid(row=0,column=0,pady=20,padx=30,sticky=W)
            lbl1=Label(dbconnection,text="Enter user",font=("Times New Roman",16,"bold"))
            lbl1.grid(row=1,column=0,pady=20,padx=30,sticky=W)
            lbl2=Label(dbconnection,text="Enter password",font=("Times New Roman",16,"bold"))
            lbl2.grid(row=2,column=0,pady=20,padx=30,sticky=W)
            entryhost=Entry(dbconnection,width=20,font=("Times New Roman",16))
            entryhost.grid(row=0,column=1,pady=20,padx=30)
            entryusername=Entry(dbconnection,width=20,font=("Times New Roman",16))
            entryusername.grid(row=1,column=1,pady=20,padx=30)
            entrypasswd=Entry(dbconnection,width=20,font=("Times New Roman",16))
            entrypasswd.grid(row=2,column=1,pady=20,padx=30)
            connectbtn=Button(dbconnection,text="Connect",font=("Helvetica",15),bg="#7F7FFF",fg="White",bd=4,command=connect)
            connectbtn.grid(row=3,columnspan=2)


        label1=Label(top,text="Welcome To The Management System",font=("Times New Roman",26),
                     anchor=CENTER,padx=5,pady=5)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW,columnspan=2)

        butt=Button(top,text="Connect To Database",font=("Helvetica",18),anchor=CENTER,
                    width=16,bg="#7F7FFF",fg="White",bd=4,command=db_connect)
        butt.grid(row=0,column=3,padx=5,pady=5,sticky="w")

        leftframe=Frame(top)
        leftframe.grid(row=1,column=0)

        img=ImageTk.PhotoImage(Image.open("C:/Users/user/Pictures/download.jpg"))
        label2=Label(leftframe,image=img)
        label2.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        

        butt1=Button(leftframe,text="Search",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=searchstudent)
        butt1.grid(row=2,column=0,padx=5,pady=5,sticky="w")

        butt2=Button(leftframe,text="Add Student",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=add)
        butt2.grid(row=3,column=0,padx=5,pady=5,sticky="w")

        butt3=Button(leftframe,text="Delete Student",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=deletestudent)
        butt3.grid(row=4,column=0,padx=5,pady=5,sticky="w")

        butt4=Button(leftframe,text="Update Student",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=updatestudent)
        butt4.grid(row=5,column=0,padx=5,pady=5,sticky="w")

        butt5=Button(leftframe,text="Display All",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=showall)
        butt5.grid(row=6,column=0,padx=5,pady=5,sticky="w")

        butt6=Button(leftframe,text="Exit",font=("Helvetica",15),anchor=CENTER,width=18,
                     bg="#7F7FFF",fg="White",bd=4,command=wexit)
        butt6.grid(row=7,column=0,padx=5,pady=5,sticky="w")
        

        rightframe=Frame(top)
        rightframe.place(x=350,y=80,width=600,height=600)

        scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
        scrollbary=Scrollbar(rightframe,orient=VERTICAL)

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)
        
        studenttable=ttk.Treeview(rightframe,columns=('Admission','Name','Contact','Gender','Birthday','Status'),
                                  xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.config(command=studenttable.xview)
        scrollbary.config(command=studenttable.yview)

        studenttable.heading('Admission',text='Admission')
        studenttable.heading('Name',text='Name')
        studenttable.heading('Contact',text='Contact')
        studenttable.heading('Gender',text='Gender')
        studenttable.heading('Birthday',text='Birthdate')
        studenttable.heading('Status',text='Status')

        studenttable.column('Admission',width=90,anchor=CENTER)
        studenttable.column('Name',width=110,anchor=CENTER)
        studenttable.column('Contact',width=110,anchor=CENTER)
        studenttable.column('Gender',width=100,anchor=CENTER)
        studenttable.column('Birthday',width=110,anchor=CENTER)
        studenttable.column('Status',width=110,anchor=CENTER)

        style=ttk.Style()
        style.configure('Treeview',rowheight=30,font=('lucida sans',10,'bold'),foreground="#BE8418",background="#C3DA8C")
        style.configure('Treeview.Heading',font=('lucida sans',12,'bold'),foreground="#BE8418")
    

        studenttable.config(show='headings')

        studenttable.pack(fill=BOTH,expand=1)
   
    else:
        messagebox.showerror("error","credentials do not match try again")

    
    
bimage=Image.open('C:/Users/user/Downloads/proj1.jpg')
resized=bimage.resize((800,600),Image.LANCZOS)
fimage=ImageTk.PhotoImage(resized)


my_canvas=Canvas(window,width=800,height=600)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0, image=fimage,anchor=NW)
my_canvas.create_text(500,280,text="User",font=("Helvetica",20),anchor=W)
my_canvas.create_text(500,355,text="Password",font=("Helvetica",20),anchor=W)
my_canvas.create_text(500,20,text="TUK MANAGEMENT SYSTEM",font=("Times New Roman",30),anchor=CENTER)

button1=Button(window,text="log in",width=10,command=open,font=("Times New Roman",15),anchor=CENTER,bg="#7F7FFF",fg="White",bd=4)
button1_window=my_canvas.create_window(550,450,window=button1,anchor=NW)

e_user=Entry(window,font=("Helvetica",18),width=16)
e_password=Entry(window,font=("Helvetica",18),width=16)
e_password.config(show="*")

user_window=my_canvas.create_window(500,305,window=e_user,anchor="nw")
password_window=my_canvas.create_window(500,375,window=e_password,anchor="nw")

window.mainloop()


