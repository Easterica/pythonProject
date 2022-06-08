deck_of_cards = input().split()
count_of_shuffles = int(input())

left_side_of_deck = list()
right_side_of_deck = list()
middle = len(deck_of_cards) // 2
shuffled_deck = list()


for _ in range(count_of_shuffles):
    for i in range(middle):
        left_side_of_deck.append(deck_of_cards[i])
    for i in range(middle, len(deck_of_cards)):
        right_side_of_deck.append(deck_of_cards[i])
    for i in range(middle):
        shuffled_deck.append(left_side_of_deck[i])
        shuffled_deck.append(right_side_of_deck[i])
    deck_of_cards = shuffled_deck
    shuffled_deck = list()
    left_side_of_deck = list()
    right_side_of_deck = list()

print(deck_of_cards)