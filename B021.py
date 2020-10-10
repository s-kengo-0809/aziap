'''
英語の文法チェック、入力された単語に対して、正しく複数形に変換するシステムの構築
＜入力例＞
3
dog
cat
studies

＜出力例＞
dogs
cats
studies

<結果>
ミスなし
if文に関して、もうちょっとまとめれそう
'''


N = int(input())

# word = []
# for i in range(N):
#     word.append(input())
# word = [input() for i in range(N)]      #成長 & appendを使わずにかけた(結局今回は使わなかったけど)

for i in range(N):
    word = input()
    
    if word[-1] == 's' or word[-2:] == 'sh' or word[-2:] == 'ch' or word[-1] == 'o' or word[-1] == 'x':
        word += 'es'
    elif word[-1] == 'f':
        word = word[:-1] + 'ves'
    elif word[-2:] == 'fe':
        word = word[:-2] + 'ves'
    elif word[-1] == 'y' and word[-2] not in "aeiou":
        word = word[:-1] + 'ies'
    else:
        word += 's'
        
    print(word)
