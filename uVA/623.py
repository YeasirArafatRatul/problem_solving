fact = [1]
for i in range(1, 1001):
  fact.append(i*fact[-1])

while True:
  try:
    num = int(input())
    print(f"{num}!")
    print(fact[num])
  except(EOFError):
    break
