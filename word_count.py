import os

file = open(os.path.expanduser('~/Documents/Python/word_count_test.txt'), encoding="utf8", errors="ignore")

word_number = 0
line_number = 0
total_char_number = 0
mean_word_length = 0

for line in file:
    line = line.strip("\n")
    words = line.split()
    for i in range(len(words)):
        words[i] = words[i].strip(',')
        words[i] = words[i].strip('.')
        total_char_number += len(words[i])

    line_number += 1
    word_number += len(words)
    mean_word_length = total_char_number/word_number


print('line number: ' + str(line_number) + 
'\n' + 'word count: ' + str(word_number) +
'\n' + 'Mean word length ' + str(round(mean_word_length)))

file.close()