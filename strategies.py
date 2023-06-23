#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md
import matplotlib.animation as animation
from capybot import load_data
import sys
from matplotlib.widgets import Slider

# Do not use automatic offsets for plot axis
import matplotlib as mpl
mpl.rcParams['axes.formatter.useoffset'] = False

if len(sys.argv) != 2:
    sys.exit("No path to Capybot log file given")

file = sys.argv[1]

data = load_data(file);
number_of_strategies = len(data['strategies']);
fig, ax = plt.subplots(number_of_strategies, 1, figsize = (6, 10));
fig.tight_layout(pad=2.0)

def animate_strategies(j):
    data = load_data(file);
    for i, uri in enumerate(data['strategies']):
        strategy = data['strategies'][uri]
        ax[i].clear()
        ax[i].set_title(strategy['parameters']['name'] + "")

        timestamps = strategy['statuses']['time']
        dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]

        if len(strategy['statuses']['value']) == 0:
            break

        for key in strategy['statuses']['value'][0]:
            y = list(map(lambda x: x[key], strategy['statuses']['value']))
            ax[i].plot(dates, y, label = key)
        
        # A trade order is indicated by a vertical red line
        if uri in data['orders']:
            x = [dt.datetime.fromtimestamp(ts) for ts in data['orders'][uri]['time']];
            for xi in x:
                ax[i].axvline(x = xi, color = 'r')
        
        ax[i].legend();    

anim = animation.FuncAnimation(fig, animate_strategies, interval = 1000)
plt.show()
