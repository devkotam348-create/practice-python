#write a pyhton function remove duplicate elments form a given list.(TSRS)

def num(a):
      dup = []

      for i in a:
            if i not in dup:
                  dup.append(i)
            
      return dup

def main ():
      
      a = [2,3,4,2,5,6,3,2,7,8]

      print(f"the list after removing the duplicat will be {num (a)}")

main()