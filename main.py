from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Heart Toe")
root.iconbitmap('icon_toe.ico')

# X start True
clicked = True
count = 0
ai_starts = False
# Initialize scores
x_score = 0
heart_score = 0
ai_symbol= "♥"

#disable all buttons
def disable_b():
    buttons["b1"].config(state= DISABLED)
    buttons["b2"].config(state= DISABLED)
    buttons["b3"].config(state= DISABLED)
    buttons["b4"].config(state= DISABLED)
    buttons["b5"].config(state= DISABLED)
    buttons["b6"].config(state= DISABLED)
    buttons["b7"].config(state= DISABLED)
    buttons["b8"].config(state= DISABLED)
    buttons["b9"].config(state= DISABLED)

buttons = {"b1": " ", "b2": " ", "b3": " ",
           "b4": " ", "b5": " ", "b6": " ",
           "b7": " ", "b8": " ", "b9": " "}


# Add labels to display scores
x_label = Label(root, text="X Score: " + str(x_score), anchor= "w", font=("Helvetica", 12), fg="#0489B1")
x_label.grid(row=3, column=0, padx=10, pady=10)
heart_label = Label(root, text="♥ Score: " + str(heart_score), anchor = "e", font=("Helvetica", 12), fg="red")
heart_label.grid(row=3, column=2, padx=10, pady=10)

def ai_turn():
    global clicked, count
    # Check if the player has made a move
    if count == 0:
        return
    # Find all empty buttons
    empty_buttons = [b for b in buttons.values() if b["text"] == " "]
    if empty_buttons:
        # Randomly select an empty button
        button = random.choice(empty_buttons)
        # Put a symbol in the button
        if clicked:
            button["text"] = "X"
            button["fg"] = "#0489B1"
        else:
            button["text"] = ai_symbol
            button["fg"] = "red"
        count += 1
        # Check for a win or tie
        won()
        if count == 9 and not winner:
            disable_b()
        else:
            clicked = not clicked

def player_turn():
    global clicked, count, buttons
    # Put a symbol in the button
    if clicked:
        buttons["text"] = "X"
        buttons["fg"] = "#0489B1"
    else:
        buttons["text"] = "♥"
        buttons["fg"] = "red"
    count += 1
    # Check for a win or tie
    won()
    if count == 9 and not winner:
        disable_b()
    else:
        clicked = not clicked
    # Call ai_turn() after the player has made a move
    ai_turn()

