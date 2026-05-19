import tkinter as tk
from PIL import Image, ImageTk

questions = [
{
        "question": "Are you ready for this test?",
        "answers": ["Yes", "No", "Maybe", "Did I win?"],
        "correct": "No",
        "hint": "Are you sure?"
    },
{
        "question": 'Why was the answer for Question 1 "No?"',
        "answers": ["Because", "No", "Its the opposite of Yes", "Donkey Kong"],
        "correct": "Because",
        "hint": "Because I said so."
    },
{
        "question": "Is the next question going to be the first REAL one?",
        "answers": ["Yes", "Yes", "Yes", "Yes"],
        "correct": "Yes",
        "hint": "dude."
    },
{
        "question": "What does GUI stand for?",
        "answers": ["Grape Under Ingot","Guacamole Universe Inside","Graphical User Interface","Graphicals Users Interfaces"],
        "correct": "Graphical User Interface",
        "hint": "Read carefully."
    },
{
        "question": "There are Lists, Sets, and ______",
        "answers": ["Tangos", "Toodles", "Tinkles", "Tuples"],
        "correct": "Tuples",
        "hint": "Starts with T and ends with S."
    },
{
        "question": "What color tie does Spongebob wear?",
        "answers": ["Green", "Red", "Blue", "Pink"],
        "correct": "Red",
        "hint": "Well, I don't think its green."
    },
{
        "question": "What does Mr. Krabs on the news in the first Spongebob movie?",
        "answers": ["Hello, I like money.", "Hello, I'm a crab.", "Give me your money!", "I have a secret formula!"],
        "correct": "Hello, I like money.",
        "hint": "I mean, he does."
    },
{
        "question": "How much wood could a woodchuck chuck if a woodchuck could chuck wood?",
        "answers": ["IDK", "3 pounds", "700 pounds", "50 pounds"],
        "correct": "700 pounds",
        "hint": "I am NOT lying this answer is true."
    },
{
        "question": "Gobbling gorgoyles gobbled gobbling goblins",
        "answers": ["Yeah! Thats what Im saying!", "Goggles", "Giggity", "What?"],
        "correct": "Yeah! Thats what Im saying!",
        "hint": "I mean, dude has a point."
    },
{
        "question": "How do you spells the teachers name?",
        "answers": ["Bawn", "Bonn", "Baan", "Baun"],
        "correct": "Baun",
        "hint": "..."
    },
{
        "question": "How many nuclear bombs could Wario tank.",
        "answers": ["500,000","None","1","Infinite"],
        "correct": "Infinite",
        "hint": "He's invincible."
    },
{
        "question": "Click the one its pointing at",
        "answers": ["↓", "its--↓", "↑", "↖"],
        "correct": "↖",
        "hint": "THINK."
    },
{
        "question": "Who do you spend 5 nights with?",
        "answers": ["Freddy", "Mr Peterson", "Baldi", "Nobody"],
        "correct": "Freddy",
        "hint": "scary bear!"
    },
{
        "question": "How do you make a tissue dance? Put a little boogie in it!",
        "answers": ["sooo funny", "hahahaha", "haha", "hahaha"],
        "correct": "hahaha",
        "hint": "DONT laugh too much or too little."
    },
{
        "question": 'Click "Green"',
        "answers": ["Click Green", "Green", "Click Blue", "Blue"],
        "correct": "Green",
        "hint": "Its in quotes."
    },
{
        "question": "What does OOP stand for?",
        "answers": ["Old Obtuse Pastry", "Original Obelisk Pothole", "Objecting Oriented Programmers", "Object Oriented Programming"],
        "correct": "Object Oriented Programming",
        "hint": "Read carefully."
    },
{
        "question": "Homer dropped his _______ D'oh!",
        "answers": ["GUI", "Donut", "Soda", "Doorway"],
        "correct": "Donut",
        "hint": "mmmmm dooonutttt"
    },
{
        "question": "What Holiday is on November 16th?",
        "answers": ["Spend Time With Your Family Day", "Not National Button Day", "International Check Your Wipers day", "Annual Eat A Live Turkey Day"],
        "correct": "International Check Your Wipers day",
        "hint": "People at Willow Grove, PA (1509 Easton Rd) probably do this all the time."
    },
{
        "question": "How many holes in a polo?",
        "answers": ["Two", "One", "Three", "Four"],
        "correct": "Four",
        "hint": "The shirt."
    },
{
        "question": "What is Mr Bauns room number?",
        "answers": ["H205", "H206", "H203", "H20"],
        "correct": "H205",
        "hint": "Water x 5."
    },
{
        "question": "Can a match box?",
        "answers": ["No, but a tin can", "No", "I'm sure they could!", "Yes"],
        "correct": "No, but a tin can",
        "hint": "Can it? CAN it?"
    },
{
        "question": "What game had the most concurrent players at one time?",
        "answers": ["Fortnite", "PUBG", "Roblox - Steal a Brainrot", "Roblox - Grow a Garden"],
        "correct": "Roblox - Steal a Brainrot",
        "hint": "This kind of surprised me, and at the same time did not."
    },
{
        "question": "If Christmas is the 25th, and Halloween is the 31st, why isn't Thanksgiving?",
        "answers": ["Thanksgiving what?", "Everyday!", "The 40st", "Yeah"],
        "correct": "The 40st",
        "hint": "Is this a day? Can it be?"
    },
{
        "question": "3000000(pi) + 2.63 x 999 - 8",
        "answers": ["9427397.331", "1", "8399402.435", "0110100001101001"],
        "correct": "9427397.331",
        "hint": "Its so easy, do it in your head. I mean, its fourth number is obviously a 7!"
    },
{
        "question": "Standing in Bauns room, and looking out the door, which way is the fire exit?",
        "answers": ["Right then left", "Right", "Up", "Left"],
        "correct": "Left",
        "hint": "The RIGHT answer is LEFT."
    },
{
        "question": "In the Spongebob movie, which quote is line 1492 in the transcript?",
        "answers": ["Did you see my butt?", "Are you crazy? I was just gonna say that your fly is down!", "We’re on a baby hunt, and don’t think we don’t know how to weed ’em out.", "I’m ready. Depression. I’m ready. Depression."],
        "correct": "Are you crazy? I was just gonna say that your fly is down!",
        "hint": "Come on Squidward. Some decency?"
    },
{
        "question": "Whats heavier, 1000 bricks or 1000 feathers?",
        "answers": ["Bricks", "Feathers", "Equal", "Or"],
        "correct": "Bricks",
        "hint": "speed im watching your stream why you trying not to laugh bro"
    },
{
        "question": "Which one of these is NOT a Python error?",
        "answers": ["SyntaxError", "TypeError", "PotatoError", "NameError"],
        "correct": "PotatoError",
        "hint": "The Amazing World of Gumball: Season 5, Episode 12."
    },
{
        "question": "You must pick the WRONG answer.",
        "answers": ["2 + 2 = baby 2", "0 + 0 = 2", "8 - 4 = 8", "2 + 2 = 4"],
        "correct": "2 + 2 = 4",
        "hint": "Think like a philosopher."
    },
{
        "question": "The next question is generated by AI, will you be kind to its funny question?",
        "answers": ["Yeah", "No", "We will see", "Hopefully"],
        "correct": "We will see",
        "hint": "We will."
    },
{
        "question": "Which button would you press if your sandwich exploded?",
        "answers": ["Call NASA", "Eat the explosion", "Cry dramatically", "The blue one"],
        "correct": "Cry dramatically",
        "hint": "Not even a button, more of an emotion."
    },
{
        "question": "Did you love it? You want another one?",
        "answers": ["Yes", "Yes", "Yes", "No"],
        "correct": "No",
        "hint": "Is it a trick question? No."
    },
{
        "question": "Choose the most trustworthy life form.",
        "answers": ["A raccoon with sunglasses", "An eel named Gregory", "A microwave", "Kevin"],
        "correct": "Kevin",
        "hint": "I remember him being mean but whatever you say."
    },
{
        "question": "Okay! Okay. One more! Just...click anywhere!",
        "answers": ["", "", "", ""],
        "correct": "",
        "hint": "DUDE."
    },
{
        "question": "Which one of these definitely pays taxes?",
        "answers": ["Goblin", "Toaster", "Fish", "The IRS Dragon"],
        "correct": "The IRS Dragon",
        "hint": "Something a millennial would make up."
    },
{
        "question": "This next one might get ya messy!",
        "answers": ["Why?", "Okay", "What?", "I don't understand"],
        "correct": "Why?"
    },
{
        "question": "Cause we're playin' bendy",
        "answers": ["Like the game?", "Huh?", "Why?", "The ink machine?"],
        "correct": "Why?"
    },
{
        "question": "If a bird flies, and a cat walks, whats a fly?",
        "answers": ["A fly", "A walk", "A thing", "An insect"],
        "correct": "An insect"
    },
{
        "question": "How many ants are there on earth?",
        "answers": ["20 quadrillion", "18.5 million", "900 billion", "18"],
        "correct": "20 quadrillion"
    },
{
        "question": "Why did the waiter say 1+1 to the chef?",
        "answers": ["Maybe there's one pie and another pie", "IDK", "Its actually a classroom", "Because 1+1 is stew!"],
        "correct": "Because 1+1 is stew!"
    },
{
        "question": "Which one sounds like a fake app?",
        "answers": ["TikTok", "Discord", "BlorboChat", "Spotify"],
        "correct": "BlorboChat"
    },
{       "question": "Mini Pekka",
        "answers": ["Butterfly", "Robot", "Pancake", "Fight"],
        "correct": "Pancake"
    },
{
        "question": "Which one of these is NOT a real Mario character?",
        "answers": ["Waluigi", "Toad", "Goombario", "Bingus"],
        "correct": "Bingus"
    },
{
        "question": "Is this quiz the most awesome ever?",
        "answers": ["Yeah", "No", "Sometimes", "NO WAY"],
        "correct": "Sometimes"
    },
{
        "question": "What drink ruined Mr Bauns computer?",
        "answers": ["Pina Colada", "Pepsi", "Root Beer Float", "Water"],
        "correct": "Root Beer Float"
    },
{
        "question": "BE RESPECTFUL, BE RESPONSIBLE, BE ___",
        "answers": ["ENVIOUS", "ENTITLED", "ENGAGING", "ENGAGED"],
        "correct": "ENGAGED"
    },
{
        "question": "What is the name of Joey Majors made up character?",
        "answers": ["Indiana Longnose", "Sally Slippydopple", "Rubert Ticklecopter", "Robby Radishorse"],
        "correct": "Idiana Longnose"
    },
{
        "question": "Page 83 of the PA drivers manual, whats the fine for a .10 to .159 blood alcohol concentration?",
        "answers": ["$700 - $7,000", "$100 - $750", "$500 - $5,000", "Nothing"],
        "correct": "$500 - $5,000"
    },
{
        "question": "Are you ready? The next one is the last.",
        "answers": ["Yes", "Did I win?", "No", "Maybe"],
        "correct": "Yes"
    },
{
        "question": "THE. SUPER. OMEGA. AWESOME. QUIZ.",
        "answers": ["WIN BUTTON!", "END", "LOSE BUTTON!", "TSOAQ"],
        "correct": "WIN BUTTON!"
    },

]

