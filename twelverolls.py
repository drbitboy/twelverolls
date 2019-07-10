"""
Usage:

  python twelverolls.py --loops=1000 | python plot12rolls.py 

"""
import os
import sys
if "__main__" == __name__:
  n_loops = 41.0
  bit_shift = 4
  for arg in sys.argv[1:]:
    if arg.startswith('--loops='): n_loops = int(arg.split('=')[1])
    elif arg.startswith('--shift='): bit_shift = int(arg.split('=')[1])
  i_bit = 1<<bit_shift
  n_794 = 0
  i_loop = 0.
  with open("/dev/urandom","rb") as f_random:
    while i_loop < n_loops:
      i_loop += 1.0
      n = 0
      for roll in range(4096):
        n += (5 > len([None
                       for c in f_random.read(12).decode('8859')
                       if (ord(c) & i_bit)
                      ])) and 1 or 0
      print(n)
      sys.stdout.flush()
