import math
import itertools


def calculate_score_1(prediction, actual):
    num_of_teams = len(prediction) + 1
    num_of_rounds = int(math.log(num_of_teams, 2))

    score = 0

    num_of_results = num_of_teams // 2
    true_flags = list(itertools.repeat(True, num_of_results))
    current_index = 0
    for i in range(0, num_of_rounds):
        predictions = []
        for j in range(current_index, current_index + num_of_results):
            predictions.append(prediction[j] == actual[j] and true_flags[j])
            current_index += 1

        score += sum(predictions)

        if num_of_results == 1:
            break
        true_flags = true_flags + [(predictions[i] and predictions[i + 1]) for i in range(0, num_of_results, 2)]
        num_of_results = num_of_results // 2

    return score


# Binary tree solution
def calculate_score_2(predictions, actuals):
    scores = []
    for prediction, actual in zip(predictions, actuals):
        scores.append(prediction == actual)
    # Invert scores, construct binary tree
    scores = scores[::-1]
    # For each node check its children if they are both True,
    # and if not, set score of that node to False.
    # Do it bottoms up
    for i in list(range(0, len(scores) // 2))[::-1]:
        scores[i] = scores[2 * i + 1] and scores[2 * i + 2]

    return sum(scores)


# Binary tree solution
def calculate_score_3(predictions, actuals):
    scores = [prediction == actual for prediction, actual in zip(predictions, actuals)]
    # Invert scores, construct binary tree
    scores = scores[::-1]
    # For each node check its children if they are both True,
    # and if not, set score of that node to False.
    # Do it bottoms up
    for i in reversed(range(0, len(scores) // 2)):
        scores[i] = scores[2 * i + 1] and scores[2 * i + 2]

    return sum(scores)