current_question = 0
lives = 3

root = tk.Tk()
root.title("The Awesome Quiz")
root.geometry("900x600")
root.configure(bg="black")
root.resizable(False, False)

title_frame = tk.Frame(root, bg="black", width=900, height=600)
title_frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(
    title_frame,
    text="THE SUPER OMEGA AWESOME QUIZ",
    font=("Arial", 36, "bold"),
    fg="red",
    bg="black"
)
title_label.pack(pady=150)

def start_game():
    title_frame.destroy()
    main_frame.place(relx=0.5, rely=0.5, anchor="center")
    question_label.place(relx=0.5, rely=0.51, anchor="center")
    lives_label.place(x=10, y=0)
    load_question()

start_button = tk.Button(
    title_frame,
    text="PLAY MY GAME.",
    font=("Arial", 20, "bold"),
    bg="green",
    fg="black",
    command=start_game
)
start_button.pack()

main_frame = tk.Frame(
    root,
    bg="#d9d9d9",
    width=750,
    height=500,
    highlightbackground="black",
    highlightthickness=4
)

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

button_font = ("Arial", 18, "bold")

def load_question():
    question = questions[current_question]
    question_label.config(text=question["question"])

    answers = question["answers"]

    red_button.config(text=answers[0])
    blue_button.config(text=answers[1])
    yellow_button.config(text=answers[2])
    green_button.config(text=answers[3])

