"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
from typing import Union


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if card in {"J", "Q", "K"}:
        return 10
    if card == "A":
        return 1
    return int(card)
    # Alternative suggestion that is optimized to be a one-liner
    # return int({"A": 1, "K": 10, "Q": 10, "J": 10}.get(card, card))


def higher_card(card_one: str, card_two: str) -> Union[str, tuple[str, str]]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    card_one_value, card_two_value = value_of_card(card_one), value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    if card_two_value > card_one_value:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    def card_value_in_hand(card: str) -> int:
        return value_of_card(card) if card != "A" else 11

    hand_value = card_value_in_hand(card_one) + card_value_in_hand(card_two)
    return 1 if (21 - hand_value) < 11 else 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    hand = {card_one, card_two}
    return ("A" in hand) and (len({"J", "Q", "K", "10"}.intersection(hand)) == 1)


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11
