# 12. Check if a String is a Palindrome

def palin(word):
    word_together = ''
    n = -1
    reverse_list = []
    reverse_word = ''

    for l in word:
        if l != " ":
            word_together += l

    for l in word:
        reverse_list.append(word[n])
        n -= 1   
    
    for l in reverse_list:
        if l != " ":
            reverse_word += l
    
    if reverse_word.lower() == word_together.lower():
        return 'It is palindrome.'
    else:
        return 'It is not palindrome'


print(palin('Roma é amor'))