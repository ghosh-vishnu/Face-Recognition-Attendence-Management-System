from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

# "dep","course","sem","id","name","div","roll","gender","dob","email","phone","address","photo","teacher","year"
        # ************* variable************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.va_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       
        #self.var_photo=StringVar()

        # First image
        img=Image.open(r"Face Recognition Attendence system(FRAS)\student image\left.jpeg")
        img=img.resize((600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=600,height=130)

        # Second image
        img1=Image.open(r"Face Recognition Attendence system(FRAS)\student image\center.jpeg")
        img1=img1.resize((600,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=550,y=0,width=600,height=130)

        # Third image
        img2=Image.open(r"Face Recognition Attendence system(FRAS)\student image\Right.jpeg")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1100,y=0,width=600,height=130)

         # backgraun img
        img3=Image.open(r"Face Recognition Attendence system(FRAS)\face photo\Right logo.jpeg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

# ************ bg image ******
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark red")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"Face Recognition Attendence system(FRAS)\student image\center.jpeg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

         # current course frame
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)

        # department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=9,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department",'IT','CSE','CIVIL','MECHNICAL')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=9)

        # course
        cor_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        cor_label.grid(row=0,column=2,padx=10,sticky=W)

        cor_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        cor_combo["values"]=("Select Course",'BCA','CIVIL','COMPUTER SCIENCE','MECHNICAL')
        cor_combo.current(0)
        cor_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2019-2020","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Course",'Semester-1','Semester-2','Semester-3','Semester-4')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class student information frame
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)
         
        # student id
        studentid_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         # student Name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        studentdiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        studentdiv_label.grid(row=1,column=0,padx=10,sticky=W)

        Div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        Div_combo["values"]=("A","B","C")
        Div_combo.current(0)
        Div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # student Roll
        studentroll_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        studentroll_label.grid(row=1,column=2,padx=10,sticky=W)

        studentroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gen_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gen_label.grid(row=2,column=0,padx=10,sticky=W)

        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gen_combo["values"]=("Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email id
        email_label=Label(class_student_frame,text="Email ID:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone number 
        phone_label=Label(class_student_frame,text="Mobile No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # adress
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",14,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # teacher Name
        teachername_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teachername_label.grid(row=4,column=2,padx=10,sticky=W)

        teachername_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teachername_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # Button frames
        
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # Button frames
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.genrate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        # Right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"Face Recognition Attendence system(FRAS)\face photo\Student Details.jpeg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        # ******************** Search system******************
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)
         
        search_label=Label(search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select",'Roll No','Mobile No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search1_btn=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search1_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        # ***************table frame****************
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        # scrool bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X,)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        # self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email Id")
        self.student_table.heading("phone",text="Mobile No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample")
       
       
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        # self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # **********************Function decration*****************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into attend values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                # self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                #self.var_photo.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                    
                                                                                                             
                                                                                                         ))            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


            # ****************Fetch data******************28
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face")
         my_cursor=conn.cursor()
         my_cursor.execute("Select * from attend")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(* self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()
#***************************** Get Function ***************************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data1=content["values"] 

        self.var_dep.set(data1[0]),  
        self.var_course.set(data1[1]),
        self.var_year.set(data1[2]),
        self.var_sem.set(data1[3]),
        self.va_std_id.set(data1[4]),
        self.var_name.set(data1[5]),
        # self.var_div.set(data1[6]),
        self.var_roll.set(data1[7]),
        self.var_gender.set(data1[8]),
        self.var_dob.set(data1[9]),
        self.var_email.set(data1[10]),
        self.var_phone.set(data1[11]),
        self.var_address.set(data1[12]),
        self.var_teacher.set(data1[13]),
        self.var_radio1.set(data1[14])
    # ************* update function *****************
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Due you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update attend set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where id=%s",(

                                                                                                                                                                      self.var_dep.get(),
                                                                                                                                                                      self.var_course.get(),
                                                                                                                                                                      self.var_year.get(),
                                                                                                                                                                      self.var_sem.get(),
                                                                                                                                                                      self.var_name.get(),
                                                                                                                                                                    #   self.var_div.get(),
                                                                                                                                                                      self.var_roll.get(),
                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                      self.var_dob.get(),
                                                                                                                                                                      self.var_email.get(),
                                                                                                                                                                      self.var_phone.get(),
                                                                                                                                                                      self.var_address.get(),
                                                                                                                                                                    #   self.var_photo.get(),
                                                                                                                                                                      self.var_teacher.get(),
                                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                                      self.va_std_id.get()
                                                                                                                    
                                                                                                                                                                     ))     
                else:
                    if not update:
                        return           
                messagebox.showinfo("success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

    #************************** Delete Function***************************
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page:"," Do you want to this student",parent=self.root)
                if delete>0: 
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face")
                    my_cursor=conn.cursor()
                    sql="delete from attend where id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete :
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

# ************************Reset function*******************
    def reset_data(self):
        self.var_dep.set("Select Department"),  
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set(" Select Semester"),
        self.va_std_id.set(""),
        self.var_name.set(""),
        # self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

# ****************** genrate data set or photo samples*******************
    def genrate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
         else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from attend")
               my_result=my_cursor.fetchall()
               id=0
               for x in my_result:
                   id+=1
               my_cursor.execute("update attend set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where id=%s",(

                                                                                                                                                                      self.var_dep.get(),
                                                                                                                                                                      self.var_course.get(),
                                                                                                                                                                      self.var_year.get(),
                                                                                                                                                                      self.var_sem.get(),
                                                                                                                                                                      self.var_name.get(),
                                                                                                                                                                    #   self.var_div.get(),
                                                                                                                                                                      self.var_roll.get(),
                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                      self.var_dob.get(),
                                                                                                                                                                      self.var_email.get(),
                                                                                                                                                                      self.var_phone.get(),
                                                                                                                                                                      self.var_address.get(),
                                                                                                                                                                      #self.var_photo.get(),
                                                                                                                                                                      self.var_teacher.get(),
                                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                                      self.va_std_id.get()==id+1
                                                                                                                    
                                                                                                                                                                      )) 
               conn.commit()
               self.fetch_data()
               self.reset_data()
               conn.close()
               #***************** load predefined data on face frontal from open cv2*************
               face_classifier=cv2.CascadeClassifier (r"Face Recognition Attendence system(FRAS)\haarcascade_frontalface_default.xml")

               def face_cropped(img):
                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                 faces=face_classifier.detectMultiScale(gray,1.3,5)
                 # scaling factor=1.3
                 # minimum neighbor=5
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
                       file_name_path="Photo_Data/user."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Face",face)

                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating data sets compled!!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

  
                      
                


    

if __name__== '__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop() 
    # update error in work