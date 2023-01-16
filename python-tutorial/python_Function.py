#함수
print('Hello world')      
print(len('Hello world')) 
#print,len = python에 내장되어 있는 함수

#ABC를 출력하는 함수 만들기
def ABC():
    print('A')
    print('B')
    print('C')     
ABC()
print(1)
ABC()
print(2)
ABC()
print(3)

#함수에 입력값을 만들고 다르게 동작하는 함수 만들기
def get_vat(price, vat_rate=0.1): #price라는 변수(매개변수,parameter)만들기
    return price*vat_rate
print(get_vat(10000)) #10000 = 인자(argument)    
#email.send('rnsuz74@naver.com', get_vat(20000,0.3)) #rnsuz74@naver.com로 실행한 결과를 전송함
                                                     #but, email.send는 동작하지 않는 코드이다.
                            

