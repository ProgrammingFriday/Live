
n_agonal = {
  3: lambda n: n * (n + 1) // 2,
  4: lambda n: n ** 2,
  5: lambda n: n * (3 * n - 1)//2,
  6: lambda n: n * (2 * n - 1),
  7: lambda n: n * (5 * n - 3)//2,
  8: lambda n: n * (3 * n - 2),
}

def main():
  n_agonal_4_digit_numbers = {}

  for key, f in n_agonal.items():
    for n in range(0, 10000):
      x = f(n)

      x_str = str(x)
      n_digits = len(x_str)

      if n_digits == 4:
        if key not in n_agonal_4_digit_numbers:
          n_agonal_4_digit_numbers[key] = set()

        n_agonal_4_digit_numbers[key].add((x, x_str[0:2], x_str[2:4]))

  current_keys = set(n_agonal_4_digit_numbers).difference({3})

  for value in n_agonal_4_digit_numbers[3]:

    number, first_two, last_two = value

    result, numbers = find_solutuion(n_agonal_4_digit_numbers, current_keys, last_two, first_two, [ number ])

    if result == True:
      print(sum(numbers))
      break


def find_solutuion(n_agonal_4_digit_numbers, keys, last_two, first_last_two, numbers):
  if len(keys) == 0:
    return last_two == first_last_two, numbers

  for k in keys:
     for tuple_value in n_agonal_4_digit_numbers[k]:
        (number, first, last) = tuple_value

        if first == last_two:
          new_numbers = [*numbers, number ]

          result, final_numbers = find_solutuion(n_agonal_4_digit_numbers, keys.difference({k}), last, first_last_two, new_numbers)

          if result == True:
            return True, final_numbers

  return False, []


if __name__ == '__main__':
  main()
