
from pprint import pprint

cache = {}

def main():
  roof = 10 ** 5

  for n in range(1, roof):
    cube = n ** 3

    digits = [int(digit) for digit in str(cube)]
    digits.sort(reverse=True)

    digits_hash = "".join([str(digit) for digit in digits])

    if digits_hash not in cache:
      cache[digits_hash] = []

    cache[digits_hash].append(cube)

    if len(cache[digits_hash]) == 5:
      return min(cache[digits_hash])

  return -1

if __name__ == '__main__':
    pprint(main())
