# Wesley Murray
# 2/15/2021
# This file is for solving the article value optimization problem.

# The problem:
# You have a list of articles. Each article has a page count and an
# intelligence value. You are given a page limit and must find the 
# combination of articles that maximizes the intelligence value while
# meeting the total page limit constraint.

def bruteForceSolution(pages,IQ,pageLimit):
    return []