
roof = (9 ** 5) * 27

def main():

  sum_of_all = 0

  for i in range(2, roof):
    total = 0

    for digit in str(i):
      n = int(digit)
      total += n ** 5

    if total == i:
      sum_of_all += i

  print(sum_of_all)

if __name__ == '__main__':
    main()
