def train_swapper(carriages):
    count = 0
    for i in range(len(carriages)):
        for j in range(i+1,len(carriages)):
            if carriages[i] > carriages[j]:
                carriages[i],carriages[j] = carriages[j],carriages[i],
                count += 1
            
    print(f"Optimal train swapping takes {count} swaps.")
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        l = int(input())
        carriages = list(map(int,input().split()))
        train_swapper(carriages)
