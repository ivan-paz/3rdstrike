from searchPatterns import iterate
def createCategoriesDict(Rules):
    dictionary_of_classes = dict()
    for rule in Rules:
        rule_class = rule[-1]
        if rule_class not in dictionary_of_classes:
            dictionary_of_classes[rule_class] = []
            dictionary_of_classes[rule_class].append(rule)
        else:
            dictionary_of_classes[rule_class].append(rule)
    return dictionary_of_classes
#-----------------------------------------------------------------------------
def getCategory(key,dictionary_of_classes):
    rules_other_classes = []
    for key1 in dictionary_of_classes:
        if key1 != key:
            for r in dictionary_of_classes[key1]:
                rules_other_classes.append(r)
        else:
            rules_current_class = dictionary_of_classes[key]
    return [rules_current_class, rules_other_classes]
#-----------------------------------------------------------------------------
def ruleExtraction(Rules,d):
    finalRules = []
    categoriesDict = createCategoriesDict(Rules)
    for category in categoriesDict:
        print('category',category)
        [rulesCurrentCategory,otherRules] = getCategory(category,categoriesDict) 
        rules = iterate(rulesCurrentCategory,d)
        [finalRules.append(rule) for rule in rules]
    [print(r) for r in finalRules]
    return finalRules


Rules = [
[{3}, {3}, {6}, 'a'],
[{4}, {3}, {6}, 'a'],
[{3}, {4}, {6}, 'a'],
[{6}, {1}, {6}, 'a'],
[{1}, {5}, {6}, 'a'],
[{1}, {3}, {6}, 'a'],
[{3}, {2}, {6}, 'a'],
[{4}, {2}, {6}, 'b'],
[{5}, {4}, {6}, 'b'],
[{2}, {2}, {6}, 'b'],
[{5}, {3}, {6}, 'b'],
[{1}, {4}, {6}, 'a'],
[{2}, {1}, {6}, 'b'],
[{2}, {5}, {6}, 'b'],
[{1}, {2}, {6}, 'a']
]
ruleExtraction(Rules,1)
