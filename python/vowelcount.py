s="hi im a good boy"
s.lower()
li=[]
vowel_count=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        li.append(i)
        vowel_count+=1
print(vowel_count)
print(li)