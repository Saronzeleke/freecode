import random
import matplotlib.pyplot as plt

# Determines winner of Rock, Paper, Scissors
def rps_result(player_move, opponent_move):
    if player_move == opponent_move:
        return "Ties"
    elif (player_move == "R" and opponent_move == "S") or \
         (player_move == "S" and opponent_move == "P") or \
         (player_move == "P" and opponent_move == "R"):
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

# Simulates a match between two players
def play(player1, player2, num_games=1000):
    results = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Ties": 0}
    
    for _ in range(num_games):
        move1 = player1()
        move2 = player2()
        result = rps_result(move1, move2)
        results[result] += 1
        
    return results

# AI Strategy (Example: Always plays Rock)
def player():
    return "R"

# Opponent: Random choice bot
def random_bot():
    return random.choice(["R", "P", "S"])

# Run the match
results = play(player, random_bot, 1000)

# Visualization
plt.bar(results.keys(), results.values(), color=['green', 'red', 'gray'])
plt.title("Match Results")
plt.ylabel("Number of Games")
plt.xlabel("Outcome")
plt.show()
