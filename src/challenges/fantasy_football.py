"""
A  B   C   D
  B     D
     D

0 = Left team won
1 = Right team won

prediction 101
actual 101
score = 3

====================

prediction: 111
actual: 101
score: 1

====================

calculateScore(prediction, actual) => return score

calculateScore([1,1,0,0,1,1,0], [1,0,0,0,1,1,1])

pred: 1100 11 0
actual: 1000 11 1
score: 4

11 v.s. 11
if agree in this round, look at last round
else disagree

Number Teams: 2^X

Size of first round: Teams/2
Size of second round: Teams/4

NumberOfBits = T/2 + T/4 + T/8 ....

111 => 4 teams
T = 4  NumberBits = 3
T = 8  NumberBits = 7

Number bits to represent match: Teams - 1

2^0 + 2^1 + 2^2...

X A  Y B  Z C W D
 A   B     C  D
   B         D
        D
"""
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
        scores[i] = scores[i] and scores[2 * i + 1] and scores[2 * i + 2]

    return sum(scores)


# Binary tree solution alt
def calculate_score_3(predictions, actuals):
    scores = [prediction == actual for prediction, actual in zip(predictions, actuals)]
    # Invert scores, construct binary tree
    scores = scores[::-1]
    # For each node check its children if they are both True,
    # and if not, set score of that node to False.
    # Do it bottoms up
    for i in reversed(range(0, len(scores) // 2)):
        scores[i] = scores[i] and scores[2 * i + 1] and scores[2 * i + 2]

    return sum(scores)
