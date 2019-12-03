import random
import os
from tkinter import *

from PIL import ImageTk, Image

from BlackJack import DHand, Hand

cards = ["d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk", "da", "s2", "s3", "s4", "s5", "s6",
         "s7", "s8", "s9", "s10", "sj", "sq", "sk", "sa", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj",
         "hq", "hk", "ha", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck", "ca"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
removed = []

dea = DHand.DHand()
play = Hand.Hand()


# stand method will just be continue (doing it in the gui)
# make player class after sure initial blackjack works


class GUI():
    def __init__(self, window):
        self.window = window
        bgcolor = "#ff0000"
        window.title("Blackjack")
        window.geometry("1280x800")
        window.resizable(0, 0)

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=1)

        self.hang_frame = Frame(master=self.frame)
        self.dealer = []
        self.player = []
        self.middle = []

        # dealer cards canvas
        for i in range(9):
            self.dealer.append(Canvas(master=self.hang_frame, width=140, height=280, bg="green", highlightthickness=0))
            self.dealer[i].grid(row=0, column=i)

        # chips canvas
        for i in range(9):
            self.middle.append(Canvas(master=self.hang_frame, width=140, height=40, bg="green", highlightthickness=0))
            self.middle[i].grid(row=1, column=i)

        self.label = Label(self.frame, text="", bg=bgcolor, fg="white")
        self.label.grid(row=4, column=4)
        self.label.config(font=("Courier", 18))

        # player cards canvas
        for i in range(9):
            self.player.append(Canvas(master=self.hang_frame, width=140, height=280, bg="green", highlightthickness=0))
            self.player[i].grid(row=2, column=i)

        self.hang_frame.grid(row=1, padx=5, pady=20, columnspan=9)

        self.money = Label(self.frame, text="Money: " + str(play.money), bg=bgcolor, fg="white")
        self.money.grid(row=4, column=0)
        self.money.config(font=("Courier", 20))
        self.enter = Entry(self.frame)
        self.enter.config(font=("Courier", 15))
        self.enter.grid(row=4, column=1)
        self.enter_bet = Button(self.frame, text="Enter Bet", command=self.bet, bg="Gray", fg="Black")
        self.enter_bet.grid(row=4, column=2, sticky="")

        self.holdbutton = Button(self.frame, text="hold", command=self.showhands, width=10, bg="purple", fg="white")
        self.holdbutton.grid(row=4, column=7)

    def bet(self):
        money = int(self.enter.get())
        if money < play.money:
            play.bet(money, blackjack_game)
            self.label.config(text="Bet " + str(money))
        else:
            self.label.config(text="Not enough money")

    def dohit(self):
        play.hit(blackjack_game)

    def redo(self):
        cards.append(removed)
        removed.clear()
        for i in range(9):
            r = "green.png"
            self.middle[i].image = ImageTk.PhotoImage(Image.open(r))
            self.middle[i].create_image(55, 0, image=self.middle[i].image, anchor="nw")
            self.dealer[i].image = ImageTk.PhotoImage(Image.open(r))
            self.dealer[i].create_image(55, 0, image=self.dealer[i].image, anchor="nw")
            self.player[i].image = ImageTk.PhotoImage(Image.open(r))
            self.player[i].create_image(55, 0, image=self.player[i].image, anchor="nw")
        self.continuebtn.destroy()
        blackjack_game.hitbutton = Button(blackjack_game.frame, text="hit", command=blackjack_game.dohit, width=10, bg="purple", fg="white")
        blackjack_game.hitbutton.grid(row=4, column=6)
        self.holdbutton = Button(self.frame, text="hold", command=self.showhands, width=10, bg="purple", fg="white")
        self.holdbutton.grid(row=4, column=7)
        self.label.config(text="")
        play.hand.clear()
        dea.hand.clear()
        for i in range(2):
            dea.hit(blackjack_game, 1)
            play.hit(blackjack_game)

    def showhands(self):
        dea.show_hand(blackjack_game, 2)
        play.show_hand(blackjack_game)
        if play.getvalue() < 22:
            if dea.getvalue() > play.getvalue() and dea.getvalue() < 22:
                self.label.config(text="You lost, further to 21 than the dealer!")
                self.hitbutton.destroy()
                self.holdbutton.destroy()
            elif dea.getvalue() == play.getvalue():
                self.label.config(text="A tie! You get a refund")
                play.money += play.betnum
                self.hitbutton.destroy()
                self.holdbutton.destroy()
            elif dea.getvalue() < 22:
                if play.getvalue() == 21:
                    self.label.config(text="Blackjack! Congrats!")
                    play.money += play.betnum + (play.betnum*(3/2))
                    self.hitbutton.destroy()
                    self.holdbutton.destroy()
                else:
                    self.label.config(text="You won! You were closer to 21 than the dealer")
                    play.money += play.betnum + play.betnum
                    self.hitbutton.destroy()
                    self.holdbutton.destroy()
            else:
                if play.getvalue() == 21:
                    self.label.config(text="Blackjack! Congrats!")
                    play.money += play.betnum + (play.betnum*(3/2))
                    self.hitbutton.destroy()
                    self.holdbutton.destroy()
                else:
                    self.label.config(text="You won! Dealer busted!")
                    play.money += play.betnum + (play.betnum)
                    self.hitbutton.destroy()
                    self.holdbutton.destroy()
        if play.getvalue() > 21:
            if dea.getvalue() > 21:
                self.label.config(text="A tie! You both busted!")
                play.money += play.betnum
                self.hitbutton.destroy()
                self.holdbutton.destroy()
            else:
                self.label.config(text="You busted! Dealer wins! :(")
                self.hitbutton.destroy()
                self.holdbutton.destroy()
        self.money.config(text="Money: " + str(play.money))

        self.continuebtn = Button(self.frame, text="continue?", command=self.redo, width=20, bg="yellow", fg="black")
        self.continuebtn.grid(row=1, column=2, columnspan=5)

    def lost(self):
        self.label.config(text="you busted, don't try hitting again")


window = Tk(screenName="BlackJack")
blackjack_game = GUI(window)


for i in range(2):
    dea.hit(blackjack_game, 1)
    print(dea.hand)

play.hit(blackjack_game)
play.hit(blackjack_game)

blackjack_game.hitbutton = Button(blackjack_game.frame, text="hit", command=blackjack_game.dohit, width=10, bg="purple", fg="white")
blackjack_game.hitbutton.grid(row=4, column=6)

window.mainloop()

# Next steps: that image.open instead of counter we rename the cards to match the cards in python, and then simply make it call using that.
# actual dealing of cards (create dealer and player)

#make the amount of money at end of round be return. Make if bet = "exit" while loop is closed