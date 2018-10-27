#!/usr/bin/env python2
from pprint import pprint

# TODO get dimenstion from \n

dimension = 10
state = \
    '..........'\
    '..........'\
    '..........'\
    '..........'\
    '.....0....'\
    '.....0....'\
    '.....0....'\
    '..........'\
    '..........'\
    '..........'


def state_printer(state, dimension):
    buff = ''
    for counter, elem in enumerate(state):
        # print(counter)
        buff += elem
        if (counter+1) % dimension == 0 and counter != 0:
            print(buff)
            buff = ''

# x1 = zip(x0, count(1, 1))
x0 = zip(state, range(1, 1000000))
# print(x0)
x1 = map(lambda x: {'value': 1 if x[0] == '0' else 0, 'position':x[1] }, x0)
# print(x1)
x2 = zip(x1, ( x1 for x in range(1, 100000)))
# print(x2)
x3 = map(lambda x: {'value': x[0]['value'], 'position': x[0]['position'], 'state': x[1]}, x2)
# pprint(x3)
x4 = map(lambda x: {'value': x['value'], 'position': x['position'],
                    'state':
                        filter(lambda xx:
                               xx['position'] == x['position']-dimension-1 or
                               xx['position'] == x['position']-dimension or
                               xx['position'] == x['position']-dimension+1 or
                               xx['position'] == x['position']-1 or
                               xx['position'] == x['position']+1 or
                               xx['position'] == x['position']+dimension-1 or
                               xx['position'] == x['position']+dimension or
                               xx['position'] == x['position']+dimension+1
                               ,
                               x['state'])}, x3)
pprint(x4)

x5 = map(lambda x: {'value': x['value'], 'position': x['position'],
                    'state': reduce(lambda a, b: a+b, map(lambda c: c['value'],x['state']))}, x4)
pprint(x5 )
x6 = map(lambda x: {'value': x['value'], 'position': x['position'],
                    'state': x['state'], 'change_state': False}, x5)
pprint(x6)

x7 = map(lambda x: {'value': x['value'], 'position': x['position'],
                    'state': x['state'], 'change_state': True if ((x['value'] == 1 and x['state'] == 1) or (x['value'] == 0 and x['state'] == 3) or (x['value'] == 1 and x['state'] > 3) ) else False}, x6)
pprint(x7)
x8 = map(lambda x: {'value': 1 if ((x['value']==1 and x['change_state'] ==False) or (x['value']==0 and x['change_state'] ==True)) else 0, 'position': x['position'],
                    'state': x['state'], 'change_state':x['change_state']} , x7)
pprint(x8)
x9 = map(lambda x: '.' if x['value'] == 0 else '0', x8)




state_printer(state, dimension)
state_printer(x9, dimension)

