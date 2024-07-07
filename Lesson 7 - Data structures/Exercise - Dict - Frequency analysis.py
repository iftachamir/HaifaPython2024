n = int(input())

# Build word-frequency dictionary
word_freq_dict = {}
for i in range(n):
  line = input()
  line_list = line.split()
  for each_word in line_list:
    if each_word in word_freq_dict.keys():
      word_freq_dict[each_word] += 1
    else:
      word_freq_dict[each_word] = 1

# Restructure to frequency-words dictionary
freq_words_dict = {}
for each_key in word_freq_dict.keys():
  freq = word_freq_dict[each_key]
  if freq in freq_words_dict.keys():
    freq_words_dict[freq].append(each_key)
  else:
    freq_words_dict[freq] = [each_key]

# Go over frequencies, then go over words, and print
sorted_freq = list(sorted(freq_words_dict.keys(), reverse=True))
for each_freq in sorted_freq:
  words_in_freq = freq_words_dict[each_freq]
  for each_word in sorted(words_in_freq):
    print(each_word, each_freq)