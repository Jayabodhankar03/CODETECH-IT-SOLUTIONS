import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coding Quiz")
        self.root.geometry("500x400")  # Set the initial size of the window
        self.root.configure(background='lightblue')  # Set background color
        
        self.questions = {
            "Q1": {"question": "What does HTML stand for?",
                   "options": ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyper Tool Multi Language"],
                   "correct_answer": "Hyper Text Markup Language"},
            "Q2": {"question": "What does CSS stand for?",
                   "options": ["Colorful Style Sheets", "Computer Style Sheets", "Cascading Style Sheets", "Creative Style Sheets"],
                   "correct_answer": "Cascading Style Sheets"},
            "Q3": {"question": "Which of the following is not a programming language?",
                   "options": ["Java", "Python", "HTML", "C++"],
                   "correct_answer": "HTML"},
            "Q4": {"question": "What is the output of '2' + '3' in Python?",
                   "options": ["5", "23", "'5'", "TypeError"],
                   "correct_answer": "'23'"}
        }
        self.score = 0
        self.current_question = 1
        self.total_questions = len(self.questions)
        
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), bg='lightblue')  # Increase font size
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx), font=("Arial", 12))  # Increase font size
            button.pack(fill=tk.X)
            self.option_buttons.append(button)
        
        self.next_question()

    def next_question(self):
        if self.current_question <= self.total_questions:
            q_data = self.questions[f"Q{self.current_question}"]
            self.question_label.config(text=q_data["question"])
            for i, option in enumerate(q_data["options"]):
                self.option_buttons[i].config(text=option)
            self.current_question += 1
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {self.total_questions}!")
            self.root.destroy()

    def check_answer(self, idx):
        selected_option = self.questions[f"Q{self.current_question - 1}"]["options"][idx]
        correct_answer = self.questions[f"Q{self.current_question - 1}"]["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Correct answer is: {correct_answer}")
        self.next_question()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
