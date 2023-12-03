from functools import partial,reduce

data=dict()
with open('problem2\input.txt','r') as f:
    for l in f.readlines():
        g_id,dta = l.strip().split(': ')
        g_id=int( g_id.split(' ')[1] )
        g_sets = map(lambda x: x.split(', '),dta.split('; '))
        g_dta=list(map(lambda s: {d.split(' ')[1]:int(d.split(' ')[0]) for d in s},g_sets))
        data[g_id]=g_dta

part1_max={'red':12,'green':13,'blue':14}

# Part 1:

has_impossible_round = lambda gq: \
    any([gq[k]>part1_max[k] for k in gq.keys()])

is_impossible_game = lambda gqs: \
    reduce(lambda x,y: x or has_impossible_round(y),gqs,False)

solution1= sum([k for k,v in data.items() if not is_impossible_game(v)])
print(f"Solution 1: {solution1}")

# Part 2:
## Utils:
flatten=lambda l: list(reduce(lambda x,y: x+y,l,[]))
prod = lambda l: reduce(lambda x,y: x*y,l,1)

color_data = lambda col,d: \
        list( map(lambda x: x[1], list(filter(lambda x: x[0]==col,d.items()))) )

get_color_data = list(
        map(lambda col: partial(color_data,col),['red','green','blue'])
)

get_color_data_sets = lambda dl: \
        map(lambda f: \
            flatten(map(lambda d: f(d),dl)),
            get_color_data
        )

set_power = lambda dl: prod(map(max,get_color_data_sets(dl)))

solution2 = sum(map(set_power,data.values()))
print(f"Solution 2: {solution2}")