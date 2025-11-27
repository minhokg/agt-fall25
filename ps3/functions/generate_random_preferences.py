import random
from typing import Dict, List, Tuple


# Function to generate random datasets for applicants' and hospitals' preferences
def generate_random_preferences(num_applicants: int, num_hospitals: int) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """
    Generate random preference lists for applicants and hospitals.

    Args:
        num_applicants (int): Number of applicants.
        num_hospitals (int): Number of hospitals.

    Returns:
        Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
            - A dictionary where each key is an applicant (str) and the value is a list of hospital names (str) ordered by preference.
            - A dictionary where each key is a hospital (str) and the value is a list of applicant names (str) ordered by preference.

    """
    applicants_preferences = {f"A{i}": random.sample([f"H{j}" for j in range(1, num_hospitals + 1)], num_hospitals) for i in range(1, num_applicants + 1)}
    hospitals_preferences = {f"H{i}": random.sample([f"A{j}" for j in range(1, num_applicants + 1)], num_applicants) for i in range(1, num_hospitals + 1)}

    return applicants_preferences, hospitals_preferences
