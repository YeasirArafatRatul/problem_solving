

sol = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440]

i = 0
while True:
  try:
    line = inpSut().strip()
    while line == "":
      line = input().strip()
    n = int(line)
    if i == 1:
      print()
    print(sol[n])
    i = 1
  except(EOFError):
    break
