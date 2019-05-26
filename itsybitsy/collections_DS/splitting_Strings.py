import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

result = re.split(r'[;,\s]\s*', line)
print(result)


# the separator is either a comma (,),semicolon (;), or whitespace
# followed by any amount of extra whitespace

text1 = '11/27/2012'
if re.match(r'\d+/\d+/\d+', text1):
    print("Match")
else:
    print("No match")

datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

result = datepat.findall(text)
print(result)

text = 'yeah, but no, but yeah, but no, but yeah'
print(text)
text = text.replace('yeah', 'yep')
print(text)
