from cardgame import Deck
'''
単純なブラックジャックのようなゲームです。
ディーラーのドローは最初の二枚のみ、エースは1のみとして扱います。
自分の手札の合計がディーラーの手札の合計より数字が大きく、かつ21を超えなければ勝利です。
standすればディーラーと勝負、しなければ1枚ドローします。
21を超えてしまうとバースト扱いとなり敗北です。
'''
def judge(cards, d_cards):
    print("Dealer cards :", end="")
    for d_card in d_cards:
        print(d_card, end=",")
    print("\nDealer sum :{}".format(sum(d_cards)))
    win() if sum(cards) > sum(d_cards) else lose()

def win():
    print("You win!")
    exit()

def lose():
    print("You lose.")
    exit()

def main():
    deck = Deck.Deck()
    deck.shuffle()
    dealer_cards = []
    dealer_cards += deck.draw(num=2, num_inspect=True)
    cards = []
    cards += deck.draw(num=2, num_inspect=True)

    stand = False
    while stand == False:
        print("Your cards :", end="")
        for card in cards:
            print(card, end=",")
        print("\nYour sum :{}".format(sum(cards)))
        if sum(cards) > 21:
            print("You busted!")
            lose()

        print("Dealer cards :", end="")
        for idx, d_card in enumerate(dealer_cards):
            print(d_card, end=",") if idx == 0 else print('?', end=",")

        stand = True if input("\nStand? [y/n]:") == "y" else False

        cards += deck.draw(num=1, num_inspect=True)

    judge(cards, dealer_cards)


if __name__ == '__main__':
    main()