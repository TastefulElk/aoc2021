from functools import cache
from itertools import product
from src.utility.file import read_lines


def get_starting_positions(input_data) -> list[int]:
    ret = []
    for line in input_data:
        _, pos = line.split(": ")
        ret.append(int(pos))
    return ret


def get_new_position(current_position, dice_roll):
    def roll_dice(last_dice_roll):
        return last_dice_roll + 1 + last_dice_roll + 2 + last_dice_roll + 3

    new_pos = (current_position + roll_dice(dice_roll)) % 10
    if new_pos == 0:
        return 10
    return new_pos


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    p1_position, p2_position = get_starting_positions(input_data)
    p1_score = p2_score = 0

    last_dice_roll = 0
    dice_rolls = 0
    while p1_score < 1000 and p2_score < 1000:
        if dice_rolls % 2 == 0:
            p1_position = get_new_position(p1_position, last_dice_roll)
            p1_score += p1_position
        else:
            p2_position = get_new_position(p2_position, last_dice_roll)
            p2_score += p2_position

        last_dice_roll += 3
        dice_rolls += 3

    return p1_score * dice_rolls if p1_score < p2_score else p2_score * dice_rolls


quantum_sides = [1, 2, 3]
quantum_rolls = [sum(x) for x in product(quantum_sides, quantum_sides, quantum_sides)]


@cache
def play_quantum_turn(current_player_pos, current_player_score, other_player_pos, other_player_score):
    """
    Recursively calculate the number of wins for each player
    for each possible quantum roll

    the turn result is cached since the outcome is deterministic
    for a given game state
    """
    current_player_wins = other_player_wins = 0
    for quantum_roll in quantum_rolls:
        new_pos = (current_player_pos + quantum_roll) % 10
        if new_pos == 0:
            new_pos = 10
        new_score = current_player_score + new_pos

        # if score is 21 or higher, the player wins and the game is done
        if new_score >= 21:
            current_player_wins += 1
        # else, the game we let the other player play a turn and summarize
        # all the winning outcomes from that
        else:
            new_other_player_wins, new_current_player_wins = play_quantum_turn(other_player_pos, other_player_score, new_pos, new_score)
            current_player_wins += new_current_player_wins
            other_player_wins += new_other_player_wins

    return current_player_wins, other_player_wins


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    p1_start, p2_start = get_starting_positions(input_data)

    wins = play_quantum_turn(p1_start, 0, p2_start, 0)
    return max(wins)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_21/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
