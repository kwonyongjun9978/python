#Boolean
print(True)
print(False)

#비교연산자
print('1==1', 1==1)
print('1==2', 1==2)
print('1<2', 1<2)
print('1>2', 1>2)
print('1>=1', 1>=1)
print('2>=1', 2>=1)
print('1!=1', 1!=1)

#조건문
'''
1. if boolean:
      code
'''
print(0)
if True:
    print(1) #tab키 사용
print(2)

print('---')

print(0)
if False:
    print(1) 
print(2)

input_id = input('id :')
id='jun'
if input_id == id:
    print('Welcome')

    
'''
2. if boolean:
      code
   else:
      code 
'''
print(0)
if True:
    print(1)
else:
    print(2)
print(3)

print('---')   

print(0)
if False:
    print(1)
else:
    print(2)
print(3)  

input_id = input('id :')
id='jun'
if input_id == id:
    print('Welcome')   
else:
    print('Who?') 
    

'''
3. if boolean:
      code
   elif boolean:
      code 
   else:
      code   
'''   
print(0)
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('---')

print(0)
if False:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('---')

print(0)
if False:
    print(1)
elif False:
    print(2)
else:
    print(3)
print(4) 

input_id = input('id : ')
id1 = 'jun'
id2 = 'yong'
if input_id == id1:
    print('Welcome')
elif input_id == id2:
    print('Welcome')
else:
    print('Who?')


#4.중첩조건문   
input_id = input('id:')
id = 'jun'
input_password = input('password:')
password = '9498'
'''
if input_id == id:
    if input_password == password:
        print('Welcome')
    else:
        print('Wrong password')
else:
    print('Wrong id') 
'''

if input_id == id and input_password == password:
    print('Welcome')