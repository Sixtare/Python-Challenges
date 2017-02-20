user_word = str(input('Digite sua palavra:'))
reversed_word = ''.join(reversed(user_word))

if user_word == reversed_word:
    print('A palavra é um palindromo')
else:
    print('A palavra nao é um palindromo')