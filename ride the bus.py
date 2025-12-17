import random

# Card ranks and suits
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
SUIT_COLORS = {'Hearts': 'red', 'Diamonds': 'red', 'Clubs': 'black', 'Spades': 'black'}

# Map ranks to numeric values for comparisons
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}

def create_deck():
    """Create and shuffle a standard 52-card deck."""
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    """Draw a card from the deck."""
    if not deck:
        deck.extend(create_deck())  # Reshuffle if deck is empty
    return deck.pop()

def card_str(card):
    """Return a human-readable card string."""
    return f"{card[0]} of {card[1]}"

def ride_the_bus():
    deck = create_deck()
    stage = 1
    cards_drawn = []

    print("Welcome to Ride the Bus! Complete all 4 stages to win.\n")

    while stage <= 4:
        if stage == 1:
            # Stage 1: Red or Black
            guess = input("Stage 1 - Red or Black? ").strip().lower()
            card = draw_card(deck)
            cards_drawn = [card]
            print(f"Card drawn: {card_str(card)}")
            if guess == SUIT_COLORS[card[1]]:
                print("Correct!\n")
                stage += 1
            else:
                print("Wrong! Back to Stage 1.\n")
                stage = 1

        elif stage == 2:
            # Stage 2: Higher or Lower
            guess = input("Stage 2 - Higher or Lower? ").strip().lower()
            card = draw_card(deck)
            cards_drawn.append(card)
            print(f"Card drawn: {card_str(card)}")
            prev_value = RANK_VALUES[cards_drawn[0][0]]
            curr_value = RANK_VALUES[card[0]]
            if (guess == "higher" and curr_value > prev_value) or \
               (guess == "lower" and curr_value < prev_value):
                print("Correct!\n")
                stage += 1
            else:
                print("Wrong! Back to Stage 1.\n")
                stage = 1

        elif stage == 3:
            # Stage 3: In Between or Outside
            guess = input("Stage 3 - In Between or Outside? ").strip().lower()
            card = draw_card(deck)
            cards_drawn.append(card)
            print(f"Card drawn: {card_str(card)}")
            values = sorted([RANK_VALUES[c[0]] for c in cards_drawn[:2]])
            curr_value = RANK_VALUES[card[0]]
            in_between = values[0] < curr_value < values[1]
            if (guess == "in between" and in_between) or \
               (guess == "outside" and not in_between):
                print("Correct!\n")
                stage += 1
            else:
                print("Wrong! Back to Stage 1.\n")
                stage = 1

        elif stage == 4:
            # Stage 4: Suit Guess
            guess = input("Stage 4 - Guess the Suit (Hearts/Diamonds/Clubs/Spades): ").strip().capitalize()
            card = draw_card(deck)
            cards_drawn.append(card)
            print(f"Card drawn: {card_str(card)}")
            if guess == card[1]:
                print("  you have offically won and you very lucky \n")
                break
            else:
                print("Wrong! Back to Stage 1.\n")
                stage = 1

if __name__ == "__main__":
    try:
        ride_the_bus()
    except KeyboardInterrupt:
        print("\nGame exited.")