def check_answer(answer):

    global current_question, lives

    question = questions[current_question]

    if answer == question["correct"]:
        question_label.config(text="Correct!")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        question_label.config(text="Wrong!")

        if lives == 0:
            question_label.config(text="GAME OVER")
            root.after(1500, root.destroy)
            return

    current_question += 1

    if current_question < len(questions):
        root.after(1000, load_question)

def show_hint():
    question = questions[current_question]

    hint_popup = tk.Label(
        root,
        text=question["hint"],
        font=("Arial", 16, "bold"),
        bg="yellow",
        fg="black",
        relief="solid",
        bd=3,
        padx=20,
        pady=10
    )

    hint_popup.place(relx=0.5, rely=0.125, anchor="center")

    root.after(1000, hint_popup.destroy)

red_button = tk.Button(
    main_frame,
    bg="red",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=250,
    command=lambda: check_answer(red_button["text"])
)

blue_button = tk.Button(
    main_frame,
    bg="#00a2ff",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=250,
    command=lambda: check_answer(blue_button["text"])
)

yellow_button = tk.Button(
    main_frame,
    bg="yellow",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=250,
    command=lambda: check_answer(yellow_button["text"])
)

green_button = tk.Button(
    main_frame,
    bg="green",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    wraplength=250,
    command=lambda: check_answer(green_button["text"])
)

red_button.place(x=70, y=40)
blue_button.place(x=410, y=40)
yellow_button.place(x=70, y=280)
green_button.place(x=410, y=280)

hint_button = tk.Button(
    main_frame,
    text="Hint",
    font=("Arial", 16, "bold"),
    bg="lightgray",
    fg="black",
    width=15,
    command=show_hint
)

hint_button.place(relx=0.5, rely=0.96, anchor="center")

root.mainloop()