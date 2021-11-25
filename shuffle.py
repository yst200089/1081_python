import random
def main():
    cards= [i for i in range(52)]
    random.shuffle(cards)
    print(cards)
if __name__ == "__main__" :
    main()