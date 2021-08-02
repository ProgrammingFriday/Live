
import math as m


def prime_sieve(n, get_real_sieve=False):
    sieve = []

    for i in range(0, n):
       sieve.append(True)

    sieve[0] = False
    sieve[1] = False

    for j in range(2, int(m.sqrt(n)) + 1):
      if sieve[j] == True:
        for p in range(j*2, n, j):
          sieve[p] = False

    if get_real_sieve:
      return sieve

    return { i for i, is_prime in enumerate(sieve) if is_prime == True }


big_sieve = prime_sieve(10_000_000, True)
N = len(big_sieve)

cache = {}
def is_prime(n):
  if n < N:
    return big_sieve[n]

  if n in cache:
    return cache[n]

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


def main():
  sieve = prime_sieve(5_000)

  pairs = []

  for new_combo in combinations(sieve, 2):
    a, b = new_combo

    if is_prime(int(f"{a}{b}")) and is_prime(int(f"{b}{a}")):
      pairs.append((a, b))

  for combo in combinations(pairs, 3):
    t1, t2, t3 = combo

    first = {t1[0], t1[1], t2[0], t2[1]}
    if len(first) < 4:
      continue

    for val in t3:
      to_check = {*first, val}
      if len(to_check) < 5:
        continue

      print(to_check)
      result = check_combo(to_check)
      if result == True:
        print(to_check)
        from sys import exit
        exit(0)


if __name__ == '__main__':
  main()
