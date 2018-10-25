# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:42:22 2018

@author: Hardik Galiawala
"""
# Reference: http://mlwhiz.com/blog/2015/09/13/seaborn_visualizations/
    
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

performance = [{'question': 'a', 'Technology': 'SQL', 'perf': 78},
               {'question': 'a', 'Technology': 'Elastic', 'perf': 212},
               {'question': 'b', 'Technology': 'SQL', 'perf': 312},
               {'question': 'b', 'Technology': 'Elastic', 'perf': 167},
               {'question': 'c', 'Technology': 'SQL', 'perf': 79},
               {'question': 'c', 'Technology': 'Elastic', 'perf': 388},
               {'question': 'd', 'Technology': 'SQL', 'perf': 1625},
               {'question': 'd', 'Technology': 'Elastic', 'perf': 256}]

''''
performance2 = [{'question': 'a', 'Technology': 78, 'Elastic': 212},
               {'question': 'b', 'SQL': 312, 'Elastic': 167},
               {'question': 'c', 'SQL': 79, 'Elastic': 388},
               {'question': 'd', 'SQL': 1625, 'Elastic': 256}]
'''
# Typecasting dictionary to a pandas dataframe
df = pd.DataFrame.from_dict(performance)

plot = sns.barplot(x = "question", y = "perf", hue = "Technology", data=df)
sns.despine()
# Cosmetic work from here.
plot.axes.set_title('Performance SQL v/s Elastic Search',
    fontsize=16,color="b",alpha=0.3)
plot.set_xlabel("Questions",size = 16,color="b",alpha=0.5)
plot.set_ylabel("Time(in ms)",size = 16,color="r",alpha=0.5)
plot.tick_params(labelsize=14,labelcolor="black")
plot.figure.savefig('performancePlot.png')