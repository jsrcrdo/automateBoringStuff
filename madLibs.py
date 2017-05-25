#!/usr/bin/python3
# madLibs.py - 
import re

fObj = open('panda.txt')
content = fObj.read()
regex = re.compile('ADJECTIVE|NOUN|VERB')

for i in range(len(regex.findall(content))): # times ADJECTIVE|NOUN|VERB appear
	mo = regex.search(content)
	if mo.group() == 'ADJECTIVE':
		print('Enter an adjective:')
		adj = input()
		content = re.sub('ADJECTIVE', adj, content, count=1)
	elif mo.group() == 'NOUN':
		print('Enter a noun:')
		noun = input()
		content = re.sub('NOUN', noun, content, count=1)
	elif mo.group() == 'VERB':
		print('Enter a verb:')
		verb = input()
		content = re.sub('VERB', verb, content, count=1)

fObj.close()
print(content)
