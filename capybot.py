#!/usr/bin/env python
# coding: utf-8

import json

# Load all data from the output of a Capybot
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
                    case "price":
                        entry = data['price']
                        price = entry['price'];
                        source = entry['source_uri'];
                        if source not in prices:
                            prices[source] = {
                                'offset': entry['price'],
                                'price': [],
                                'time': [],
                            }
                        prices[source]['price'].append(price)
                        prices[source]['time'].append(data['time'] / 1000)

                    # When starting, Capybot outputs all used strategies
                    case "strategies":
                        for strategy in data['strategies']:
                            strategies[strategy] = {};
                            strategies[strategy]['parameters'] = data['strategies'][strategy];
                            strategies[strategy]['statuses'] = {
                                'value': [],
                                'time': []  
                            }

                    case "strategy status":
                        strategy = data['uri']
                        entry = data['data'];
                        strategies[strategy]['statuses']['value'].append(entry)
                        strategies[strategy]['statuses']['time'].append(data['time'] / 1000)

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