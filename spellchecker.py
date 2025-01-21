import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x500")
root.config(background="#C19EE0")

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())
    spell.config(text=right)  # Display corrected text in the correct place

# Main Frame to Center Everything
main_frame = Frame(root, bg="#C19EE0")
main_frame.pack(expand=True)  # Centers the entire layout

# Heading (Centered)
heading = Label(main_frame, text="Spelling Checker", font=("Cardo", 24, "bold"), bg="#C19EE0", fg="#6247AA")
heading.pack(pady=(10, 10))

# Entry Field (Centered)
enter_text = Entry(main_frame, justify="center", font=("Trebuchet MS", 20), bg="white", border=2)
enter_text.pack(pady=10, padx=20, fill=X)
enter_text.focus()

# Check Button (Centered)
button = Button(main_frame, text="Check", font=("arial", 18, "bold"), fg="white", bg="#C05299", command=check_spelling)
button.pack(pady=10)

# Output Section (Centered)
output_frame = Frame(main_frame, bg="#C19EE0")  # Group output elements
output_frame.pack(pady=10)

cs = Label(output_frame, text="Correct Text is:", font=("Trebuchet MS", 18), bg="#C19EE0")
cs.pack(side=LEFT, padx=(10, 5))

spell = Label(output_frame, font=("Trebuchet MS", 18), bg="#C19EE0", fg="#6247AA")
spell.pack(side=LEFT)

root.mainloop()