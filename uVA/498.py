while True:
  line = input()

  if line == "":
    break

  coeffs = list(map(int, line.strip().split()))
  
  out = []
  for x in map(int,input().strip().split()):
    out.append(sum(c*(x**i) for i, c in enumerate(reversed(coeffs))))

  print(f"{(' '.join(map(str, out)))}")
