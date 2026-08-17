"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number: The current round number.

    Returns:
        The current round number and the two that follow.
    """
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1: The first rounds played.
        rounds_2: The second group of rounds played.

    Returns:
        All rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds: The rounds played.
        number: The round number.

    Returns:
        Was the round played?
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and returns the average card value from the list.

    Parameters:
        hand: The cards in the hand.

    Returns:
        The average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Compare the average of first and last card with middle card

    Parameters:
        hand: The cards in the hand.

    Returns:
        Does one of the approximate averages equal the `true average`?
    """
    average = card_average(hand)
    op1 = (hand[0] + hand[-1]) / 2
    op2 = hand[len(hand) // 2]
    return average in (op1, op2)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Compare the average of even and odd indexes

    Parameters:
        hand: The cards in the hand.

    Returns:
        Are the even and odd averages equal?
    """
    return card_average(hand[0::2]) == card_average(hand[1::2])


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand: The cards in the hand.

    Returns:
        The hand with Jacks (if present and last) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
