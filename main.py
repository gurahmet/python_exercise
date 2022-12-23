import random
import tkinter as tk

root = tk.Tk()
root.title("ROCK PAPER SCISSOR")
paper_img = tk.PhotoImage(file="img/paper.png", width=100, height=165)
rock_img = tk.PhotoImage(file="img/rock.png", width=100, height=165)
scissor_img = tk.PhotoImage(file="img/scissor.png", width=100, height=165)


class Operator:
    def __init__(self, my_card):
        self.my_card = my_card
        self.pc_cards = []
        self.result = []

    def shuffle(self):
        list_of_cards = ("paper", "rock", "scissor")
        self.pc_cards.append(random.choice(list_of_cards))
        return self.pc_cards

    def comparing(self):
        if self.pc_cards[0] == "paper":
            if self.my_card == "paper":
                self.result.append("It is Draw")
            elif self.my_card == "scissor":
                self.result.append("It is WIN")
            elif self.my_card == "rock":
                self.result.append("It is LOSE")
        elif self.pc_cards[0] == "rock":
            if self.my_card == "paper":
                self.result.append("It is WIN")
            elif self.my_card == "scissor":
                self.result.append("It is LOSE")
            elif self.my_card == "rock":
                self.result.append("It is DRAW")
        elif self.pc_cards[0] == "scissor":
            if self.my_card == "paper":
                self.result.append("It is LOSE")
            elif self.my_card == "scissor":
                self.result.append("It is DRAW")
            elif self.my_card == "rock":
                self.result.append("It is WIN")
        print(f"this is result: {self.result} \nComputer card: {self.pc_cards}\nYour card: {self.my_card}")


your_card = ""


def rock():
    global your_card
    your_card = "rock"
    numbers = Operator(your_card)
    numbers.shuffle()
    numbers.comparing()
    info_label = tk.Label(root, text=f"Computer card: {numbers.pc_cards}\n"
                                     f"Your card:{numbers.my_card}\n"
                                     f"Result: {numbers.result}".upper())
    info_label.grid(row=2, column=1, columnspan=3)


def paper():
    global your_card
    your_card = "paper"
    numbers = Operator(your_card)
    numbers.shuffle()
    numbers.comparing()
    info_label = tk.Label(root, text=f"Computer card: {numbers.pc_cards}\n"
                                     f"Your card:{numbers.my_card}\n"
                                     f"Result: {numbers.result}".upper())
    info_label.grid(row=2, column=1, columnspan=3)


def scissor():
    global your_card
    your_card = "scissor"
    numbers = Operator(your_card)
    numbers.shuffle()
    numbers.comparing()
    info_label = tk.Label(root, text=f"Computer card: {numbers.pc_cards}\n"
                                     f"Your card:{numbers.my_card}\n"
                                     f"Result: {numbers.result}".upper())
    info_label.grid(row=2, column=1, columnspan=3)


button_rock = tk.Button(root, image=rock_img, command=rock)
button_paper = tk.Button(root, image=paper_img, command=paper)
button_scissor = tk.Button(root, image=scissor_img, command=scissor)

button_paper.grid(row=1, column=1)
button_rock.grid(row=1, column=2)
button_scissor.grid(row=1, column=3)

root.mainloop()
