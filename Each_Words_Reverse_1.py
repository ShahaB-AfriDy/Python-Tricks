def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

print(reverse_words("Equal != equal"))