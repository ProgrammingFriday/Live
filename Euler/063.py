# Om t > 10 => vi kan skriva t = a*10^k, där 1<=a<10, alltså består t^n av fler än n siffror


def main():
  roof1 = 100
  roof2 = 25

  powerful = set()
  for n in range(1, roof1):
    for e  in range(1, roof2):
      val = n ** e
      if len(str(val)) == e:
        powerful.add(val)

  print(len(powerful))
  # print(powerful)

if __name__ == '__main__':
  main()
