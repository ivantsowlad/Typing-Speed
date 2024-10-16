import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
my_timer = ""


# ------------------------ TIMER --------------------------- #
def start_timer():
    test_text.delete('1.0', END)
    test_text.config(state="normal")
    work_sec = int(WORK_MIN * 60)
    count_down(work_sec)


def count_down(count):
    """In format 00 sec"""
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_sec} sec")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        test_text.config(state="disabled")
        canvas.itemconfig(timer_text, text="Time is off.")
        new_label.config(text="STOP", fg=RED)
        all_text = test_text.get('1.0', 'end-1c').split()
        print(all_text)
        for i in range(len(all_text)):
            if all_text[i] != check_words[i]:
                all_text[i] = "0"
        print(all_text)
        all_text = [i for i in all_text if i != "0"]
        print(all_text)
        score = round(len(" ".join(all_text))/5)
        messagebox.showinfo(title="RESULT", message=f"Your typing speed is {score} wpm.")
        return
    else:
        start_timer()


# ------------------------ WORDS LIST --------------------------- #
words_list = []
check_words = ["an", "ten", "do", "friend", "tree", "to", "right", "order", "like", "yet", "hear", "speed",
               "city", "pattern", "red", "still", "live", "war", "think", "still", "there", "think", "all",
               "family", "these", "try", "produce", "ever", "word", "came", "develop", "well", "ground", "got"]
word_to_print = " ".join(check_words)


# ------------------------------ UI SETUP -------------------------------- #
# ---- WINDOW ---- #
window = Tk()
window.minsize(500, 400)
window.title("Typing Speed")
window.config(padx=100, pady=50, bg=YELLOW)


# ----- CANVAS ---- #
canvas = Canvas(width=400, height=30, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(200, 15, text="00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

# ----- LABELS ---- #
new_label = Label(text="You need to type:", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
new_label.grid(column=1, row=1)

text_label = Label(text=word_to_print, font=(FONT_NAME, 20, "italic"), fg="black", bg=YELLOW, wraplength=600)
text_label.grid(column=1, row=2)

textfield = ScrolledText(wrap=tkinter.WORD)

# ----- BUTTON ---- #
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer, width=10, font=(FONT_NAME, 30, "italic"), bg=GREEN)
start_button.grid(column=1, row=3)

# ----- TEST TEXT ---- #
test_text = Text(window, width=50, height=10, state="disabled", bg=YELLOW, fg="black", font=(FONT_NAME, 20, "italic"))
test_text.grid(column=1, row=4)

typed_text_list = test_text.get('1.0', 'end-1c').split()
a = test_text.get('1.0', 'end-1c').split()
print(a)

window.mainloop()
