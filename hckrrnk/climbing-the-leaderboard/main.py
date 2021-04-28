#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player_scores):
    
    results = []
    ranked_scores = list(sorted(set(ranked)))
    # ranked_scores = sorted(ranked)
    
    # time complexity: O(N*M)

    # for lowest_player_score in player_scores:
    #     while len(ranked_scores) > 0 and lowest_player_score >= ranked_scores[0]:
    #         ranked_scores.pop(0)
    #     results.append(len(ranked_scores)+1)
    
    # return results

    ranked.sort()

    y = len(ranked)
    for i in range(len(player_scores)):
        results.append(y - bisect(ranked, player_scores[i]) + 1)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

