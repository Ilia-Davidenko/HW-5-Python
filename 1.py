#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


from ntpath import join


file = open('abvgd.txt', 'r', encoding='utf-8')
data = file.read()
text = data.split(' ')
file.close()

del_bool = 'абв'
new_text = []

for i in text:
    if del_bool not in i:
        new_text.append(i)
new_text = ' '.join(new_text)
print(new_text)
    