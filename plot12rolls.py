import os
import sys
import math
import matplotlib.pyplot as plt

if "__main__" == __name__:

  expected = 794

  lt_data = list(map(float,sys.stdin))
  count = len(lt_data)
  mn,mx = map(int,[min(lt_data),max(lt_data)+2])
  bins = range(mn,mx)

  avg = sum(lt_data)/count
  plt.xlim([mn,mx])
  plt.axvline(avg,color='r',label='Mean')
  plt.hist(lt_data,bins=bins,histtype='bar',label='Histogram')
  plt.xlabel('Modeled cases per 4096 rolls with even count<5')
  plt.ylabel('Count of occurences of each value of cases')
  plt.title('{0} cases; mean={1:.2f}'.format(count,avg))
  plt.legend()
  plt.show()

"""
  plt.xlim([1,i])
  plt.axhline(0.)
  plt.axhline(-1.)
  plt.axhline(-2.)
  plt.axhline(-3.)
  plt.plot(ipos,dpos,'b.',label='N>{0}'.format(expected))
  plt.plot(ineg,dneg,'r.',label='N<{0}'.format(expected))
  plt.ylabel('log10(|N-{0}|); N=running avg cases/4096 w/even count<5'.format(expected))
  plt.xlabel('4096-sample run')
  plt.legend()
  plt.show()
"""
