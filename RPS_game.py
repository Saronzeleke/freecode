import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from RPS_game import play, quincy, kris, abbey, random_player
from RPS import player  # Your AI bot

def run_game_and_visualize(opponent, num_games=1000):
    results = {'Player 1 Wins': 0, 'Player 2 Wins': 0, 'Ties': 0}
    moves = {'R': 0, 'P': 0, 'S': 0}  # Track move choices
    history = []
    
    def track_results(p1_move, p2_move, result):
        if result == 1:
            results['Player 1 Wins'] += 1
        elif result == -1:
            results['Player 2 Wins'] += 1
        else:
            results['Ties'] += 1
        history.append(results['Player 1 Wins'] / len(history) if history else 0)
        moves[p1_move] += 1
    
    play(player, opponent, num_games, callback=track_results)
    
    # Visualization
    fig, ax = plt.subplots(1, 3, figsize=(18, 5))
    
    # Win Percentage Bar Chart
    ax[0].bar(results.keys(), results.values(), color=['green', 'red', 'gray'])
    ax[0].set_title("Win Distribution")
    
    # Win Rate Over Time
    ax[1].plot(history, label='Win Rate', color='blue')
    ax[1].set_title("Win Rate Over Time")
    ax[1].set_xlabel("Games")
    ax[1].set_ylabel("Win %")
    
    # Move Distribution
    ax[2].bar(moves.keys(), moves.values(), color=['blue', 'orange', 'purple'])
    ax[2].set_title("Move Distribution")
    
    plt.show()
    
    print(f"Player 1 Wins: {results['Player 1 Wins'] / num_games * 100:.2f}%")
    print(f"Player 2 Wins: {results['Player 2 Wins'] / num_games * 100:.2f}%")
    print(f"Ties: {results['Ties'] / num_games * 100:.2f}%")
    
# Run visualization against an opponent
run_game_and_visualize(quincy, 1000)