#check for X win
def won():
    global winner, x_score, heart_score
    winner = False
    if buttons["b1"]["text"] == "X" and buttons["b2"]["text"] == "X" and buttons["b3"]["text"] == "X":
        buttons["b1"].config(bg="gray")
        buttons["b2"].config(bg="gray")
        buttons["b3"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()
    
    elif buttons["b4"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b6"]["text"] == "X":
        buttons["b4"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b6"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()

    elif buttons["b7"]["text"] == "X" and buttons["b8"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b7"].config(bg="gray")
        buttons["b8"].config(bg="gray")
        buttons["b9"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()
    
    elif buttons["b1"]["text"] == "X" and buttons["b4"]["text"] == "X" and buttons["b7"]["text"] == "X":
        buttons["b1"].config(bg="gray")
        buttons["b4"].config(bg="gray")
        buttons["b7"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()

    elif buttons["b2"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b8"]["text"] == "X":
        buttons["b2"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b8"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()

    elif buttons["b3"]["text"] == "X" and buttons["b6"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b3"](bg="gray")
        buttons["b6"](bg="gray")
        buttons["b9"](bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()

    elif buttons["b3"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b7"]["text"] == "X":
        buttons["b3"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b7"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()
        
    elif buttons["b1"]["text"] == "X" and buttons["b5"]["text"] == "X" and buttons["b9"]["text"] == "X":
        buttons["b1"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b9"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n X wins!")
        x_score += 1
        x_label.config(text="X Score: " + str(x_score))
        disable_b()
#Check for ♥ win
    if buttons["b1"]["text"] == "♥" and buttons["b2"]["text"] == "♥" and buttons["b3"]["text"] == "♥":
        buttons["b1"].config(bg="gray")
        buttons["b2"].config(bg="gray")
        buttons["b3"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()
    
    elif buttons["b4"]["text"] == "♥" and buttons["b5"]["text"] == "♥" and buttons["b6"]["text"] == "♥":
        buttons["b4"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b6"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()

    elif buttons["b7"]["text"] == "♥" and buttons["b8"]["text"] == "♥" and buttons["b9"]["text"] == "♥":
        buttons["b7"].config(bg="gray")
        buttons["b8"].config(bg="gray")
        buttons["b9"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()
    
    elif buttons["b1"]["text"] == "♥" and buttons["b4"]["text"] == "♥" and buttons["b7"]["text"] == "♥":
        buttons["b1"].config(bg="gray")
        buttons["b4"].config(bg="gray")
        buttons["b7"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()

    elif buttons["b2"]["text"] == "♥" and buttons["b5"]["text"] == "♥" and buttons["b8"]["text"] == "♥":
        buttons["b2"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b8"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()

    elif buttons["b3"]["text"] == "♥" and buttons["b6"]["text"] == "♥" and buttons["b9"]["text"] == "♥":
        buttons["b3"].config(bg="gray")
        buttons["b6"].config(bg="gray")
        buttons["b9"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()

    elif buttons["b3"]["text"] == "♥" and buttons["b5"]["text"] == "♥" and buttons["b7"]["text"] == "♥":
        buttons["b3"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b7"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()
        
    elif buttons["b1"]["text"] == "♥" and buttons["b5"]["text"] == "♥" and buttons["b9"]["text"] == "♥":
        buttons["b1"].config(bg="gray")
        buttons["b5"].config(bg="gray")
        buttons["b9"].config(bg="gray")
        winner = True
        messagebox.showinfo("Tic Heart Toe", "Congrats!\n ♥ wins!")
        heart_score += 1
        heart_label.config(text="♥ Score: " + str(heart_score))
        disable_b()
    #Ties
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Heart Toe", " Tied!\n Go again?")
        disable_b()

#Button click function
def b_click(b):
    global clicked, count, ai_starts

    # Check if it's the player's turn
    if b["text"] == " ":
        if clicked:
            b["text"] = "X"
            b["fg"] = "#0489B1"
        else:
            b["text"] = "♥"
            b["fg"] = "red"
        
        clicked = not clicked
        count += 1
        won()
        

        if not clicked and not winner:
            ai_turn()


def reset():
    global buttons, clicked, count
    for button in buttons.values():
        clicked = True
        count = 0

#buttons section
    buttons = {
    "b1": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b1"])),
    "b2": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b2"])),
    "b3": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b3"])),
    "b4": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b4"])),
    "b5": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b5"])),
    "b6": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b6"])),
    "b7": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b7"])),
    "b8": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b8"])),
    "b9": Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(buttons["b9"]))
}

#Grid buttons
    buttons["b1"].grid(row=0, column=0)
    buttons["b2"].grid(row=0, column=1)
    buttons["b3"].grid(row=0, column=2)

    buttons["b4"].grid(row=1, column=0)
    buttons["b5"].grid(row=1, column=1)
    buttons["b6"].grid(row=1, column=2)

    buttons["b7"].grid(row=2, column=0)
    buttons["b8"].grid(row=2, column=1)
    buttons["b9"].grid(row=2, column=2)

#create menu
my_menu= Menu(root)
root.config(menu=my_menu)
#menu option
option_menu= Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset game", command=reset)
option_menu.add_command(label="PVE", command=ai_turn)
option_menu.add_command(label="PVP", command=player_turn)


reset()

root.mainloop()