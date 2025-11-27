from typing import Dict, List


def check_applicant_optimality(
    applicants_result: Dict[str, str],
    hospitals_result: Dict[str, str],
    applicants_preferences: Dict[str, List[str]],
) -> bool:
    """
    Check if the matching produced by the Deferred Acceptance Algorithm is applicant-optimal.

    This is done by comparing the applicant-optimal matching to the hospital-optimal matching.

    Args:
        applicants_result (Dict[str, str]): A dictionary with applicants' results from an algorithm.
        hospitals_result (Dict[str, str]): A dictionary with hospitals' results from an algorithm.
        applicants_preferences (Dict[str, List[str]]): A dictionary with applicants' preferences.

    Returns:
        bool: True if the applicant-optimal matching holds, False otherwise.

    """
    # Check if applicants are matched to their best possible hospital in the applicant-optimal matching
    for applicant in applicants_preferences:
        applicant_match = applicants_result[applicant]
        # If there isn't match for the applicant, then pass.
        # It happens when the number of applicant is larger than the number of hospitals
        if len(applicant_match) == 0:
            pass
        else:
            hospital_optimal_match = [hospital for hospital, matched_applicant in hospitals_result.items() if matched_applicant == applicant][0]

            # If the applicant's match in the applicant-optimal matching is ranked higher than in the hospital-optimal matching
            if applicants_preferences[applicant].index(hospital_optimal_match) < applicants_preferences[applicant].index(applicant_match):
                # This means the applicant could have gotten a better match in the applicant-optimal matching
                return False
    return True
