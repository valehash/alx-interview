#!/usr/bin/python3
"""script to run a prime number game"""


def is_prime(n:int)->bool:
    """Function that checks if a number is prime or not"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_game(n:int)->int:
    """runs a single instance of the game"""
    numbers = set(range(1, n + 1))
    current_player = 0  # 0 for Maria, 1 for Ben

    while numbers:
        move_made = False
        for num in range(2, n + 1):
            if num in numbers and is_prime(num):
                # Remove num and its multiples
                numbers -= set(range(num, n + 1, num))
                move_made = True
                break
        
        if not move_made:
            return 1 - current_player  # Return the other player as winner
        
        current_player = 1 - current_player

    return 1 - current_player  # This line should never be reached, but just in case

def isWinner(x:int, nums)->str:
    """defines which player won the game"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
