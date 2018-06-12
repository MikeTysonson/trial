import sys

if __name__ == "__main__":
  print ('Hello World')
  print ('i already know more than before')
  print ("now the renaming get's weird")
  print ('how can git now this is the same file if both name and content changed')
  print ('why do i even add if it all goes in one Aufwasch')

# jup
# hey, i changed a lot of stuff and now i have a conflict
from monkey  import * 

printSome()

def print_palmtrees(num):
  for i in range(num):
    sys.stdout.write(' /|\\')
  sys.stdout.write('\n')
  for i in range(num):
    sys.stdout.write('  | ')
  sys.stdout.write('\n\n')

print_palmtrees(2)
