
import math as m


def prime_sieve(n):
    sieve = { i: True for i in range(0, n) }

    sieve[0] = False
    sieve[1] = False

    for j in range(2, int(m.sqrt(n)) + 1):
      if j not in sieve or sieve[j] == True:

        for p in range(j*2, n, j):
          sieve[p] = False

    return sieve


print("generating big sieve...")
big_sieve = prime_sieve(150_000_000)
N = len(big_sieve)
print("big sieve done")

cache = {}
def is_prime(n):
  if n in big_sieve:
    return big_sieve[n]

  if n in cache:
    return cache[n]

  print("OH NO: " + str(n))

  if n <= 3:
    return n > 1

  if n % 2 == 0 or n % 3 == 0:
    cache[n] = False
    return cache[n]

  i = 5

  while i ** 2 <= n:
    if n % i == 0 or n % (i + 2) == 0:
      cache[n] = False
      return cache[n]
    i += 6

  cache[n] = True
  return cache[n]


from itertools import combinations

def check_combo(combo):
  for new_combo in combinations(combo, 2):
    a, b = new_combo

    if not is_prime(int(f"{a}{b}")) or not is_prime(int(f"{b}{a}")):
      return False

  return True


def _test_intersection(pair_dict, intersection, depth = 1, good_numbers = set()):
  if depth == 5:
    return good_numbers

  for n in intersection:
    new_intersection = intersection.intersection(pair_dict[n])

    if len(intersection) + depth < 5:
      continue

    recursive_value = _test_intersection(pair_dict, new_intersection, depth + 1, {*good_numbers, n})

    if recursive_value == False:
      continue

    return recursive_value

  return False

def test_intersection(pair_dict, n):
  return _test_intersection(pair_dict, pair_dict[n], good_numbers={n})


def main():
  primes = set()

  print("generating primes...")

  for i in range(0, 10_000):
    if is_prime(i):
      primes.add(i)

  pair_map = {}

  print("generating pair_map...")
  for new_combo in combinations(primes, 2):
    a, b = new_combo

    if is_prime(int(f"{a}{b}")) and is_prime(int(f"{b}{a}")):
      if a not in pair_map:
        pair_map[a] = set()

      pair_map[a].add(b)

      if b not in pair_map:
        pair_map[b] = set()

      pair_map[b].add(a)

  for prime in pair_map.keys():
    result = test_intersection(pair_map, prime)

    if result:
      s = sum(list(result))
      print(f"{prime:6}: {result} => {s}")


if __name__ == '__main__':
  main()
