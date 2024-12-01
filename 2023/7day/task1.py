from enum import IntEnum
from collections import Counter

_input = open("in.txt", "rt").read()


class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Combo(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH = 0


class Hand:
    def __init__(self, cards: list[Card], bid: int) -> None:
        self.cards = cards
        self.bid = bid
        self.combo = self.get_highest_combo()

    def get_highest_combo(t) -> Combo:
        unique = Counter(t.cards)
        if len(unique) == 1:
            return Combo.FIVE_OF_A_KIND

        counted = sorted(unique.values())
        if len(unique) == 2:
            return Combo.FULL_HOUSE if counted == [2, 3] else Combo.FOUR_OF_A_KIND
        if len(unique) == 3:
            return Combo.TWO_PAIR if counted == [1, 2, 2] else Combo.THREE_OF_A_KIND
        if len(unique) == 4:
            return Combo.PAIR

        return Combo.HIGH

    @staticmethod
    def from_str(s: str) -> "Hand":
        char_to_card = {
            "2": Card.TWO,
            "3": Card.THREE,
            "4": Card.FOUR,
            "5": Card.FIVE,
            "6": Card.SIX,
            "7": Card.SEVEN,
            "8": Card.EIGHT,
            "9": Card.NINE,
            "T": Card.T,
            "J": Card.J,
            "Q": Card.Q,
            "K": Card.K,
            "A": Card.A,
        }
        cards_str, bid = s.split(" ")
        cards = [char_to_card[x] for x in cards_str]
        return Hand(cards, int(bid))

    def __lt__(t, o: "Hand") -> bool:
        if t.combo != o.combo:
            return t.combo < o.combo

        for t_card, o_card in zip(t.cards, o.cards):
            if t_card != o_card:
                return t_card < o_card

    def __repr__(t) -> str:
        empty = " "
        return f"< cards = {empty.join(x.name for x in t.cards)}, bid = {t.bid} >"


hands = sorted(Hand.from_str(l) for l in _input.split("\n"))
res = 0
for idx, hand in enumerate(hands, 1):
    res += idx * hand.bid

print(res)
