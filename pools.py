#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md
import matplotlib.animation as animation
from capybot import load_data
import sys

# Do not use automatic offsets for plot axis
import matplotlib as mpl
mpl.rcParams['axes.formatter.useoffset'] = False

if len(sys.argv) != 2:
    sys.exit("No path to Capybot log file given")

file = sys.argv[1]

# Readable names for pools
pools = {
    '0xcf994611fd4c48e277ce3ffd4d4364c914af2c3cbb05f7bf6facd371de688630': 'Cetus USDC/SUI',
    '0x2e041f3fd93646dcc877f783c1f2b7fa62d30271bdef1f21ef002cebf857bded': 'Cetus CETUS/SUI',
    '0x238f7e4648e62751de29c982cbf639b4225547c31db7bd866982d7d56fc2c7a8': 'Cetus USDC/CETUS',
    '0x5eb2dfcdd1b15d2021328258f6d5ec081e9a0cdcfa9e13a0eaeb9b5f7505ca78': 'Turbos SUI/USDC',
    '0xaa57c66ba6ee8f2219376659f727f2b13d49ead66435aa99f57bb008a64a8042': 'Cetus WBTC/USDC',
}

# Plot of prices of all monitored pools
fig, ax = plt.subplots(1,1)

def animate_prices(j):
    data = load_data(file);
    ax.clear()
    ax.set_title('Price development (A to B)')
    for source in data['prices']:
        prices = data['prices'][source]['price'];
        normalized = np.multiply(prices, 1 / data['prices'][source]['offset'])    
        timestamps = data['prices'][source]['time'];
        dates = [dt.datetime.fromtimestamp(ts) for ts in timestamps]
        ax.plot(dates, normalized, label = pools[source])
    ax.legend();

anim = animation.FuncAnimation(fig, animate_prices, interval = 1000)
plt.show()