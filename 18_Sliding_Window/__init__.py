from functools import reduce
data=[
    {'a':[1,2]},
    {'a':[2,3]},
    {'b':[22]},
    {'d':'90'}
]

final_dict = dict()
for i in data:
    name=None
    for k,v in i.items():
        if k=='name':
            final_dict[v]=[]
            name=k
        if k=='rules':
            final_dict[name].extend(v)


print(final_dict)