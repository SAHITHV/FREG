import tkinter as tk
from tkinter import messagebox, simpledialog
from train import Train
from face_recognition import FaceRecognitionApp
from student import Student
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")  # Adjusted dimensions for your screen resolution
        self.root.title("Face Recognition System")

        # First image
        first_img_width = 400
        first_img_height = 130
        img = Image.open(r"your_image_path1.jpg")
        img = img.resize((first_img_width, first_img_height), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=10, y=10, width=first_img_width, height=first_img_height)

        # Second image
        second_img_width = 400
        second_img_height = 130
        img1 = Image.open(r"your_image_path2.jpg")
        img1 = img1.resize((second_img_width, second_img_height), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=10, y=150, width=second_img_width, height=second_img_height)

        # Third image
        third_img_width = 400
        third_img_height = 130
        img2 = Image.open(r"your_image_path3.jpg")
        img2 = img2.resize((third_img_width, third_img_height), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=10, y=290, width=third_img_width, height=third_img_height)
        
        # Background image
        bg_img_width = 1366
        bg_img_height = 638
        img3 = Image.open(r"your_image_path4.jpg")
        img3 = img3.resize((bg_img_width, bg_img_height), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=bg_img_width, height=bg_img_height)
        
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("verdana", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=bg_img_width, height=45)
        
        # Student button
        student_button_width = 220
        student_button_height = 220
        img4 = Image.open(r"your_image_path5.jpg")
        img4 = img4.resize((student_button_width, student_button_height), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=student_button_width, height=student_button_height)
        
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b1_1.place(x=200, y=330, width=student_button_width, height=30)
        
        # Face detector button
        face_detector_button_width = 220
        face_detector_button_height = 220
        img5 = Image.open(r"your_image_path6.jpg")
        img5 = img5.resize((face_detector_button_width, face_detector_button_height), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=face_detector_button_width, height=face_detector_button_height)
        
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b2_1.place(x=500, y=330, width=face_detector_button_width, height=30)
        
        # Attendance face button
        attendance_button_width = 220
        attendance_button_height = 220
        img6 = Image.open(r"your_image_path7.jpg")
        img6 = img6.resize((attendance_button_width, attendance_button_height), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=attendance_button_width, height=attendance_button_height)
        
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b3_1.place(x=800, y=330, width=attendance_button_width, height=30)
        
        # Help desk button
        help_desk_button_width = 220
        help_desk_button_height = 220
        img7 = Image.open(r"your_image_path8.jpg")
        img7 = img7.resize((help_desk_button_width, help_desk_button_height), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=help_desk_button_width, height=help_desk_button_height)
        
        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b4_1.place(x=1100, y=330, width=help_desk_button_width, height=30)
        
        # Train button
        train_button_width = 220
        train_button_height = 220
        img8 = Image.open(r"your_image_path9.jpg")
        img8 = img8.resize((train_button_width, train_button_height), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=450, width=train_button_width, height=train_button_height)
        
        b5_1 = Button(bg_img, text="Train data", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b5_1.place(x=200, y=680, width=train_button_width, height=30)
        
        # Photos button
        photos_button_width = 220
        photos_button_height = 220
        img9 = Image.open(r"your_image_path10.jpg")
        img9 = img9.resize((photos_button_width, photos_button_height), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=450, width=photos_button_width, height=photos_button_height)
        
        b6_1 = Button(bg_img, text="Photos", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b6_1.place(x=500, y=680, width=photos_button_width, height=30)
        
        # Developer button
        developer_button_width = 220
        developer_button_height = 220
        img10 = Image.open(r"your_image_path11.jpg")
        img10 = img10.resize((developer_button_width, developer_button_height), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=450, width=developer_button_width, height=developer_button_height)
        
        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b7_1.place(x=800, y=680, width=developer_button_width, height=30)
        
        # Exit button
        exit_button_width = 220
        exit_button_height = 220
        img11 = Image.open(r"your_image_path12.jpg")
        img11 = img11.resize((exit_button_width, exit_button_height), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=450, width=exit_button_width, height=exit_button_height)
        
        b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=("verdana", 10, "bold"), bg="dark blue", fg="white")
        b8_1.place(x=1100, y=680, width=exit_button_width, height=30)
        
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Face Recognition Attendance System")

        self.train = Train()
        self.attendance = Attendance()
        self.face_app = FaceRecognitionApp(self.root)
        self.student = Student(self.root)

        # Attach the callbacks for student face recognition and attendance
        self.face_app.on_face_recognized(self.student.on_face_recognized)
        self.student.on_mark_attendance(self.on_mark_attendance)

        # Set up buttons and GUI elements for the main app
        self.btn_train_classifier = tk.Button(self.root, text="Train Classifier", command=self.train_classifier)
        self.btn_train_classifier.pack(pady=10)

        self.btn_collect_data = tk.Button(self.root, text="Collect Data", command=self.collect_data)
        self.btn_collect_data.pack(pady=10)

        self.btn_view_attendance = tk.Button(self.root, text="View Attendance", command=self.view_attendance)
        self.btn_view_attendance.pack(pady=10)
               
    def student_details(self) :
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_classifier(self):
        self.train.train_classifier()

    def collect_data(self):
        self.student.collect_data()

    def view_attendance(self):
        self.attendance_data = self.attendance.fetch_attendance_data()
        if self.attendance_data:
            for row in self.attendance_data:
                print(row)
        else:
            print("Attendance data not found.")

    def on_mark_attendance(self, name):
        self.attendance.update_attendance(name)
        messagebox.showinfo("Attendance Marked", f"Attendance for {name} marked successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()