# 3-Создайте два списка — один с названиями языков программирования, другой
#  — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 1092, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (1092,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

from functools import reduce


def tuples(value, lang):
    return list(zip(value, lang))


def work(lst):
    for i in range(len(lst)-1, -1, -1):
        num = []
        for k in lst[i][1]:
            num.append(ord(k))
        if sum(num) % lst[i][0] == 0:
            lang = lst[i][1].upper()
            del lst[i]
            lst.insert(i, (reduce(lambda x, y: x + y, num), lang))
        else:
            del lst[i]
    return lst
        

languages = ['c#', 'java', 'python', 'c++', 'c', 'pascal', 'php']
nums = [1,2,3,4,5,6,7]
tup = tuples(nums, languages)
print(tup)
result = work(tup)
print(result)