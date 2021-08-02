
def main():
  total = 1

  for i in range(3, 1002, 2):
      square = i ** 2
      corners = [ square - (i-1) * k for k in range(0, 4) ]

      total += sum(corners)

  print(total)


if __name__ == "__main__":
  main()
