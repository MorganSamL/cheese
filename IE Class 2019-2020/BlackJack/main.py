import random
import os
from tkinter import *
import time

from PIL import ImageTk, Image

cards = ["d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da","s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa","h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha","c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"]
values = [1,2,3,4,5,6,7,8,9,10,11]
removed = []



class Hand(object):

    def __init__(self):
        self.hand = []

    def hit(self, GUI, type):
        chosen = random.choice(cards)
        self.hand.append(chosen)
        cards.remove(chosen)
        removed.append(chosen)
        GUI.showplay()
        print(self.hand)
        if type ==1:
            if self.getvalue()==21:
                GUI.label.config(text="BLACKJACK!")
                blackjack_game.hitbutton.destroy()
                GUI.showhands()
            if self.getvalue() > 21:
                GUI.label.config(text="You busted")
                blackjack_game.hitbutton.destroy()
                GUI.showhands()

    def getvalue (self):
        TotalVal =0
        ace = False
        for c in self.hand:
            if c[1]=="j" or c[1]=="q" or c[1]=="k" or c[1]=="1":
                val=10
            elif c[1]=="a":
                ace = True
                val = 11
            else:
                val = int(c[1])
            TotalVal += val
        if TotalVal > 21 and ace:
            TotalVal -=10
        return TotalVal



dea = Hand()
play = Hand()

#stand method will just be continue (doing it in the gui)
#make player class after sure initial blackjack works

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
        self.text = []

        for i in range(9):
            self.dealer.append(Canvas(master=self.hang_frame, width=140, height=310, bg="green", highlightthickness=0))
            self.dealer[i].grid(row=0, column=i)

        self.text.append(Canvas(master=self.hang_frame, width=140, height=40, bg="green", highlightthickness=0))
        self.label = Label(self.frame, text="", bg = "green", fg = "Black")
        self.label.grid(row = 1, column= 0, columnspan=9)

        for i in range(9):
            self.player.append(Canvas(master=self.hang_frame, width=140, height=310, bg="green", highlightthickness=0))
            self.player[i].grid(row=2, column=i)

        self.hang_frame.grid(row=3, padx=5, pady=20, columnspan=3)

        self.holdbutton = Button(self.frame, text="hold", command= self.showhands, bg="black", fg="Purple")
        self.holdbutton.grid(row=4, column=2)

    def dohit(self):
        play.hit(blackjack_game, 1)

    def hidden(self):
        if dea.getvalue()<17:
            dea.hit(blackjack_game, 2)
            for c in dea.hand:
                for cc in os.listdir("52cards"):
                    if dea.hand.index(c)<1:
                        if c[0].upper() == cc[-5] and c[1] == cc[0] or c[0].upper() == cc[-5] and c[1].upper() == cc[0]:
                            r = "52cards/" + cc
                            index = dea.hand.index(c)
                            self.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                            self.dealer[index].create_image(0, 50, image=self.dealer[index].image, anchor="nw")
                    else:
                        r = "52cards/" + "gray_back.png"
                        index = dea.hand.index(c)
                        self.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                        self.dealer[index].create_image(0, 50, image=self.dealer[index].image, anchor="nw")

    def showhands(self):
        for d in play.hand:
            for cc in os.listdir("52cards"):
                if d[0].upper() == cc[-5] and d[1] == cc[0] or d[0].upper() == cc[-5] and d[1].upper() == cc[0]:
                    g = "52cards/" + cc
                    index2 = play.hand.index(d)
                    self.player[index2].image = ImageTk.PhotoImage(Image.open(g))
                    self.player[index2].create_image(0, 50, image=self.player[index2].image, anchor="nw")

        for i in range(6):
            blackjack_game.hidden()
        for c in dea.hand:
            for cc in os.listdir("52cards"):
                if c[0].upper() == cc[-5] and c[1] == cc[0] or c[0].upper() == cc[-5] and c[1].upper() == cc[0]:
                    r = "52cards/" + cc
                    index = dea.hand.index(c)
                    self.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                    self.dealer[index].create_image(0, 50, image=self.dealer[index].image, anchor="nw")
        if play.getvalue()<22:
            if dea.getvalue()>play.getvalue() and dea.getvalue()<22:
                self.label.config(text="You lost, further to 21 than the dealer!")
                self.holdbutton.destroy()
            elif dea.getvalue()==play.getvalue():
                self.label.config(text="It's a tie!")
                self.holdbutton.destroy()
            elif dea.getvalue()<22:
                self.label.config(text="You won! You were closer to 21 than the dealer")
                self.holdbutton.destroy()
            else:
                self.label.config(text="You won! Dealer busted!")
                self.holdbutton.destroy()
        if play.getvalue()>21:
            if dea.getvalue()>21:
                self.label.config(text="A tie! You both busted!")
                self.holdbutton.destroy()
            else:
                self.label.config(text="You busted! Dealer wins! :(")
                self.holdbutton.destroy()

    def showplay(self):
        for d in play.hand:
            for cc in os.listdir("52cards"):
                if d[0].upper() == cc[-5] and d[1] == cc[0] or d[0].upper() == cc[-5] and d[1].upper() == cc[0]:
                    g = "52cards/" + cc
                    index2 = play.hand.index(d)
                    self.player[index2].image = ImageTk.PhotoImage(Image.open(g))
                    self.player[index2].create_image(0, 50, image=self.player[index2].image, anchor="nw")
    def lost(self):
        self.label.config(text="you busted, don't try hitting again")

window = Tk(screenName="BlackJack")
blackjack_game = GUI(window)

for i in range(2):
    blackjack_game.hidden()



play.hit(blackjack_game, 1)
play.hit(blackjack_game, 1)

blackjack_game.hitbutton = Button(blackjack_game.frame, text="hit", command=blackjack_game.dohit, bg="black", fg="Purple")
blackjack_game.hitbutton.grid(row=4, column=0)

window.mainloop()

#Next steps: that image.open instead of counter we rename the cards to match the cards in python, and then simply make it call using that.
# actual dealing of cards (create dealer and player)






