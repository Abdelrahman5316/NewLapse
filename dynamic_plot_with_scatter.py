import matplotlib.pyplot as plt

from collections import deque
import random
import scrape as sc
def pred_plot(dic):
    years_mean={}
    for year,urls in dic.items():
     #   for i in urls:
      #      x=sc.scrape(i)
       #     dic[year].replace(i,x)
            good=0
            bad=0
            for i in range(len(urls)):
                x=sc.scrape(dic[year][i])
                if x=='good':
                    good+=1
                elif x=='bad':
                    bad+=1
                if urls[i] == dic[year][i]:
                    urls[i] = x
            print(good)
            print(bad)
            mean_good=good/len(urls)
            mean_bad=bad/len(urls)
            dic[year]=(mean_good,mean_bad)

    print(dic)
        #urls_mean=sum([ sc.scrape(i) for i in urls])/len(urls)
        #years_mean[year]=urls_mean
    plot(dic)
      
    

import matplotlib.pyplot as plt
from collections import deque

def plot(dr):
    # Create a fixed-length deque to store the data points
    data_points = deque(maxlen=50)

    fig, ax = plt.subplots()

    line, = ax.plot([])
    line2, = ax.plot([])

    years = list(map(int, dr.keys()))  # Convert dictionary keys to a list of integers
    tp = list(dr.values())
    good=[]
    bad=[]
    for g,b in tp:
        good.append(g)
        bad.append(b)
    print(f'G & B {g,b}')
    ax.set_xlim(int(years[0]),int(years[-1]))
    mx=0
    for tp in dr.values():

        if tp[0]>mx:
            mx=tp[0]
        if tp[1]>mx:
            mx=tp[1]
    print(mx)
    ax.set_ylim(0,mx+10)
    print(years)
    for i in range(len(years)):
        
        print(years[i])
        new_x = int(years[i])
        new_yG = good[i]
        new_yB = bad[i]
        print(f'yG {new_yG}')
        print(f'yB {new_yB}')
        data_points.append((new_x, new_yG, new_yB))

        x_values = [x for x, y, y2 in data_points]
        y_values = [y for x, y, y2 in data_points]
        y2_values = [y2 for x, y, y2 in data_points]
        print(x_values)
        line.set_data(x_values, y_values)
        line2.set_data(x_values, y2_values)
        
        plt.pause(0.1)
        #Clear the plot for the next set of values
        #line.set_data([],[])

    plt.show()


#plot()
#def plot2(dr):
#    que=deque(maxlen=len(dr.keys())
#    for year,tp in dr.items():

#dr={2016:(2,3),2017:(10,2),2020:(15,2)}
#plot(dr)

