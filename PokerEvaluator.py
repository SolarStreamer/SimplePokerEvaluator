from collections import Counter

RANKS = "23456789TJQKA"
SUITS = "CDHS"

def card_value(card):
    return RANKS.index(card[0])

def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_straight(hand):
    values = sorted([card_value(card) for card in hand])
    return values == list(range(values[0], values[0] + 5)) or values == [0, 1, 2, 3, 12]  # Handle A-2-3-4-5

def classify_hand(hand):
    values = [card[0] for card in hand]
    counts = Counter(values)
    count_values = sorted(counts.values(), reverse=True)
    flush = is_flush(hand)
    straight = is_straight(hand)

    if flush and straight:
        if sorted([card_value(card) for card in hand]) == [8, 9, 10, 11, 12]:
            return "Royal Flush"
        return "Straight Flush"
    elif count_values == [4, 1]:
        return "Four of a Kind"
    elif count_values == [3, 2]:
        return "Full House"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif count_values == [3, 1, 1]:
        return "Three of a Kind"
    elif count_values == [2, 2, 1]:
        return "Two Pair"
    elif count_values == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"

# Example usage:
hand = ['AH', 'KH', 'QH', 'JH', 'TH']  # Royal Flush
print("Hand:", hand)
print("Classification:", classify_hand(hand))

