from typing import List

import numpy as np


# define the strategies
def tit_for_tat(opponent_history: List[str]) -> str:
    """
    Tit-for-tat strategy: Cooperate initially, then mimic the opponent's previous move.

    :param opponent_history: history of the opponent
    :return: "C" for cooperation, "D" for defect
    """
    # cooperate first
    if not opponent_history:
        return "C"

    # mimic opponent's last move
    return opponent_history[-1]


def grim_trigger(opponent_history: List[str]) -> str:
    """
    Grim-trigger strategy: Cooperate until the opponent defects, then always defect after that.

    :param opponent_history: history of the opponent
    :return: "C" for cooperation, "D" for defect
    """
    # defect after any defection
    if "D" in opponent_history:
        return "D"

    # cooperate until the opponent defects
    return "C"


def always_cooperate(opponent_history: List[str]) -> str:
    """
    Cooperate.

    :param opponent_history: history of the opponent
    :return: "C" for cooperation
    """
    # always cooperate
    return "C"


def always_defect(opponent_history: List[str]) -> str:
    """
    Defect.

    :param opponent_history: history of the opponent
    :return: "D" for defect
    """
    # always defect
    return "D"


def probabilistic_strategy(opponent_history: List[str], p: float, seed: int = None) -> str:
    """
    Cooperate with some probability.

    :param opponent_history: history of the opponent
    :param p: probability
    :param seed: random seed for reproducibility
    :return: "C" for cooperation, "D" for defect
    """
    # set the seed for reproducibility
    if seed is not None:
        np.random.seed(seed)

    # cooperate with probability p, otherwise defect
    return "C" if np.random.random() < p else "D"


def intermediate_punishment(opponent_history: List[str], k: int = 3) -> str:
    """
    Cooperate until the opponent defects. If the opponent defects, don't cooperate for the next 'k' periods. Then return to cooperation.

    :param opponent_history: history of the opponent
    :param k: number of periods to cooperate
    :return: "C" for cooperation, "D" for defect
    """
    # cooperation initially
    if not opponent_history:
        return "C"

    # if the opponent defects, don't cooperate for the next 'k' periods
    if opponent_history[-1] == "D" or "D" in opponent_history[-k:]:
        return "D"

    return "C"
