from random import random
def shuffle(cards):
    for i in range(1000):
        x,y=int(random()*52),int(random()*52)
        cards[x],cards[y]=cards[y],cards[x]
def main():
    cards= [i for i in range(52)]
    shuffle(cards)
    print(cards)
if __name__ == "__main__" :
    main()