""" Exercise Two tea party COMP 110 HW """

__author__: str = "730621803"


def contains_char(search_string: str, search_char: str) -> bool:

    assert len(search_char) == 1, f"len('{search_char}') is not 1"

    index = 0
    while index < len(search_string):
        if search_string[index] == search_char:
            return True
        index += 1

    return False


def emojified(guess: str, secret: str) -> str:

    assert len(guess) == len(secret), "Guess must be the same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_result = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        index += 1

    return emoji_result


def input_guess(expected_length: int) -> str:
    """Function that askes participants for a guess of the expected length and
    keeps asking until it is valid."""

    guess = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def main(secret: str) -> None:
    """The main part of the game loop, we entry right here"""
    turn = 1
    max_turns = 6
    won = False

    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(len(secret))
        result = emojified(guess, secret)
        print(result)

        if guess == secret:
            won = True
            print(f"You won in {turn}/6 turns!")

        turn += 1

    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
