#!/usr/bin/env python
# coding: utf-8

import json

# Load all data from the output of a Capybot. Each line is a log message in JSON format.
def load_data(file):
    prices = {}
    strategies = {}
    orders = {}
    
    with open(file) as f:
        for line in f.read().splitlines():
            try:
                data = json.loads(line)
                
                if 'msg' not in data:
                    continue

                match data['msg']:
                    # A price message for a swap pool
                    case "price":
                        entry = data['price']
                        price = entry['price'];
                        source = entry['source_uri'];

                        # The first price is used as the relative offset
                        if source not in prices:
                            prices[source] = {
                                'offset': entry['price'],
                                'price': [],
                                'time': [],
                            }
                        prices[source]['price'].append(price)
                        prices[source]['time'].append(data['time'] / 1000)

                    # When starting, Capybot outputs all used strategies. But note that this is only done once.
                    case "strategies":
                        for strategy in data['strategies']:
                            strategies[strategy] = {};
                            strategies[strategy]['parameters'] = data['strategies'][strategy];
                            strategies[strategy]['statuses'] = {
                                'value': [],
                                'time': []  
                            }

                    # Status from a strategy. This may contain arbitrary values decided by the strategy, so we just store everything.
                    case "strategy status":
                        strategy = data['uri']
                        entry = data['data'];
                        strategies[strategy]['statuses']['value'].append(entry)
                        strategies[strategy]['statuses']['time'].append(data['time'] / 1000)

                    # A strategy returned a trade order. Store the time-stamp.
                    case "order":
                        strategy = data['strategy']
                        if strategy not in orders:
                            orders[strategy] = {
                                'time':  [],
                            }
                        orders[strategy]['time'].append(data['time'] / 1000);

                    case _:
                        continue
                     
            except: 
                continue
                
    return {
        'prices': prices, 
        'strategies': strategies,
        'orders': orders
    } 