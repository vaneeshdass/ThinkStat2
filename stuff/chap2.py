import nsfg
import thinkplot
import thinkstats2

t = [1, 2, 2, 3, 5]

hist = {}
for x in t:
    hist[x] = hist.get(x, 0) + 1

hist

from collections import Counter

counter = Counter(t)
counter

hist = thinkstats2.Hist([1, 2, 2, 3, 5])
hist

thinkplot.Hist(hist)
thinkplot.Config(xlabel='value', ylabel='frequency')
thinkplot.Show(xlabel='value', ylabel='frequency')

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
thinkplot.Hist(hist)
thinkplot.Show(xlabel='pounds', ylabel='frequency')

live.__len__()
