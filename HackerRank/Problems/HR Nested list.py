

N = int(input())

students = list()
#will take studesnts name and number until i<n (i=0)
for i in range(N):
    students.append([input(), float(input())])

#sorting scores and setting the values with students name
score = set([students[x][1] for x in range(N)])
scores = list(score)
scores.sort()

#sorting the students name 

students = [x[0] for x in students if x[1] == scores[1]]
students.sort()

for s in students:
    print(s)
