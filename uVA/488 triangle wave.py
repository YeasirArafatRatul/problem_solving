no_of_cases = int(input())

def sequence(n):
    return (str(n)*n)
     
for cases in range(no_of_cases):
    input()
    amplitude = int(input())
    frequency = int(input())

    loop_times = amplitude+(amplitude-1)
    
    for f in range(frequency):
        to_minus = 1
        for i in range(1,loop_times+1):
            if i > amplitude:
                i = amplitude - to_minus
                print(sequence(i))
                to_minus += 1
            else:
                print(sequence(i))
                
        if f < frequency-1:
            print()
    if cases < no_of_cases-1:
        print()


