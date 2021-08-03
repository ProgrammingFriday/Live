

money = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
coins = money.reversed()

def solve(goal, current=0):
  n = 0

  if current >= goal:
    return True

  for coin in money:
    if current + coin == goal:
      n += 1
    else:
      n += solve(goal, current + goal)

  return n

def solve2(goal, coins, index):
  i = 0
  while goal > coins[index]:



def main():
  print(solve(200))


if __name__ == '__main__':
  main()

