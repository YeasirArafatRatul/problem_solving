N = 5842
import heapq


h = [1]
s = set(h)
heapq.heapify(h)

humble_numbers = [0]
for i in range(N):
  m = heapq.heappop(h)

  s.remove(m)
  humble_numbers.append(m)
  
  if not m*2 in s:
    s.add(m*2)
    heapq.heappush(h, m*2)
  if not m*3 in s:
    s.add(m*3)
    heapq.heappush(h, m*3)
  if not m*5 in s:
    s.add(m*5)
    heapq.heappush(h, m*5)
  if not m*7 in s:
    s.add(m*7)
    heapq.heappush(h, m*7)

    
while True:
    n = int(input())
    if n == 0:
        break
    str_n = str(n)
    if 10 <= (n % 100) < 20:
        print(f"The {n}th humble number is {humble_numbers[n]}.")
    else:
        if str_n[-1]== '1':
            print(f"The {n}st humble number is {humble_numbers[n]}.")
        elif str_n[-1]=='2':
            print(f"The {n}nd humble number is {humble_numbers[n]}.")
        elif str_n[-1]=='3':
            print(f"The {n}rd humble number is {humble_numbers[n]}.")
        else:
            print(f"The {n}th humble number is {humble_numbers[n]}.")
        
