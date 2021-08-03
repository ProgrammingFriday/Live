
from functools import cache


@cache
def partitions(n, limit):
  if n <= 0 or limit <= 0:
    return 0

  if n == 1 or limit == 1:
    return 1

  if limit >= n:
    return 1 + partitions(n, n-1)

  s = 0
  for i in range(1, limit+1):
    new_limit = i
    s += partitions(n-i, new_limit)

  return s


def main():
  print(partitions(100, 100) - 1)


if __name__ == '__main__':
  main()
