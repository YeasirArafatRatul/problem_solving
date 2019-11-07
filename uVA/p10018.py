
def addition(n):
    count = 0
    while True:
        str_n = str(n)
        if str_n == str_n[::-1]:
            break
        else:
            reverse_n = str_n[::-1]
            n += int(reverse_n)
            count += 1
    print(f"{count} {n}")



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        addition(n)
