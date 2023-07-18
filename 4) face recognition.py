import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2
import os
import openpyxl
import csv
import numpy as np
from PIL import Image
from train import Train
from attendance import Attendance

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Face Recognition Attendance System")
        self.train = Train()
        self.attendance = Attendance()
        self.create_widgets()

    def create_widgets(self):
        self.btn_collect_data = tk.Button(self.root, text="Collect Data", command=self.collect_data)
        self.btn_collect_data.pack(pady=10)

        self.btn_train_classifier = tk.Button(self.root, text="Train Classifier", command=self.train_classifier)
        self.btn_train_classifier.pack(pady=10)

        self.btn_recognize_face = tk.Button(self.root, text="Recognize Face", command=self.recognize_face)
        self.btn_recognize_face.pack(pady=10)

        self.btn_mark_attendance = tk.Button(self.root, text="Mark Attendance", command=self.mark_attendance, state=tk.DISABLED)
        self.btn_mark_attendance.pack(pady=10)

        self.btn_view_attendance = tk.Button(self.root, text="View Attendance", command=self.view_attendance)
        self.btn_view_attendance.pack(pady=10)

    def collect_data(self):
        # Capture images using OpenCV and save them for training
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        video_capture = cv2.VideoCapture(0)

        person_name = simpledialog.askstring("Input", "Enter your name:")
        if not person_name:
            return

        data_path = os.path.join("data", person_name)
        os.makedirs(data_path, exist_ok=True)

        count = 0
        while count < 20:  # Capture 20 images for training
            ret, frame = video_capture.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                face_region = gray_frame[y:y + h, x:x + w]
                cv2.imwrite(os.path.join(data_path, f"{person_name}_{count}.jpg"), face_region)
                count += 1

            cv2.imshow("Collecting Data", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def train_classifier(self):
        self.train.train_classifier()

    def recognize_face(self):
        # Capture a frame from the camera
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        video_capture.release()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_region = self.train.face_data_function(gray_frame)
        if face_region is not None:
            predicted_label, confidence = self.train.face_recognition_function(face_region)
            if confidence < 100:  # You may need to adjust the threshold based on your training data
                name = self.train.get_name_from_label(predicted_label)
                self.current_attendance_name = name
                messagebox.showinfo("Face Recognized", f"Hello, {name}!")
                self.btn_mark_attendance.config(state=tk.NORMAL)
            else:
                self.current_attendance_name = None
                messagebox.showinfo("Unknown Face", "Sorry, your face is not recognized.")
                self.btn_mark_attendance.config(state=tk.DISABLED)

    def mark_attendance(self):
        if self.current_attendance_name:
            self.attendance.update_attendance(self.current_attendance_name)
            messagebox.showinfo("Attendance Marked", f"Attendance for {self.current_attendance_name} marked successfully.")
            self.btn_mark_attendance.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
