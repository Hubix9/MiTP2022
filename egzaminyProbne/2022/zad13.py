# I
# B
# E
# D
# A
# C
# G
# J
# F
# H

# teksty piosenek sciagnalem z googla

files = ['baby.txt', 'up.txt', 'sorry.txt', 'onetime.txt']
for filename in files:
    with open(filename, 'r') as infile:
        text = infile.read().lower()
        frequency = {}
        for word in text.split():
            frequency[word] = frequency.get(word, 0) + 1
        frequency_sorted = sorted(frequency, key=frequency.get)
        for key in reversed(frequency_sorted):
            print("{} : {}".format(key, frequency[key]))
