import re

# pattern1='cat'
# pattern2='bird'
# string='dog runs to cat'
# print(pattern1 in string)
# print(pattern2 in string)

# print(re.search(pattern1,string))
# print(re.search(pattern2,string))

# multiple patterns ('run' or 'ran')
ptn='r[au]n'
print('ptn=',ptn)
print(re.search(ptn,'dog ran to cat'))