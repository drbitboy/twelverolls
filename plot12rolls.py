import os
import sys
import math
import matplotlib.pyplot as plt

if "__main__" == __name__:

  expected = 794

  ### Convert flat file to floats
  lt_data = list(map(float,sys.stdin))

  ### Number of cases
  count = len(lt_data)

  ### Extent
  mn,mx = map(int,[min(lt_data),max(lt_data)+2])

  ### Bins to plot
  bins = range(mn,mx)

  ### Calculate average
  avg = sum(lt_data)/count

  ### Set abscissa limits
  plt.xlim([mn,mx])

  ### Plot vertical lines at expected value and at mean
  plt.axvline(expected+0.5,color='k',label='Expected ({0})'.format(expected))
  plt.axvline(avg,color='r',label='Mean')

  ### Plot histogram
  plt.hist(lt_data,bins=bins,histtype='bar',label='Histogram')

  ### Annotate plot
  plt.xlabel('Modeled cases per 4096 12-roll runs with even count<5')
  plt.ylabel('Count of occurences of each value of cases')
  plt.title('{0} cases; 4096 12-roll runs per case; mean={1:.2f}'.format(count,avg))
  plt.legend()

  ### Show plot
  plt.show()
