def specialChar(text) :
    if '-' in text or '[' in text or ']' in text or '{' in text or '}' in text or '!' in text or ';' in text or ':' in text or '%' in text or '&' in text or '<' in text or '>' in text or '.' in text or ',' in text or '!' in text or '?' in text or '(' in text or '*' in text or "'" in text or '"' in text or '/' in text or ')' in text or '$' in text or '©' in text or '+' in text or '=' in text:
        return True
    else:
        return False
#TEST   if spechar(word) is True:
#           print(word, ' has a special character')
#       else:
#           print(word, ' does not have a special character')
#       print(length[word])


file = input('What file do you want to open? ')
try:
    handle = open(file, encoding="utf8")
except :
    print(' That file cannot be found or opened')
    quit()


counts = dict()
length = dict()
for line in handle: # I don't know why I can interact with this file only in this way
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # This dictionary keeps track of the number of occurrences of words in the file.
        length[word] = length.get(word, len(word)) # This dictionary keeps track of the lengths of words in the file

freqvalue = None
freqkey = None
longvalue = None
longkeys = dict()

for key, value in counts.items():
    if freqvalue is None or value > freqvalue:
        freqkey = key
        freqvalue = value

for key, value in length.items():
    freq = counts[key]
    if specialChar(key) is False:
        if value is longvalue: #if the current word is same length as the longsest word so far,
            longkeys[key] = freq # add the current word to the list of longest words

        if (longvalue is None or value > longvalue): #if the current word is greater than the longest word so far
            longvalue = value # the current word is the new longest word
            longkeys.clear() # the list of old longest words is deleted
            longkeys[key] = freq  # the list of new longest word is started with the current word

print('In the file with the handle: \n ',handle)
print('The most common word is: \n', "'", freqkey,"'", ' with ', freqvalue, ' occurrences \n')
print('The longest words are:')
for key, value in longkeys.items():
    if value == 1 :
        print( "'", key, "'", 'which is', length[key], "characters long and occurs on", value, "occasion " )
    else:
        print( "'", key, "'", 'which is', length[key], "characters long and occurs on", value, "occasions " )