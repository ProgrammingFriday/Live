

tokens = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, "*", "==" ]
tokens = map(str, tokens)

from itertools import permutations

def main():
  valid = []
  n = 0
  for perm in permutations(tokens, 11):
    statement = "".join(perm)

    if n % 10000 == 0:
      print(n, statement)
      print(valid)
      pass

    try:
      value = eval(statement)
      if value == True:
        print(statement)
        valid.append(statement)
    except:
      pass

    n += 1

  print(valid)

  # valid = ['12*483==5796', '138*42==5796', '157*28==4396', '159*48==7632', '1738*4==6952', '186*39==7254', '18*297==5346', '1963*4==7852', '198*27==5346', '27*198==5346', '28*157==4396', '297*18==5346', '39*186==7254', '42*138==5796', '4396==157*28', '4396==28*157', '483*12==5796', '48*159==7632', '4*1738==6952', '4*1963==7852', '5346==18*297', '5346==198*27', '5346==27*198', '5346==297*18', '5796==12*483', '5796==138*42', '5796==42*138', '5796==483*12', '6952==1738*4', '6952==4*1738', '7254==186*39', '7254==39*186', '7632==159*48', '7632==48*159', '7852==1963*4', '7852==4*1963']

  numbers = set()

  for valid_statement in valid:
    (left, right) = valid_statement.split("==")
    if "*" in left:
      numbers.add(right)
    else:
      numbers.add(left)

  print(sum([int(number) for number in numbers]))

if __name__ == '__main__':
  main()
