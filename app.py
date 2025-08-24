import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import os

# Load the model
model_file = 'student_score_model.pkl'
if not os.path.exists(model_file):
    raise FileNotFoundError("Model file not found. Make sure 'student_score_model.pkl' is in the same directory.")

model = joblib.load(model_file)

def predict_score():
    try:
        # Get user input
        study = float(entry_study.get())
        attendance = float(entry_attendance.get())
        sleep = float(entry_sleep.get())
        previous = float(entry_previous.get())
        tutoring = float(entry_tutoring.get())
        activity = float(entry_activity.get())

        # Prepare input for prediction
        input_data = np.array([[study, attendance, sleep, previous, tutoring, activity]])
        prediction = model.predict(input_data)[0]

        # Show result in large font
        result_label.config(text=f"📊 Predicted Exam Score: {prediction:.2f}", font=('Helvetica', 22, 'bold'), fg="#ff9900")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Create window
root = tk.Tk()
root.title("🎓 Student Exam Score Predictor")
root.geometry("500x500")
root.configure(bg='#fff2e6')

# Header
header = tk.Label(root, text="Exam Score Predictor", bg='#ffa500', fg='white',
                  font=('Helvetica', 18, 'bold'), pady=10)
header.pack(fill='x')

# Form Frame
form_frame = tk.Frame(root, bg='#fff2e6', pady=20)
form_frame.pack(pady=10)

labels = ["Hours Studied", "Attendance", "Sleep Hours", "Previous Scores", "Tutoring Sessions", "Physical Activity"]
entries = []

for i, label_text in enumerate(labels):
    lbl = tk.Label(form_frame, text=label_text + ":", font=('Arial', 12), bg='#fff2e6', anchor='w')
    lbl.grid(row=i, column=0, padx=10, pady=8, sticky='w')
    entry = tk.Entry(form_frame, font=('Arial', 12), width=25)
    entry.grid(row=i, column=1, padx=10, pady=8)
    entries.append(entry)

entry_study, entry_attendance, entry_sleep, entry_previous, entry_tutoring, entry_activity = entries

# Predict Button
btn_predict = tk.Button(root, text="Predict Score", font=('Arial', 14, 'bold'),
                        bg='#ff9900', fg='white', padx=20, pady=10, command=predict_score)
btn_predict.pack(pady=20)

# Result Display (For predicted score)
result_label = tk.Label(root, text="Predicted Exam Score: ", bg='#fff2e6', font=('Helvetica', 18, 'bold'), fg="#ff9900")
result_label.pack(pady=20)

# Footer
footer = tk.Label(root, text="Designed with ❤ using ML", bg='#fff2e6', fg='gray', font=('Arial', 10))
footer.pack(side='bottom', pady=10)

# Run the GUI
root.mainloop()