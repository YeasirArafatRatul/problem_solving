num_tests = int(input())

for test in range(num_tests):
  
  num_routes = int(input())
  
  total, ans = 0,0
  start = 0
  last_l = 1
  
  for i in range(0, num_routes-1):
    total += int(input().strip())
    print(total)
    
    if total > ans:
      ans = total
      start = last_l
      end = i + 2
      
    elif total == ans:
      if i + 2 - last_l > end - start:
        start = last_l
        end = i + 2

    if total  < 0:
      total = 0
      last_l = i + 2

  if ans > 0:
      print(f"The nicest part of route {test+1} is between stops {start} and {end}")
  else:
      print(f"Route {test+1} has no nice parts")

