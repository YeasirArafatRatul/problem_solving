N, X = map(int, input().split(' '))

students = zip(*[list(map(float,input().split(' '))) for subject in range(0,X)])

print( *map(lambda x: x/X, list( map(sum, students) ) ) , sep='\n')
