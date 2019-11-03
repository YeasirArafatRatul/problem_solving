
def score_count(data,score = 0):
    for i in range(len(data)):
        number = i
        if data[i]== '0':
            score += (number + 1)
            print(score)
        else:
            score_count(data[i+1:],score=score)
            break

            
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        data = input()
    score_count(data)
 

