from ruleExtraction import ruleExtraction
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

#Rules = [
#[{3}, {2}, {5}, 'b'],
#[{3}, {1}, {5}, 'a'],
#[{1}, {2}, {5}, 'b'],
#[{3}, {4}, {5}, 'b'],
#[{1}, {6}, {5}, 'a'],
#[{6}, {2}, {5}, 'b'],
#[{4}, {5}, {5}, 'a'],
#[{2}, {2}, {5}, 'b'],
#[{4}, {1}, {5}, 'b'],
#[{2}, {6}, {5}, 'b'],
#[{5}, {2}, {5}, 'a'],
#[{2}, {1}, {5}, 'b'],
#[{6}, {3}, {5}, 'a'],
#[{4}, {4}, {5}, 'a'],
#[{1}, {1}, {5}, 'a']
#]
#Rules = [[{3}, {2, 4}, {5}, 'b'], [{2, 4}, {1}, {5}, 'b'], [{1, 2, 3}, {2}, {5}, 'b'],[{2, 3, 6}, {2}, {5}, 'b'], [{2}, {1, 2, 6}, {5}, 'b']]

#Rules = [[{6}, {1}, {6}, 'a'], [{1, 3, 4}, {3}, {6},'a'], [{3}, {2, 3, 4}, {6}, 'a'],[{1, 3}, {2, 4}, {6}, 'a'], [{1}, {2, 3, 4, 5}, {6}, 'a']]

#  Testing 3rdstrike v.s Rulex
Rules = [
[{1},{2}, {6}, 'a'],
[{6},{5}, {6}, 'a'],
[{5},{4}, {6}, 'b'],
[{6},{6}, {6}, 'b'],
[{5},{3}, {6}, 'b'],
[{6},{3}, {6}, 'b'],
[{6},{4}, {6}, 'a'],
[{4},{5}, {6}, 'b'],
[{5},{5}, {6}, 'b'],
[{1},{1}, {6}, 'b'],
[{4},{1}, {6}, 'b'],
[{2},{5}, {6}, 'a']]

Rules = [ # test3
[{2}, {3}, {2}, 'b'],
[{3}, {2}, {2}, 'b'],
[{6}, {5}, {2}, 'b'],
[{4}, {6}, {2}, 'a'],
[{4}, {2}, {2}, 'a'],
[{1}, {1}, {2}, 'b'],
[{5}, {5}, {2}, 'a'],
[{2}, {2}, {2}, 'b'],
[{4}, {5}, {2}, 'b'],
[{2}, {1}, {2}, 'a'],
[{3}, {4}, {2}, 'a'],
[{4}, {4}, {2}, 'a'],
[{3}, {6}, {2}, 'b'],
[{6}, {6}, {2}, 'a']]

Rules = [ #test5
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
[{3}, {5}, {2}, 'a']]
Rules = [ #test6
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
#-------------------------------------------------------------------------------
#   t e s t s   d o c u m e n t a t i o n    d = 1
#Rules = [ [{1},{2},'a'], [{2},{2},'a'],[{2},{3},'a'] ] 
#d = 1; ratio = 0
#ruleExtraction(Rules,d,ratio)


##-     d o c u m e n t a t i o n    t e s t i n g   d >= 2
#Rules = [ [{1},{2},'a'], [{2},{2},'a'], [{2},{3},'a'], [{1},{3},'b'] ]
## [{1},{3},'b'] contradicts one rule in [ {1,2}, {2,3}, 'a']
## So this rule can not be formed
#d = 2; ratio = 1/2
#ruleExtraction(Rules,d,ratio)
#
#print('--------------- second rules -----------')
## there are no contradictions for rule [{1,2}, {2,3}, 'a']
## and ratio = 1/2 i.e at least 2 of 4
#Rules = [ [{1},{2},'a'], [{2},{2},'a'], [{2},{3},'a'] ]
#d = 2; ratio = 1/2
#ruleExtraction(Rules,d,ratio)
#
#  I F ratio = 4/5 rule [{1,2},{2,3},'a'] can not be created
#print(' ratio 4/5')
#Rules = [ [{1},{2},'a'], [{2},{2},'a'], [{2},{3},'a'] ]
#d = 2; ratio = 4/5
#ruleExtraction(Rules,d,ratio)
##
#print('------------- third rules ---------------')
#Rules = [ [{1},{2},'a'],[{2},{2},'a'], [{2},{3},'a'],[{1},{3},'b'] ]
#d = 2; ratio = 1/2
#ruleExtraction(Rules,d,ratio)

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#---------------      THIS IS THE DRAFT FOR THE INTERACTIVE ALGORITHM
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#    draft for the interactive algorithm
#print(Rules)
#number_of_parameters = len(Rules[0])
#ratio = 1/2
#for d in range(1,number_of_parameters):
#    print(d)
#    print(Rules)
#    rules = ruleExtraction(Rules,d,ratio)
#    print(rules)
Rules = [[{1},{1},{3},'a'],[{2},{1},{3},'a'],[{3},{2},{2},'a']]
print('Rules',Rules)
d = 1; print('d',d)
rules = ruleExtraction(Rules,d,1/2)
print('Rules',Rules)
print('-----------------------------------')
print('Rules',Rules)
d = 2; print('d',d)
rules = ruleExtraction(Rules,d,1/2)
#print('rules',rules)
print('Rules',Rules)
d = 3; print('d',d)
rules = ruleExtraction(Rules,d,1/4)

