import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_twopair(self):
        for i in range(5):
            for j in range(i+1, 5):
                 if self.cards[i].get_rank() == self.cards[j].get_rank():
                    self.cards.pop[i]
                    self.cards.pop[j]
                    for v in range(3):
                        for b in range(v+1, 3):
                            if self.cards[v].get_rank() == self.cards[b].get_rank():
                            return True

    def is_fourofakind(self):
        for i in range(5):
            for j in range(i+1, 5):
                for v in range(j+2, 5):
                    for b in range(v+3, 5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() and self.cards[i].get_rank() == self.cards[v].get_rank() and self.cards[i].get_rank() == self.cards[b].get_rank():
                            return True

    def is_flush(self):
        for i in range(5):
            for j in range(i+1, 5):
                for v in range(j+2, 5):
                    for b in range(v+3, 5):
                        for n in range(b+4, 5)
                        if self.cards[i].get_suit() == self.cards[j].get_suit() and self.cards[i].get_suit() == self.cards[v].get_suit() and self.cards[i].get_suit() == self.cards[b].get_suit() and  self.cards[i].get_suit() == self.cards[n].get_suit():
                            return True



new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)
