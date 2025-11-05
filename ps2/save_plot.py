import os
from typing import List

import matplotlib.pyplot as plt


# Save and plot results
def save_plot(
    player1_strategy_name: str,
    player2_strategy_name: str,
    player1_moves: List[int],
    player2_moves: List[int],
    player1_payoff: int,
    player2_payoff: int,
    save_dir: str,
) -> None:
    """
    Save plot for each game.

    :param player1_strategy_name: The name of the player 1 strategy.
    :param player2_strategy_name: The name of the player 2 strategy.
    :param player1_moves: The moves played in the first player.
    :param player2_moves: The moves played in the second player.
    :param player1_payoff: The payoff of the first player.
    :param player2_payoff: The payoff of the second player.
    :param save_dir: The directory to save the plot to.
    :return: None
    """
    rounds = range(1, len(player1_moves) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(rounds, player1_moves, "go-", label=player1_strategy_name)
    plt.plot(rounds, player2_moves, "bo-", label=player2_strategy_name)

    plt.title(f"Moves over Time: {player1_strategy_name} vs {player2_strategy_name}")
    plt.xlabel("Round")
    plt.ylabel("Move (Cooperate = 1, Defect = 0)")
    plt.legend()
    plt.grid(True)

    # Save the plot to the specified directory
    plot_filename = f"{player1_strategy_name}_vs_{player2_strategy_name}.png"
    plot_path = os.path.join(save_dir, plot_filename)
    plt.savefig(plot_path)
    plt.close()  # Close the plot to avoid displaying it in Jupyter

    return None
