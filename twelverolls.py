"""
Usage:

  python twelverolls.py [--loops=41] [--shift=4]

Sample usage:

  python twelverolls.py --loops=1000 | python plot12rolls.py 

Modeling:

- Use /dev/urandom to get random bytes
- Extract bit 4 (1<<4 => 16) as indication of even or odd roll of die

"""
import os
import sys
if "__main__" == __name__:

  ### Defaults
  n_loops = 41
  bit_shift = 4

  ### Process input arguments
  for arg in sys.argv[1:]:
    if arg.startswith('--loops='): n_loops = int(arg.split('=')[1])
    elif arg.startswith('--shift='): bit_shift = int(arg.split('=')[1])
    else:
      sys.stderr.write('WARNING:  invalid argument [{0}] ignored\n'.format(arg))

  ### Convert shift to bit
  i_bit = 1<<bit_shift

  ### Open uniform random bytes file
  with open("/dev/urandom","rb") as f_random:

    ### Start sample loop; each loop models 4096 12-roll runs
    for i_loop in range(n_loops):

      ### Initialize counter
      n = 0

      ### Perform 4096 12-roll runs
      for roll in range(4096):

        ### Model 12 rolls via 12 bytes from f_random (urandom file)
        ### - Bit i_bit of each byte models even roll if set, else odd
        ### - List of conditional None's models resulting even rolls
        ### - Increment counter if less than five even rolls
        n += (5 > len([None
                       ### Convert binary to string, loop over chars
                       for char in f_random.read(12).decode('8859')
                       ### ord() converts char to inty; test bit i_t
                       if (ord(char) & i_bit)
                      ### Add 1 to counter if bit is set (=> even roll)
                      ])) and 1 or 0

      ### Print number of 12-roll runs with less than 5 even rolls
      print(n)
      sys.stdout.flush()
