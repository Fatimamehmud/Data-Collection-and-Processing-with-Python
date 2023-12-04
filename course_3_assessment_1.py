# Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
yellow="yellow" in lst[2]
print(yellow)
    

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four=4 in lst[1]
print(four)        

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]  
orange = 'orange' in lst[0]
print(orange)

# Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1="hola" in L
print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2=[5, 8, 7] in L
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3=6.6 in L[2]
print(test3)

# Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data ="data" in nested.keys()
print(data)
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

twentyfour=24 in nested["data"]
print(twentyfour)
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole="whole" not in nested['window']
print(whole)
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics= " physics" in nested.keys()
print(physics)

# The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold=nested_d['London']['Great Britain']
print(london_gold)

# Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1=sports['swimming'][2]
print(v1)

# Assign the string 'platform' to the name v2
v2=sports['diving'][1]
print(v1)

# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3=sports['gymnastics']['women']
print(v3)
# Assign the string 'rings' to the name v4
v4='rings'

# Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
for olympic in nested_d:
    if 'USA' in nested_d[olympic]:
        US_count.append(nested_d [olympic]['USA'])

print(US_count)

