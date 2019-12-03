import random
import os
from tkinter import *
from PIL import ImageTk, Image

cards = ["d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da","s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa","h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha","c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"]
removed = []


class DHand(object):

    def __init__(self):
        self.hand = []

    def hit(self, GUI, type):
        chosen = random.choice(cards)
        self.hand.append(chosen)
        cards.remove(chosen)
        removed.append(chosen)
        self.show_hand(GUI, type)

    def getvalue(self):
        TotalVal = 0
        ace = False
        for c in self.hand:
            if c[1] == "j" or c[1] == "q" or c[1] == "k" or c[1] == "1":
                val = 10
            elif c[1] == "a":
                ace = True
                val = 11
            else:
                val = int(c[1])
            TotalVal += val
        if TotalVal > 21 and ace:
            TotalVal -= 10
        return TotalVal

    def hide_hand(self, GUI):
        for c in self.hand:
            for cc in os.listdir("Cards"):
                if self.hand.index(c)<1:
                    if c[0] == cc[0] and c[1] == cc[-5]:
                        r = "Cards/" + cc
                        index = self.hand.index(c)
                        GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                        GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")
                else:
                    r = "Cards/" + "back.png"
                    index = self.hand.index(c)
                    GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                    GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")

    def show_hand(self, GUI, type):
        if self.getvalue()<17:
            if type == 2:
                self.hit(GUI, 2)
            for c in self.hand:
                for cc in os.listdir("Cards"):
                    if self.hand.index(c) < 1 or type == 2:
                        if c[0] == cc[0] and c[1] == cc[1]:
                            r = "Cards/" + cc
                            index = self.hand.index(c)
                            GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                            GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")
                    else:
                        r = "Cards/" + "back.png"
                        index = self.hand.index(c)
                        GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                        GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")
        else:
            for c in self.hand:
                for cc in os.listdir("Cards"):
                    if self.hand.index(c) < 1 or type == 2:
                        if c[0] == cc[0] and c[1] == cc[1]:
                            r = "Cards/" + cc
                            index = self.hand.index(c)
                            GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                            GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")
                    else:
                        r = "Cards/" + "back.png"
                        index = self.hand.index(c)
                        GUI.dealer[index].image = ImageTk.PhotoImage(Image.open(r))
                        GUI.dealer[index].create_image(0, 35, image=GUI.dealer[index].image, anchor="nw")