import tkinter as tk

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
    text="Question Goes Here",
    font=("Arial", 22, "bold"),
    bg="#d9d9d9",
    fg="black",
    wraplength=600
)

question_label.place(x=5, y=25, anchor="center")


question_label.place(relx=0.5, rely=0.45, anchor="center")

button_font = ("Arial", 18, "bold")

red_button = tk.Button(
    main_frame,
    text="Answer 1",
    bg="red",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

red_button.place(x=70, y=40)

blue_button = tk.Button(
    main_frame,
    text="Answer 2",
    bg="#00a2ff",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

blue_button.place(x=410, y=40)

yellow_button = tk.Button(
    main_frame,
    text="Answer 3",
    bg="yellow",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

yellow_button.place(x=70, y=280)

green_button = tk.Button(
    main_frame,
    text="Answer 4",
    bg="green",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

green_button.place(x=410, y=280)

root.mainloop()

questions = [
    {
        "Question 1": "Are you ready for this test?",
        "Answers": ["Yes", "No", "Maybe", "Did I win?"],
        "Correct": "No"
    },

    {


    },

]
import tkinter as tk

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
    text="Question Goes Here",
    font=("Arial", 22, "bold"),
    bg="#d9d9d9",
    fg="black",
    wraplength=600
)

question_label.place(x=5, y=25, anchor="center")


question_label.place(relx=0.5, rely=0.45, anchor="center")

button_font = ("Arial", 18, "bold")

red_button = tk.Button(
    main_frame,
    text="Answer 1",
    bg="red",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

red_button.place(x=70, y=40)

blue_button = tk.Button(
    main_frame,
    text="Answer 2",
    bg="#00a2ff",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

blue_button.place(x=410, y=40)

yellow_button = tk.Button(
    main_frame,
    text="Answer 3",
    bg="yellow",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

yellow_button.place(x=70, y=280)

green_button = tk.Button(
    main_frame,
    text="Answer 4",
    bg="green",
    fg="black",
    font=button_font,
    width=18,
    height=5,
    bd=5,
    relief="raised"
)

green_button.place(x=410, y=280)

root.mainloop()

questions = [
    {
        "Question 1": "Are you ready for this test?",
        "Answers": ["Yes", "No", "Maybe", "Did I win?"],
        "Correct": "No"
    },

    {
        "Question 2": "",
        "Answers": [],
        "Correct": ""

    },

]