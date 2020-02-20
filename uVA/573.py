while True:
  h, u, d, f = list(map(int, input().split()))

  if h == 0:
    break

  total_ascent = 0 
  f = f*u/100
  
  for i in range(200):
    ascent = max(u - f*i, 0)

    total_ascent += ascent
    if total_ascent > h:
      print(f"success on day {i+1}")
      break

    total_ascent -= d
    if total_ascent < 0:
      print(f"failure on day {i+1}")
      break
  



