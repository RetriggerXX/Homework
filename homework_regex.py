import re

#1
pattern = r"cat"
texts = ['mycatnip','I love dogs','i hate cat']
for text in texts:
    print(re.search(pattern, text))

#2
pattern = r"z...z"
texts = ['zaza','zackziel','zzz...']
for text in texts:
    print(re.search(pattern, text))

#3
pattern = r"^(8|9)\d{9}$"
texts = ['8800555353','1234567890','87654333']
for text in texts:
    print(re.match(pattern, text))

#4
pattern = r"\b[ауеои]\w*"
text = 'Как начинаеться расказ безрукого мальчика? "- иду я значит, никого не трогаю"'
print(re.findall(pattern,text))

#5
pattern = r"(\d+|-\d+)"
text = 'мышь считала дырке в сыре - 3+2 = 4, но мне нужно проверить еще и отрицательные числа, поэтому -2 -456'
print(re.findall(pattern,text))

#6
pattern = r"human"
texts = ['I love my human','i hate humans']
for text in texts:
    print(re.sub(pattern,"computer", text))

#7
pattern = r"((0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-\d{4})"
text = '12-12-2025, 32-10-2003, 12-10-2000,'
for i in range(len(re.findall(pattern, text))):
    print(f"{re.findall(pattern,text)[i][0]}", end=", ")

#8
pattern = r"\b\S*b\w*"
text = '-say my name -hisenberg -you god damn right'
print(re.findall(pattern, text))

#9
pattern = r"(\w)\1+"
text = 'a ab aab bab babba'
print(re.sub(pattern, r"\1", text))