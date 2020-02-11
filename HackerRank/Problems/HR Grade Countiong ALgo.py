#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    updated_grades = []
    for grade in grades:
        if grade<38:
            updated_grades.append(grade)
        elif grade%5 >= 3:
            t = 5-(grade%5)
            grade += t
            updated_grades.append(grade)
        else:
            updated_grades.append(grade)
    return updated_grades
            

            
if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
