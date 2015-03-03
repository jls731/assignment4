'''

@author: JLS731 (Joseph Song)

Assignment #4: Answer to question #8
'''

new_dict = {'first':[2,1], 'second':[2,3], 'third':[3,4]}

'a) store first and third values and swap values'
a = new_dict['first']
b = new_dict['third']

new_dict['first'] = b
new_dict['third'] = a

'b) Sort the elements of the list with key third'
c = new_dict['third']
c.sort()
new_dict['third'] = c

'c) Add a new key fourth with the value of the key second'
new_dict['fourth'] = new_dict['second']

'd) Delete the key/vaue pair second'
del new_dict['second']

print new_dict