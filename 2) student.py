import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import cv2
import os

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.title("Student Management System")

        # text variables
        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_student_id = tk.StringVar()
        self.var_student_name = tk.StringVar()
        self.var_div = tk.StringVar()
        self.var_roll_number = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_teacher = tk.StringVar()

        # Database connection (MySQL)
        self.connection = mysql.connector.connect(host="your_host", user="your_username", password="your_password", database="your_database_name")
        self.cursor = self.connection.cursor()

        # Create table if not exists
        self.create_table()
        

        # First image
        first_img_width = 400
        first_img_height = 130
        img = Image.open(r"your_image_path1.jpg")
        img = img.resize((first_img_width, first_img_height), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = tk.Label(self.root, image=self.photoimg)
        f_lbl.place(x=10, y=10, width=first_img_width, height=first_img_height)

        # Second image
        second_img_width = 400
        second_img_height = 130
        img1 = Image.open(r"your_image_path2.jpg")
        img1 = img1.resize((second_img_width, second_img_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=10, y=150, width=second_img_width, height=second_img_height)

        # Third image
        third_img_width = 400
        third_img_height = 130
        img2 = Image.open(r"your_image_path3.jpg")
        img2 = img2.resize((third_img_width, third_img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = tk.Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=10, y=290, width=third_img_width, height=third_img_height)

        # Background image
        bg_img_width = 1366
        bg_img_height = 638
        img3 = Image.open("your_image_path4.jpg")
        img3 = img3.resize((bg_img_width, bg_img_height), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = tk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=bg_img_width, height=bg_img_height)

        title_lbl = tk.Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("verdana", 25, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=bg_img_width, height=45)

        main_frame = tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1500, height=600)

        # Left label frame
        left_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE, text="Student Details", font=("verdana", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

        second_img_width = 400
        second_img_height = 130
        img_left = Image.open("your_image_path2.jpg")
        img_left = img_left.resize((second_img_width, second_img_height), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl1 = tk.Label(left_frame, image=self.photoimg_left)
        f_lbl1.place(x=5, y=0, width=second_img_width, height=second_img_height)

        # Current course information
        current_course = tk.LabelFrame(left_frame, bd=2, bg="white", relief=tk.RIDGE, text="Current Course Information", font=("verdana", 12, "bold"))
        current_course.place(x=5, y=135, width=720, height=125)

        # Department
        dep_label = tk.Label(current_course, text="Department", font=("verdana", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=("verdana", 12, "bold"), state="readonly", width=170)
        dep_combo["values"] = ("Select Department", "CSE", "ECE", "SMART MANUFACTURING", "MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=tk.W)

        # Course
        course_label = tk.Label(current_course, text="Course", font=("verdana", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course,textvaribles = self.var_course, font=("verdana", 12, "bold"), state="readonly", width=170)
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "MBA", "BBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=tk.W)

        # Year
        year_label = tk.Label(current_course, text="Year", font=("verdana", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=10)

        year_combo = ttk.Combobox(current_course,textvaribles = self.var_year, font=("verdana", 12, "bold"), state="readonly", width=170)
        year_combo["values"] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=tk.W)

        # Semester
        semester_label = tk.Label(current_course, text="Semester", font=("verdana", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=10)

        semester_combo = ttk.Combobox(current_course,textvaribles = self.var_semester, font=("verdana", 12, "bold"), state="readonly", width=170)
        semester_combo["values"] = ("Select Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=tk.W)
        
        # Class student information
        class_student_frame = tk.LabelFrame(left_frame, bd=2, bg="white", relief=tk.RIDGE, text="Class Student Information", font=("verdana", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # studentId
        studentId_label = tk.Label(class_student_frame,textvaribles = self.var_student_id, text="Student ID", font=("verdana", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        studentId_entry = tk.Entry(class_student_frame, font=("verdana", 12))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Additional student details
        
        # student name
        studentName_label = tk.Label(class_student_frame, text="Student Name", font=("verdana", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        studentName_entry = tk.Entry(class_student_frame,textvaribles = self.var_student_name, font=("verdana", 12))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)
        
        # class division
        ivision_label = tk.Label(class_student_frame, text="Division", font=("verdana", 12, "bold"), bg="white")
        division_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        division_entry = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("verdana", 12, "bold"), state="readonly", width=20)
        division_entry["values"] = ("A", "B", "C")  # Replace with the actual divisions
        division_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        
        # roll number
        rollNumber_label = tk.Label(class_student_frame, text="Roll Number", font=("verdana", 12, "bold"), bg="white")
        rollNumber_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

        rollNumber_entry = tk.Entry(class_student_frame,textvaribles = self.var_roll_number, font=("verdana", 12))
        rollNumber_entry.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

        # gender
        gender_label = tk.Label(class_student_frame, text="Gender", font=("verdana", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        gender_entry = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("verdana", 12, "bold"), state="readonly", width=20)
        gender_entry["values"] = ("Male", "Female", "Other")
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
 
        # date of birth
        dob_label = tk.Label(class_student_frame, text="Date of Birth", font=("verdana", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)

        dob_entry = tk.Entry(class_student_frame,textvaribles = self.var_dob, font=("verdana", 12))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        # phone number
        phone_label = tk.Label(class_student_frame, text="Phone Number", font=("verdana", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        phone_entry = tk.Entry(class_student_frame,textvaribles = self.var_phone, font=("verdana", 12))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        # address
        address_label = tk.Label(class_student_frame, text="Address", font=("verdana", 12, "bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

        address_entry = tk.Entry(class_student_frame,textvaribles = self.var_address, font=("verdana", 12))
        address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)

        # teacher
        teacher_label = tk.Label(class_student_frame, text="Teacher", font=("verdana", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        teacher_entry = tk.Entry(class_student_frame, textvar=self.var_teacher, font=("verdana", 12))
        teacher_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # email
        email_label = tk.Label(class_student_frame, text="Email", font=("verdana", 12, "bold"), bg="white")
        email_label.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)

        email_entry = tk.Entry(class_student_frame, textvar=self.var_email, font=("verdana", 12))
        email_entry.grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)

        
        # radio button
        self.var_radio1 = tk.StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, textvariable=self.var_radio1, text="take photo sample", value="yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, textvariable=self.var_radio1, text="no photo sample", value="no")
        radiobtn2.grid(row=6, column=1)
        
        # Buttons frame
        btn_frame = tk.Frame(class_student_frame, bd=2, relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=230, width=715, height=60)
        
        
        save_btn = tk.Button(btn_frame, text="Save", width=17, font=("verdana", 12, "bold"), bg="blue", fg="white", command=self.add_data)
        save_btn.grid(row=0, column=0)

        update_btn = tk.Button(btn_frame, text="Update", width=17, font=("verdana", 12, "bold"), bg="green", fg="white", command=self.update_student)
        update_btn.grid(row=0, column=1, padx=10, pady=5)

        delete_btn = tk.Button(btn_frame, text="Delete", width=17, font=("verdana", 12, "bold"), bg="red", fg="white", command=self.delete_student)
        delete_btn.grid(row=0, column=2, padx=10, pady=5)

        reset_btn = tk.Button(btn_frame, text="Reset", width=17, font=("verdana", 12, "bold"), bg="purple", fg="white", command=self.reset_student)
        reset_btn.grid(row=0, column=3, padx=10, pady=5)

        take_photo_btn = tk.Button(btn_frame, text="Take Photo Sample", width=25, font=("verdana", 12, "bold"), bg="red", fg="white", command=self.take_photo_sample)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = tk.Button(btn_frame, text="Update Photo", width=25, font=("verdana", 12, "bold"), bg="orange", fg="white", command=self.update_photo)
        update_photo_btn.grid(row=1, column=1, padx=10, pady=5)


        
        # Right label frame
        right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE, text="Student Details", font=("verdana", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=580)

        new_img_width = 400
        new_img_height = 130
        img_right = Image.open("your_new_image_path.jpg")
        img_right = img_right.resize((new_img_width, new_img_height), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl1 = tk.Label(right_frame, image=self.photoimg_right)
        f_lbl1.place(x=5, y=0, width=new_img_width, height=new_img_height)

        # Search frame
        search_frame = tk.LabelFrame(right_frame, bd=2, bg="white", relief=tk.RIDGE, text="Search System", font=("verdana", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        # Search student ID entry
        search_label = tk.Label(search_frame, text="Search By:", font=("verdana", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        search_combo = ttk.Combobox(search_frame, font=("verdana", 12, "bold"), state="readonly", width=20)
        search_combo["values"] = ("Student ID", "Student Name", "Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=tk.W)

        search_entry = tk.Entry(search_frame, font=("verdana", 12))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        search_btn = tk.Button(search_frame, text="Search", font=("verdana", 12, "bold"), bg="blue", fg="white", command=self.search_student)
        search_btn.grid(row=0, column=3, padx=10, pady=5)

        # Table frame
        table_frame = tk.Frame(right_frame, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=5, y=220, width=710, height=340)


        # Treeview widget for displaying student details
        self.student_table = ttk.Treeview(table_frame, column=("Student ID", "Student Name", "Roll Number", "Phone Number", "Gender", "Date of Birth", "Address", "Teacher"))
        self.student_table.heading("Student ID", text="Student ID")
        # ... (Add heading and column definitions for other columns)
        self.student_table.column("Teacher", width=120)
        self.student_table.pack(fill=tk.BOTH, expand=1)
        
        # Database connection (MySQL)
        self.connection = mysql.connector.connect(host="your_host", user="your_username", password="your_password", database="your_database_name")
        self.cursor = self.connection.cursor()

        # Create table if not exists
        self.create_table()

        # Other code remains the same
        
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY,student_name VARCHAR(255),roll_number VARCHAR(50),phone_number VARCHAR(20),gender VARCHAR(10),date_of_birth VARCHAR(20),address VARCHAR(255),teacher VARCHAR(100),email VARCHAR(100),year VARCHAR(20),photo_path VARCHAR(255))''')
        self.connection.commit()

        # Treeview widget for displaying student details
        self.student_table = ttk.Treeview(self.table_frame, column=("Student ID", "Student Name", "Roll Number", "Phone Number", "Gender", "Date of Birth", "Address", "Teacher"))
        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Student Name", text="Student Name")
        self.student_table.heading("Roll Number", text="Roll Number")
        self.student_table.heading("Phone Number", text="Phone Number")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Date of Birth", text="Date of Birth")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table["show"] = "headings"
        self.student_table.column("Student ID", width=100)
        self.student_table.column("Student Name", width=150)
        self.student_table.column("Roll Number", width=100)
        self.student_table.column("Phone Number", width=120)
        self.student_table.column("Gender", width=80)
        self.student_table.column("Date of Birth", width=100)
        self.student_table.column("Address", width=200)
        self.student_table.column("Teacher", width=120)
        self.student_table.pack(fill=tk.BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def search_student(self):
        # Get the selected option and entry value
        search_option = self.search_combo.get()
        search_value = self.search_entry.get()

        # Implement the logic to search for a student based on the selected option and the entry value.
        # You can use the search_option and search_value to query the database and populate the table accordingly.
        # For demonstration purposes, we will show sample data.

        self.student_table.delete(*self.student_table.get_children())  # Clear the existing data from the table

        try:
            # Connect to the database
            connection = mysql.connector.connect(host="your_host", user="your_username", password="your_password", database="your_database_name")
            cursor = connection.cursor()

            # Execute the search query
            cursor.execute(f"SELECT * FROM students WHERE {search_option.lower()}=%s", (search_value,))
            data = cursor.fetchall()

            if data:
                for row in data:
                    self.student_table.insert("", tk.END, values=row)

            # Close the database connection
            connection.close()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}", parent=self.root)
            
            
    def show_all_students(self):
        # Fetch and display all students in the right frame

        self.student_table.delete(*self.student_table.get_children())  # Clear the existing data from the table

        try:
            # Connect to the database
            connection = mysql.connector.connect(host="your_host", user="your_username", password="your_password", database="your_database_name")
            cursor = connection.cursor()

            # Execute the query to fetch all students
            cursor.execute("SELECT * FROM students")
            data = cursor.fetchall()

            if data:
                for row in data:
                    self.student_table.insert("", tk.END, values=row)

            # Close the database connection
            connection.close()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}", parent=self.root)
            
            
    
    # function declaration 
           
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_student_name.get() == "" or self.var_student_id.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="your_database_name")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO students (year, semester, student_id, student_name, div, roll_number, gender, dob, email, phone, address, teacher) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                         self.var_year.get(),
                         self.var_semester.get(),
                         self.var_student_id.get(),
                         self.var_student_name.get(),
                         self.var_div.get(),
                         self.var_roll_number.get(),
                         self.var_gender.get(),
                         self.var_dob.get(),
                         self.var_email.get(),
                         self.var_phone.get(),
                         self.var_address.get(),
                         self.var_teacher.get()
                    ) 
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
                
    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            data = self.cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", tk.END, values=i)
                self.connection.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {str(e)}", parent=self.root)
            
    def get_cursor(self, event):
        # Get the selected item from the student_table Treeview widget
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

    # Update the text variables with the selected data
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_student_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll_number.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.usertype.set(data[14])

# If you have more columns in the student_table, update the code accordingly.

                    
    def take_photo_sample(self):
        camera = cv2.VideoCapture(0)  # Initialize the camera (0 indicates the default camera)

        while True:
            ret, frame = camera.read()  # Read a frame from the camera

            # Convert the frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame using the loaded Haar Cascade classifier
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Show the frame with face rectangles
            cv2.imshow("Take Photo Sample", frame)

            # Press 's' to save a photo sample and 'q' to quit
            key = cv2.waitKey(1)
            if key == ord('s'):
                # Save the taken photo sample to a file or database
                cv2.imwrite("sample.jpg", frame)
                break

        camera.release()
        cv2.destroyAllWindows()

        # Display the taken photo sample in the tkinter application
        self.var_photo.set("sample.jpg")  # Set the photo path in the text variable
        self.show_photo_sample()  # Display the photo in the canvas

    
    def update_photo(self):
        # Get the student ID from the entry widget
        student_id = self.var_student_id.get()

        # Update the student's photo path in the database
        self.cursor.execute("UPDATE students SET photo_path=? WHERE student_id=?", ("new_photo.jpg", student_id))
        self.connection.commit()

        messagebox.showinfo("Success", "Student photo updated successfully!")

    def save_student(self):
        # Get the student information from the entry widgets
        student_name = studentName_entry.get()
        roll_number = rollNumber_entry.get()
        phone_number = phone_entry.get()
        gender = gender_entry.get()
        date_of_birth = dob_entry.get()
        address = address_entry.get()
        teacher = teacher_entry.get()

        # Insert the student information into the database
        self.cursor.execute("""INSERT INTO students (student_name, roll_number, phone_number, gender, date_of_birth, address, teacher, photo_path)VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (student_name, roll_number, phone_number, gender, date_of_birth, address, teacher, "sample.jpg"))
        self.connection.commit()

        messagebox.showinfo("Success", "Student information saved successfully!")

    def update_student(self):
        # Get the updated student information from the entry widgets
        student_id = self.var_student_id.get()
        student_name = self.var_student_name.get()
        roll_number = self.var_roll_number.get()
        phone_number = self.var_phone.get()
        gender = self.var_gender.get()
        date_of_birth = self.var_dob.get()
        address = self.var_address.get()
        teacher = self.var_teacher.get()

        # Check if all required fields are filled
        if student_name == "" or roll_number == "" or phone_number == "":
            messagebox.showerror("Error", "Student Name, Roll Number, and Phone Number are required fields.")
            return

        try:
            # Connect to the database
            connection = mysql.connector.connect(host="your_host", user="your_username", password="your_password", database="your_database_name")
            cursor = connection.cursor()

            # Update the student information in the database
            cursor.execute("""UPDATE students SET student_name=%s, roll_number=%s, phone_number=%s, gender=%s, date_of_birth=%s, address=%s, teacher=%s WHERE student_id=%s""",
                           (student_name, roll_number, phone_number, gender, date_of_birth, address, teacher, student_id))
            
            # Commit the changes
            connection.commit()

            # Close the database connection
            connection.close()

            # Show success message
            messagebox.showinfo("Success", "Student information updated successfully!")

            # Clear the entry fields
            self.reset_student()

            # Refresh the table to show the updated data
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update student information: {str(e)}")
            
            
    def show_photo_sample(self):
        photo_path = self.var_photo.get()
        if photo_path:
            try:
                image = Image.open(photo_path)
                image = image.resize((250, 300), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)

                self.lbl_sample_photo.config(image=photo)
                self.lbl_sample_photo.image = photo

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load photo sample: {str(e)}", parent=self.root)
        else:
            messagebox.showwarning("Warning", "No photo sample found.", parent=self.root)
            
        
    def detect_face(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        camera = cv2.VideoCapture(0)  # Initialize the camera (0 indicates the default camera)

        while True:
            ret, frame = camera.read()  # Read a frame from the camera

            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the frame with detected faces
            cv2.imshow('Face Detection', frame)

            # Press 'q' to quit
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()
        
    def generate_dataset(output_dir, num_samples=10):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        camera = cv2.VideoCapture(0)  # Initialize the camera (0 indicates the default camera)
        sample_count = 0

        while True:
            ret, frame = camera.read()  # Read a frame from the camera

        # Convert the frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame using the loaded Haar Cascade classifier
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Save the captured face region (ROI) as an image file
                sample_count += 1
                face_path = os.path.join(output_dir, f"sample_{sample_count}.jpg")
                cv2.imwrite(face_path, gray_frame[y:y+h, x:x+w])

            # Display the sample count on the frame
                cv2.putText(frame, f"Sample {sample_count}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # Display the frame with detected faces
            cv2.imshow('Generate Dataset', frame)

        # Break the loop if the specified number of samples is captured
            if sample_count >= num_samples:
                break

        # Press 'q' to quit
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

class Student:
    def __init__(self, root):
        self.root = root
        self.current_attendance_name = None

    def on_face_recognized(self, predicted_name):
        if predicted_name:
            self.current_attendance_name = predicted_name
            self.mark_attendance()

    def collect_data(self):
        # Similar code for data collection from the student.py class in your original code
        pass
    
    def mark_attendance(self):
        # Similar code for marking attendance from the student.py class in your original code
        pass
    
    def on_mark_attendance(self, callback):
        self.mark_attendance_callback = callback
        
    def delete_student(self):
        # Get the student ID from the entry widget
        student_id = studentId_entry.get()

        # Delete the student information from the database
        self.cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
        self.connection.commit()

        messagebox.showinfo("Success", "Student information deleted successfully!")
        
    def __del__(self):
        # Destructor to close the database connection when the object is deleted
        if self.connection:
            self.connection.close()
        

        

if __name__ == "__main__":
    root = tk.Tk()
    obj = StudentManagementSystem(root)
    root.mainloop()

# Replace "your_image_path1.jpg" with the actual path to your first image.
# Replace "your_image_path2.jpg" with the actual path to your second image.
# Replace "your_image_path3.jpg" with the actual path to your third image.
# Replace "your_image_path4.jpg" with the actual path to your background image.
# Replace "your_new_image_path.jpg" with the actual path to your new image.