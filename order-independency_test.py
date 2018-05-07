import copy
import random
from ruleExtraction import ruleExtraction 

dataSets = [[ #test5
[{2}, {3}, {2}, 'a'],
[{5}, {5}, {2}, 'a'],
[{4}, {3}, {2}, 'b'],
[{5}, {2}, {2}, 'b'],
[{6}, {5}, {2}, 'b'],
[{4}, {6}, {2}, 'b'],
[{3}, {2}, {2}, 'b'],
[{4}, {2}, {2}, 'a'],
[{4}, {1}, {2}, 'b'],
[{2}, {6}, {2}, 'a'],
[{1}, {5}, {2}, 'a'],
[{6}, {6}, {2}, 'b'],
[{3}, {3}, {2}, 'a'],
[{2}, {5}, {2}, 'a'],
[{3}, {5}, {2}, 'a']],
[ #test6
[{1}, {2}, {3}, "a"],
[{1}, {5}, {3}, "b"],
[{4}, {4}, {3}, "a"],
[{1}, {3}, {3}, "a"],
[{5}, {6}, {3}, "a"],
[{2}, {3}, {3}, "a"],
[{3}, {4}, {3}, "b"],
[{5}, {2}, {3}, "b"],
[{3}, {1}, {3}, "a"],
[{5}, {4}, {3}, "b"],
[{6}, {5}, {3}, "b"],
[{6}, {6}, {3}, "a"],
[{6}, {3}, {3}, "b"]]
]

for dataSet in dataSets:
    data = copy.deepcopy(dataSet)
    previousRules = []
    for i in range(0,10):
        print(i)
        random.shuffle(data)
        rules = ruleExtraction(data,1)
        flag = 0
        for rule in rules:
            if rule not in previousRules:
                flag = 1
        if i > 0 and flag == 1:
            print('fuck')
            print('previousRules', previousRules)
            print('rules', rules)
            break
        previousRules = rules

