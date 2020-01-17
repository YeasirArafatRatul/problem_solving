n = int(input())
student_marks = {}
for _ in range(n):
    #*line is a variable length argument
    name, *line = input().split()
    scores = list(map(float, line))
    #name is the key of the dictionary and scores are value
    student_marks[name] = scores
#print(scores)
#print(student_marks)
query_name = input() #student_name

student_score = student_marks[query_name]

total_num = sum(student_score)
average = total_num/len(student_score)

print("{0:.2f}".format(average))
    

