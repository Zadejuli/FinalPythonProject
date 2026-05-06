import tkinter as tk

questions = [
{
        "question": "Are you ready for this test?",
        "answers": ["Yes", "No", "Maybe", "Did I win?"],
        "correct": "No"
    },
{
        "question": 'Why was the answer for Question 1 "No?"',
        "answers": ["Because", "No", "Its the opposite of Yes", "Donkey Kong"],
        "correct": "Because"
    },
{
        "question": "Is the next question going to be the first REAL one?",
        "answers": ["Yes", "Yes", "Yes", "Yes"],
        "correct": "Yes"
    },
{
        "question": "What does GUI stand for?",
        "answers": ["Grape Under Ingot","Guacamole Universe Inside","Graphical User Interface","Graphicals Users Interfaces"],
        "correct": "Graphical User Interface"
    },
{
        "question": "There are Lists, Sets, and ______",
        "answers": ["Banjos", "Toodles", "Tinkles", "Tuples"],
        "correct": "Tuples"
    },
{
        "question": "What color tie does Spongebob wear?",
        "answers": ["Green", "Red", "Blue", "Pink"],
        "correct": "Red"
    },
{
        "question": "What does Mr. Krabs on the news in the first Spongebob movie?",
        "answers": ["Hello, I like money.", "Hello, I'm a crab.", "Give me your money!", "I have a secret formula!"],
        "correct": "Hello, I like money."
    },
{
        "question": "How much wood could a woodchuck chuck if a woodchuck could chuck wood?",
        "answers": ["IDK", "3 pounds", "700 pounds", "50 pounds"],
        "correct": "700 pounds"
    },
{
        "question": "Gobbling gorgoyles gobbled gobbling goblins",
        "answers": ["Yeah! Thats what Im saying!", "Goggles", "Giggity", "What?"],
        "correct": "Yeah! Thats what Im saying!"
    },
{
        "question": "How do you spells the teachers name?",
        "answers": ["Bawn", "Bonn", "Bawn", "Baun"],
        "correct": "Baun"
    },
{
        "question": 'If Wario is evil Mario, why isnt Waluigi "Γuigi"',
        "answers": ["Because hes purple",'Because Luigis name with the Japanese word warui, means "bad luigi"', "Because hes so evil", "Warioware"],
        "correct": 'Because Luigis name with the Japanese word warui, means "bad Luigi"'
    },
{
        "question": "",
        "answers": ["", "", "", ""],
        "correct": ""
    },





]

current_question = 0

lives = 3

root = tk.Tk()
root.title("Impossible Quiz")
root.geometry("900x600")
root.configure(bg="black")
root.resizable(False, False)

main_frame = tk.Frame(
    root,
    bg="#d9d9d9",
    width=750,
    height=500,
    highlightbackground="black",
    highlightthickness=4
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

question_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 22, "bold"),
    bg="#d9d9d9",
    fg="black",
    wraplength=600
)

lives_label = tk.Label(
    main_frame,
    text=f"Lives: {lives}",
    font=("Arial", 16, "bold"),
    bg="#d9d9d9",
    fg="red"
)

question_label.place(relx=0.5, rely=0.51, anchor="center")

button_font = ("Arial", 18, "bold")

lives_label.place(x=10, y=0)

def load_question():
    question = questions[current_question]

    question_label.config(
        text=question["question"]
    )

    answers = question["answers"]

    red_button.config(text=answers[0])
    blue_button.config(text=answers[1])
    yellow_button.config(text=answers[2])
    green_button.config(text=answers[3])

def check_answer(answer):
    global current_question
    global lives

    question = questions[current_question]

    if answer == question["correct"]:
        question_label.config(text="Correct")
    else:
        lives -= 1

        lives_label.config(
            text=f"Lives: {lives}"


        )


        question_label.config(text="Wrong")

        if lives == 0:
            print("SUPER F! YOU FAILED!")
            root.after(1000, root.destroy)
            return

    current_question += 1

    if current_question < len(questions):
        root.after(1000, load_question)

red_button = tk.Button(
    main_frame,
    bg="red",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=200,
    command=lambda: check_answer(red_button["text"])
)

red_button.place(x=70, y=40)

blue_button = tk.Button(
    main_frame,
    bg="#00a2ff",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=200,
    command=lambda: check_answer(blue_button["text"])
)

blue_button.place(x=410, y=40)

yellow_button = tk.Button(
    main_frame,
    bg="yellow",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=200,
    command=lambda: check_answer(yellow_button["text"])
)

yellow_button.place(x=70, y=280)

green_button = tk.Button(
    main_frame,
    bg="green",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=200,
    command=lambda: check_answer(green_button["text"])
)

green_button.place(x=410, y=280)

load_question()

root.mainloop()