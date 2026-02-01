import random 
from typing import Tuple
def monty_hall_game (switch_door: bool) -> bool:
    """monty_hall_game simulates a single round of the Monty Hall game.
    the player can choose to switch their initial door choice or not.
    """
    doors = ['car','goat','goat']
    random.shuffle(doors)

    initial_choice=random.choice(range(len(doors)))

    doors_revealed = [i for i in range(len(doors)) if i != initial_choice and doors[i] != 'car' ]
    door_revealed = random.choice(doors_revealed)
    
    if switch_door:
        final_choice = [i for i in range(len(doors)) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'

def simulate_monty_hall(number_of_game: int) -> tuple[float, float]:
    
    num_win_without_switch = sum(monty_hall_game(False) for _ in range(number_of_game))
    num_win_with_switch = sum(monty_hall_game(True) for _ in range(number_of_game))
    return num_win_without_switch/number_of_game, num_win_with_switch/number_of_game

if __name__ == "__main__":
    w = simulate_monty_hall(1000)
    print("Win rate without switching:", w[0], " Win rate with switching:", w[1])
