import random
import os
from tkinter import *
from PIL import ImageTk, Image

cards = ["d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da","s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa","h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha","c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"]
values = [1,2,3,4,5,6,7,8,9,10,11]
removed = []


class Hand(object):

    def __init__(self):
        self.hand = []
        self.money = 100
        self.betnum = 0

    def hit(self, GUI):
        chosen = random.choice(cards)
        self.hand.append(chosen)
        cards.remove(chosen)
        removed.append(chosen)
        self.show_hand(GUI)
        if self.getvalue() > 21:
            GUI.label.config(text="You busted")
            GUI.hitbutton.destroy()
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

    def show_hand(self,GUI):
        for d in self.hand:
            for cc in os.listdir("Cards"):
                if d[0] == cc[0] and d[1] == cc[1]:
                    g = "Cards/" + cc
                    index2 = self.hand.index(d)
                    GUI.player[index2].image = ImageTk.PhotoImage(Image.open(g))
                    GUI.player[index2].create_image(0, 35, image=GUI.player[index2].image, anchor="nw")

    def bet(self, amount, GUI):
        self.money -= amount
        self.betnum = amount
        GUI.money.config(text="Money: "+str(self.money))
        index=0
        while amount!=0:
            if amount>=100:
                GUI.middle.insert(index, Canvas(master=GUI.hang_frame, width=30, height=30, bg="green", highlightthickness=0))
                GUI.middle[index].grid(row=1, column=index)
                r = "Chips/100.png"
                GUI.middle[index].image = ImageTk.PhotoImage(Image.open(r))
                GUI.middle[index].create_image(0, 0, image=GUI.middle[index].image, anchor="nw")
                amount-=100
                index += 1
            elif amount>=25:
                GUI.middle.append(Canvas(master=GUI.hang_frame, width=30, height=30, bg="green", highlightthickness=0))
                GUI.middle[index].grid(row=1, column=index)
                print(GUI.middle[index], str(index))
                r = "Chips/25.png"
                GUI.middle[index].image = ImageTk.PhotoImage(Image.open(r))
                GUI.middle[index].create_image(0, 0, image=GUI.middle[index].image, anchor="nw")
                amount-=25
                index+=1
            elif amount>=5:
                GUI.middle.insert(index, Canvas(master=GUI.hang_frame, width=30, height=30, bg="green", highlightthickness=0))
                GUI.middle[index].grid(row=1, column=index)
                r = "Chips/6.png"
                GUI.middle[index].image = ImageTk.PhotoImage(Image.open(r))
                GUI.middle[index].create_image(0, 0, image=GUI.middle[index].image, anchor="nw")
                amount -= 5
                index += 1
            elif amount>=1:
                GUI.middle.insert(index, Canvas(master=GUI.hang_frame, width=30, height=30, bg="green", highlightthickness=0))
                GUI.middle[index].grid(row=1, column=index)
                r = "Chips/2.png"
                GUI.middle[index].image = ImageTk.PhotoImage(Image.open(r))
                GUI.middle[index].create_image(0, 0, image=GUI.middle[index].image, anchor="nw")
                amount -= 1
                index += 1