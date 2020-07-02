'''
Leet文字列
特定の文字列を数字に変換する
'''

word = input()
word = word.replace('A','4').replace('E','3').replace('G','6').replace('I','1').replace('O','0').replace('S','5').replace('Z','2')
print(word)
