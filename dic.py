student = {
    "name": "Alice",
    "age": 23,
}
print(student)
print(student["name"])
student.age=24

s="hareesh is a good boy"      #frequency count 
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)

s="hareesh is a good boy"      #vowel count
d={}
for ch in s:
    if ch in 'aeiou':
        d[ch]=d.get(ch,0)+1
print(d)

s="hareesh is a good boy"      #constant count
d={}
for ch in s:
    if ch not in 'aeiou':
     d[ch]=d.get(ch,0)+1
print(d)

def dic(s):
    d={}
    d1={}
    d2={}
    for ch in s:
           d[ch]=d.get(ch,0)+1
    print(d)
    for ch in s:
        if ch in 'aeiou':
            d1[ch]=d1.get(ch,0)+1
    print(d1)
    for ch in s:
        if ch not in 'aeiou':
            d2[ch]=d2.get(ch,0)+1
    print(d2)
s="hareesh"
dic(s)
student = {
    "name": "Alice",
    "age": 23,
}
print(student["name"])
print(student.get("age"))

