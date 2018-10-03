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
#Rules = [[{1},{1},{3},'a'],[{2},{1},{3},'a'],[{3},{2},{2},'a']]

#     Experiment 1 presets tiempos de aguacero
Rules = [
[{200},{159},{0.2},{161},{0.4},{160},{0.5},{0.27},{200},{159},{0.01},{150},{0.3},{161},{0.5},{0.001},'intro'],
[{200},{150},{0.23},{150},{0.3},{160},{0.5},{0.3},{200},{150},{0.01},{150},{0.3},{160},{0.5},{0.01},'intro'],
[{200},{150},{0.26},{150},{0.3},{160},{0.4},{0.36},{200},{150},{0.001},{150},{0.3},{160},{0.4},{0.01},'intro'],
[{200},{159},{0.2},{150},{0.3},{161},{0.5},{0.3},{200},{159},{0.01},{150},{0.3},{161},{0.5},{0.001},'intro'],

[{20},{150},{0.25},{101},{0.3},{102},{0.5},{0.33},{20},{150},{0.01},{101},{0.3},{102},{0.5},{0.01},'main'],
[{200},{150},{0.28},{150},{0.6},{160},{0.4},{0.38},{200},{150},{0.01},{150},{0.6},{160},{0.4},{0.01},'main'],
[{100},{100},{0.25},{100},{0.6},{102},{0.4},{0.33},{100},{100},{0.25},{100},{0.6},{102},{0.4},{0.33},'main'],

[{100},{100},{0.25},{100},{0.6},{102},{0.4},{0.28},{0},{0},{0},{0},{0},{0},{0},{0},'break'],
[{440},{880},{0.2},{660},{0.3},{661},{0.5},{0.25},{0},{0},{0},{0},{0},{0},{0},{0},'break'],

[{440},{660},{0.2},{441},{0.3},{661},{0.4},{0.22},{0},{0},{0},{0},{0},{0},{0},{0},'end'],
[{220},{440},{0.2},{660},{0.3},{221},{0.5},{0.23},{0},{0},{0},{0},{0},{0},{0},{0},'end'],
[{110},{240},{0.2},{330},{0.3},{221},{0.5},{0.23},{0},{0},{0},{0},{0},{0},{0},{0},'end'],
[{440},{660},{0.2},{165},{0.3},{221},{0.5},{0.23},{0},{0},{0},{0},{0},{0},{0},{0},'end']
]



Rules = [
#    datos para el blip extraidos por lina
[{ 15.830774841703}, {3.7286417219032}, {0.25566414744665}, '1' ], 
[{ 30.17095810902}, {3.7286417219032},  {0.25566414744665}, '2' ], 
[{ 54.92009003464}, {3.7286417219032},  {0.25566414744665}, '2' ], 
[{ 94.018248923402}, {3.7286417219032}, {0.25566414744665}, '3' ], 
[{ 154.5799317639}, {3.7286417219032},  {0.25566414744665}, '3' ], 
[{ 188.58593573556}, {3.7286417219032}, {0.25566414744665}, '3' ], 
[{ 188.58593573556}, {6.3618722599916}, {0.25566414744665}, '2' ], 
[{ 188.58593573556}, {20},              {0.25566414744665}, '2' ], 
[{ 188.58593573556}, {28.400374548492}, {0.25566414744665}, '2' ], 
[{ 134.22679449727}, {28.400374548492}, {0.25566414744665}, '2' ], 
[{ 89.07363977731}, {28.400374548492},  {0.25566414744665}, '2' ], 
[{ 31.172986723209}, {28.400374548492}, {0.25566414744665}, '1' ], 
[{ 31.172986723209}, {34.29296786778},  {0.25566414744665}, '1' ], 
[{ 31.172986723209}, {59.785917847597}, {0.25566414744665}, '1' ], 
[{ 70}, {59.785917847597}, { 0.25566414744665}, ' 2' ], 
[{ 70}, {59.785917847597}, { 0.12388781940694}, ' 2' ], 
[{ 70}, {59.785917847597}, { 0.067314763025783},' 2' ], 
[{ 37}, {19.646362769912}, { 0.24176269236384}, ' 1' ], 
[{ 37}, {0}, {0.24176269236384}, '3' ],
[{ 37}, {33.14944629048}, {0.24176269236384}, '2' ], 
[{ 37}, {100}, {0.24176269236384}, '1' ] ,
[{ 141.22229230154}, {100}, {0.24176269236384}, '3' ],
[{ 141.22229230154}, {43.044743106751}, {0.24176269236384}, '2' ], 
[{ 141.22229230154}, {47.35}, {0.24176269236384}, '2' ] ,
[{ 45.785232368163}, {47.35}, {0.24176269236384}, '1' ], 
[{ 45.785232368163}, {76.627436182189},{ 0.24176269236384}, '1' ], 
[{ 65.728741117097}, {76.627436182189},{ 0.24176269236384}, '1' ], 
[{ 86.039330858851}, {76.627436182189},{ 0.24176269236384}, '2' ], 
[{ 86.039330858851}, {76.627436182189},{ 0.057070321322205}, '2'], 
[{ 55.712418923309}, {76.627436182189},{ 0.057070321322205}, '1'], 
[{ 55.712418923309}, {34.170199794742},{ 0.14215325121246},  '2'], 
[{ 104.56838683546}, {34.170199794742},{ 0.14215325121246}, '2' ], 
[{ 104.56838683546}, {19},             { 0.14215325121246}, '2' ], 
[{ 149.09506331088}, {19},             { 0.14215325121246}, '2' ], 
[{ 149.09506331088}, {100},            { 0.14215325121246}, '1' ] 
]


#----------------------------------------------------------------------
#		some data to test the fuzzy classifier
#
Rules = [
	[{5},{2},'a'],
	[{1},{2},'a'],
	[{1},{4},'a'],
	[{5},{4},'a'],
	[{2},{3},'b']
]
#----------------------------------------------------------------------


#print('Rules',Rules)
#d = 1; print('d',d)
#rules = ruleExtraction(Rules,d,1/4)
#print('Rules',Rules)
#print('-----------------------------------')
#print('Rules',Rules)
d = 2; ratio = 0; print('d',d, '---', 'ratio',ratio)
#d = 12; ratio = 1/16; print('d',d, '---', 'ratio',ratio)
#d = 15; ratio = 0; print('d',d, '---', 'ratio',ratio)
rules = ruleExtraction(Rules,d,ratio)
print(' these are the extracted rules: ')
[print(rule) for rule in rules]
#print('Rules',Rules)
#d = 14; print('d',d)
#rules = ruleExtraction(Rules,d,1/10)








