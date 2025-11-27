from typing import Dict, List, Tuple


def deferred_acceptance(applicants_preferences: Dict[str, List[str]], hospitals_preferences: Dict[str, List[str]]) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Implement the Deferred Acceptance Algorithm to find a stable matching between applicants and hospitals.

    Args:
        applicants_preferences (Dict[str, List[str]]): A dictionary where each key is an applicant (str)
            and the value is a list of hospital names (str) ordered by preference.
        hospitals_preferences (Dict[str, List[str]]): A dictionary where each key is a hospital (str)
            and the value is a list of applicant names (str) ordered by preference.

    Returns:
        Tuple[Dict[str, str], Dict[str, str]]:
            - A dictionary where each key is an applicant (str) and the value is the matched hospital (str).
            - A dictionary where each key is a hospital (str) and the value is the matched applicant (str).

    """
    # Initialize all applicants and hospitals as unmatched
    unmatched_applicants = list(applicants_preferences.keys())
    applicant_matches = {applicant: "" for applicant in applicants_preferences}
    hospital_matches = {hospital: "" for hospital in hospitals_preferences}

    # While there are unmatched applicants
    while unmatched_applicants:
        applicant = unmatched_applicants.pop(0)
        # Applicant proposes to the most preferred hospital that hasn't rejected them yet
        preferred_hospitals = applicants_preferences[applicant]

        for hospital in preferred_hospitals:
            if hospital_matches[hospital] == "":
                # If the hospital is unmatched, the applicant gets matched to it
                applicant_matches[applicant] = hospital
                hospital_matches[hospital] = applicant
                break
            else:
                # If the hospital is already matched, it checks if it prefers the new applicant
                current_match = hospital_matches[hospital]
                if hospitals_preferences[hospital].index(applicant) < hospitals_preferences[hospital].index(current_match):
                    # The hospital prefers the new applicant, so they swap matches
                    applicant_matches[applicant] = hospital
                    applicant_matches[current_match] = ""
                    unmatched_applicants.append(current_match)
                    hospital_matches[hospital] = applicant
                    break
                else:
                    # Hospital rejects the applicant
                    continue

    return applicant_matches, hospital_matches
