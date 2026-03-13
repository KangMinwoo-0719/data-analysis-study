import json
import pandas as pd


d = {"name" : "혼자 공부하는 데이터 분석"}

d_str = json.dumps(d, ensure_ascii=False)   
# json.dumps() : python object > json txt 형식 변환
print(type(d_str))

d2 = json.loads(d_str)
#json.loads() : json txt > python object 변환
print(d2['name'])
print(type(d2))


d3 = json.loads('{"name" : "혼자 공부하는 데이터 분석", "author" : ["박해선", "홍길동"], \"year" : 2022}')
print(d3['author'][1])



d4_str = """
[
    {"name" : "혼자 공부하는 데이터 분석", "author" : "박해선", "year" : 2022},
    {"name" : "혼자 공부하는 머신러닝 + 딥러닝", "author" : "박해선", "year" : 2020} 
]
"""
d4 = json.loads(d4_str)
# pd.read_json(d4_str) #json txt > data frame
#   ㄴ read.json()에서 괄호 안 변수를 file name으로 인식하여 OS Error가 발생하는 경우가 있음

pd.DataFrame(d4)  #파이썬 객체로 변환한 d4를 dataFrame으로 전환하기


# print(d4[0]['year'])