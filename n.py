from tkinter import *

# -----------------------------
# Personal information
# -----------------------------
my_personal_info = {
    "name": "eysra salum mengi",
    "age": "14 years",
    "school": "shamsiye boys secondary school",
    "hobby": "football,working out,making money and rapping",
    "height": "158 cm",
    "mother": "elizabeth",
    "father": "salum",
    "food": "burger and pizza",
    "occupation": "software Engineering",
    "contact": "+225761935555"
}

# -----------------------------
# Function to send message
# -----------------------------
def send_message():
    question = entry.get().lower().strip()

    if question == "":
        return

    chat_box.config(state=NORMAL)
    chat_box.insert(END, "🧑 You: " + entry.get() + "\n")

    if "name" in question:
        answer = my_personal_info["name"]

    elif "age" in question:
        answer = my_personal_info["age"]

    elif "school" in question:
        answer = my_personal_info["school"]

    elif "hobby" in question:
        answer = my_personal_info["hobby"]

    elif "height" in question:
        answer = my_personal_info["height"]

    elif "mother" in question:
        answer = my_personal_info["mother"]

    elif "father" in question:
        answer = my_personal_info["father"]

    elif "food" in question:
        answer = my_personal_info["food"]

    elif "occupation" in question:
        answer = my_personal_info["occupation"]

    elif "contact" in question:
        answer = my_personal_info["contact"]

    elif question == "bye":
        answer = "Goodbye!"
        chat_box.insert(END, "🤖 Bot: " + answer + "\n")
        window.after(1000, window.destroy)
        return

    else:
        answer = "SIJUI"

    chat_box.insert(END, "🤖 Bot: " + answer + "\n\n")
    chat_box.see(END)
    chat_box.config(state=DISABLED)

    entry.delete(0, END)

# -----------------------------
# Main Window
# -----------------------------
window = Tk()
window.title("eysra'S CHATBOT")
window.geometry("850x500")
window.configure(bg="lightblue")

# Title
title = Label(
    window,
    text="🤖 eysra'S CHATBOT",
    font=("Arial",18,"bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=10)

# Main Frame
main_frame = Frame(window, bg="lightblue")
main_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

# -----------------------------
# LEFT SIDE (Chat Box)
# -----------------------------
left_frame = Frame(main_frame, bg="lightblue")
left_frame.pack(side=LEFT, padx=10)

scroll = Scrollbar(left_frame)

chat_box = Text(
    left_frame,
    width=45,
    height=22,
    font=("Arial",11),
    yscrollcommand=scroll.set,
    state=DISABLED
)

scroll.config(command=chat_box.yview)

chat_box.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

# -----------------------------
# RIGHT SIDE
# -----------------------------
right_frame = Frame(main_frame, bg="lightblue")
right_frame.pack(side=LEFT, padx=20)

Label(
    right_frame,
    text="Ask me a question",
    font=("Arial",14,"bold"),
    bg="lightblue"
).pack(pady=10)

entry = Entry(
    right_frame,
    width=28,
    font=("Arial",13)
)
entry.pack(pady=15)

send_button = Button(
    right_frame,
    text="SEND",
    command=send_message,
    bg="green",
    fg="white",
    font=("Arial",12,"bold"),
    width=12
)
send_button.pack()

window.bind("<Return>", lambda event: send_message())

entry.focus()

window.mainloop()