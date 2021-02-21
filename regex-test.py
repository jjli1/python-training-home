import re

# pattern1='cat'
# pattern2='bird'
# string='dog runs to cat'
# print(pattern1 in string)
# print(pattern2 in string)

# print(re.search(pattern1,string))
# print(re.search(pattern2,string))

# multiple patterns ('run' or 'ran')
# ptn='r[au]n'
# print('ptn=',ptn)
# print(re.search(ptn,'dog ran to cat'))
string = '臺中市南屯區埔興段11-1地號'
# regex = re.compile(r'段(\d+-*\d*)')
# match = regex.search(string)
# print(match.group(1))

print(re.search(r'段(\d+-*\d*)', string).group(1))
