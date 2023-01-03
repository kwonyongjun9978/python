'''
1.for
for value in []:
    print(value)
'''
names = ['kwon', 'yong', 'jun'] #list
for name in names:
    print('Hello, '+name+' . Bye, '+name+'.')


#2.다차원배열(리스트)의 처리
persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]
print(persons[0][0])

for person in persons:
    print(person[0]+','+person[1]+','+person[2])
 
person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)
 
name, address, interest = ['egoing', 'Seoul', 'Web']
print(name, address, interest)
 
for name, address, interest in persons:
    print(name+','+address+','+interest)


#3.사전형(dictionary)
person = {'name':'egoing', 'address':'Seoul', 'interest':'Web'}  #name=key, egoing=value
print(person['name'])
 
for key in person:
    print(key, person[key]) #person[key]=value값을 가져온다
 
persons = [
    {'name':'egoing', 'address':'Seoul', 'interest':'Web'},
    {'name':'basta', 'address':'Seoul', 'interest':'IOT'},
    {'name':'blackdew', 'address':'Tongyeong', 'interest':'ML'}
]
 
print('==== persons ====')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-----------------')      