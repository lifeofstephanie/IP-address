import customtkinter
from tkinter import messagebox

questions = [
    {
        "question": "Who is the current president of Nigeria?",
        "options": ["Buhari", "Yaradua", "Jonathan", "Tinubu"],
        "Correct Answer": "Tinubu"
    },
    {
        "question": "Which is the most user-friendly programming language?",
        "options": ["Python", "Java", "JavaScript", "Kotlin"],
        "Correct Answer": "Python"
    },
    {
        "question": "Which is not an Operating system?",
        "options": ["Windows", "Linux", "Android", "Vscode"],
        "Correct Answer": "Vscode"
    },
    {
        "question": "Which of the following is a Python framework?",
        "options": ["Django", "node", "Spark", "Bootstrap"],
        "Correct Answer": "Django"
    }
]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("480x350")
app.title("Quiz")

question_label = customtkinter.CTkLabel(
    app, text="", font=customtkinter.CTkFont(size=18, weight="bold"))
question_label.pack(pady=12)

option_buttons = []
for i in range(4):
    btn = customtkinter.CTkButton(app, fg_color=("gray75", "gray30"))
    btn.pack(pady=12, padx=20)
    option_buttons.append(btn)

current_question = 0
score = 0

def next_question():
    global current_question
    if current_question < len(questions):
        ask_question(questions[current_question])
        current_question += 1
    else:
        show_final_score()

def ask_question(question):
    question_label.configure(text=question["question"])

    for i in range(4):
        option = question["options"][i]  # Changed "Options" to "options"
        option_buttons[i].configure(text=option, command=lambda x=option: check_answer(x))

def check_answer(answer):
    global score

    if answer == questions[current_question-1]["Correct Answer"]:
        score += 1
        result_label.configure(text="Correct!")
    else:
        result_label.configure(text=f"Incorrect. The answer is {questions[current_question-1]['Correct Answer']}")

    next_question()

def show_final_score():
    final_text = f"Your final score is {score} / {len(questions)}"
    result_label.configure(text=final_text)
    app.destroy()
    messagebox.showinfo("Quiz Completed", final_text)

result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=12)

next_question()
app.mainloop()
