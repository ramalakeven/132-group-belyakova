def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Введите предложение: ")
word_count = count_words(sentence)
print("Число слов:", word_count)
