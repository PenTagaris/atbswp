#!/bin/python3

birthdays = {'Alice': 'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
while True:
	print ('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print('{0} is the birthday of {1}'.format(birthdays[name], name))
	else:
		#print ('I do not have birthday information for ' + name)
		print ('What is their birthday?')
