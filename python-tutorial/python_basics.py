#숫자형 데이터 타입
print(-1)
print(0)
print(1) #int
print(1.1) #float
print('1+1', 1+1)
print('2-1', 2-1)
print('2*2', 2*2)
print('4/2', 4/2)

import math #math 라고하는 수학과 관련된 여러가지 기능을 가진 모듈을 import(로딩)한다.
print('math.sqrt(4)', math.sqrt(4)) #재곱근 구하기
print('math.pow(4,2)', math.pow(4,2)) #재곱 구하기

import random #random 라고하는 랜덤과 관련된 여러가지 기능을 가진 모듈을 import(로딩)한다.
print('random.random()',random.random()) #랜덤값 구하기


#문자열 데이터 타입(string)
print('Hellow world')
print("Hellow world")
print('''
      Hello
      world
      ''')
print("""
      Hello
      world
      """)
print("'1'+'1'",'1'+'1')
print('Hello world'*100) #100번 출력
print("len('Hello world'*100)", len('Hello world'*100)) #글자수
print("'Hellow world'.replace('world', 'universe')",'Hellow world'.replace('world', 'universe')) #문자 변경


#리스트 데이터 타입
students=["egoing","sori","maru"]
grades=[2,1,4]
print("students[1]",students[1])
print("len(students)",len(students)) #원소 개수
print("min(grades)",min(grades)) #원소 중에서 가장 작은값 출력
print("max(grades)",max(grades)) #원소 중에서 가장 큰값 출력

import statistics
print('statistics.mean(grades)',statistics.mean(grades)) #mean=평균

print("random.choice(students)",random.choice(students)) #랜덤으로 students원소들중 하나를 출력

#https://docs.python.org/3/(메뉴얼)


#변수
name='jun'
message='hi, '+name+'... bye, '+name+'.'
print(message)


#입력과 출력
name=input('name: ')
message='hi, '+name+'... bye, '+name+'.'
print(message)


#pypi
#표준 라이브러리 = 내장 모듈 ex)math, statistics 등, 패키지 = 외부 개발자들이 만든 모듈(소프트웨어), pypi(python package index) = 파이썬 패키지를 모아 놓은 데이터베이스, pip = 패키지를 pypi.org를 통해 import하는 프로그램
import pandas
house=pandas.read_csv('house.csv')
print(house)
print(house.head()) #앞쪽에 있는 데이터 5개만 출력
print(house.head(2)) #앞쪽에 있는 데이터 2개만 출력
print(house.describe()) #각각의 컬럼에대한 성격을 파악하고싶을때(표에대한 정보를 묘사)







