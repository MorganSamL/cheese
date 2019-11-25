import random
from tkinter import *

from PIL import ImageTk, Image

cards = ["d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da","s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa","h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha","c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"]
values = [1,2,3,4,5,6,7,8,9,10,11]
removed = []

class Hand(object):

    def __init__(self):
        self.hand = []

    def hit (self):
        chosen = random.choice(cards)
        self.hand.append(chosen)
        cards.remove(chosen)
        removed.append(chosen)

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
            TotalVal-10
        return TotalVal

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
        for i in range(9):
            self.dealer.append(Canvas(master=self.hang_frame, width=140, height=310, bg="green", highlightthickness=0))
            self.dealer[i].grid(row=0, column=i)
        for i in range(9):
            self.player.append(Canvas(master=self.hang_frame, width=140, height=310, bg="green", highlightthickness=0))
            self.player[i].grid(row=1, column=i)

        self.hang_frame.grid(row=2, padx=5, pady=80)
        self.player[0].image = ImageTk.PhotoImage(Image.open("2D.png"))
        self.player[0].create_image(0,50,image=self.player[0].image,anchor="nw")

window = Tk(screenName="BlackJack")
blackjack_game = GUI(window)
window.mainloop()

#Next steps: that image.open instead of counter we rename the cards to match the cards in python, and then simply make it call using that.
# actual dealing of cards (create dealer and player)






