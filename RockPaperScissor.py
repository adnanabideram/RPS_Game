from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img_user = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors-user.png"))

# frames
top_frame = Frame(root, bg="#9b59b6", pady=20)
top_frame.grid(row=0, column=0, columnspan=5)
mid_frame = Frame(root, bg="#9b59b6", pady=20)
mid_frame.grid(row=1, column=0, columnspan=5)
bottom_frame = Frame(root, bg="#9b59b6", pady=20)
bottom_frame.grid(row=2, column=0, columnspan=5)

# user and computer labels
user_label = Label(mid_frame, image=scissor_img_user, bg="#9b59b6")
comp_label = Label(mid_frame, image=scissor_img_comp, bg="#9b59b6")
user_label.grid(row=0, column=0, padx=20)
comp_label.grid(row=0, column=4, padx=20)

# scores
playerScore = Label(mid_frame, text=0, font=('Allegro', 48), bg="#9b59b6", fg="white")
computerScore = Label(mid_frame, text=0, font=('Allegro', 48), bg="#9b59b6", fg="white")
playerScore.grid(row=0, column=1, padx=40)
computerScore.grid(row=0, column=3, padx=40)

# indicators
user_indicator = Label(top_frame, font=('Allegro', 24), text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(top_frame, font=('Allegro', 24), text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=1, padx=(30, 80))  # Move USER text a little left
comp_indicator.grid(row=0, column=3, padx=(290, 0))  # Move COMPUTER text more to the right

# messages
msg = Label(bottom_frame, font=('Allegro', 24), bg="#9b59b6", fg="white")
msg.grid(row=1, column=2, pady=10)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")

# update choices
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img_user)
    elif x == "paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)

    checkWin(x, compChoice)

# buttons
rock = Button(bottom_frame, width=20, height=2, text="ROCK", font=('Allegro', 16, 'bold'), bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock"))
rock.grid(row=2, column=1, padx=10, pady=10)
paper = Button(bottom_frame, width=20, height=2, text="PAPER", font=('Allegro', 16, 'bold'), bg="#FAD02E", fg="black", command=lambda: updateChoice("paper"))
paper.grid(row=2, column=2, padx=10, pady=10)
scissor = Button(bottom_frame, width=20, height=2, text="SCISSOR", font=('Allegro', 16, 'bold'), bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor"))
scissor.grid(row=2, column=3, padx=10, pady=10)

root.mainloop()
