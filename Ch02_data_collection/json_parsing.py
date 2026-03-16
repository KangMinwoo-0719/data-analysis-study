import json
import pandas as pd
import gdown


d = {"name" : "혼자 공부하는 데이터 분석"}

# json.dumps() : python object > json txt 형식 변환
d_str = json.dumps(d, ensure_ascii=False)   


#json.loads() : json txt > python object 변환
d2 = json.loads(d_str)

d3 = json.loads('{"name" : "혼자 공부하는 데이터 분석", "author" : ["박해선", "홍길동"], \"year" : 2022}')
print(d3['author'][1])



d4_str = """
[
    {"name" : "혼자 공부하는 데이터 분석", "author" : "박해선", "year" : 2022},
    {"name" : "혼자 공부하는 머신러닝 + 딥러닝", "author" : "박해선", "year" : 2020} 
]
"""

# pd.read_json(d4_str) #json txt > data frame
d4 = json.loads(d4_str)
#   ㄴ read.json()에서 괄호 안 변수를 file name으로 인식하여 OS Error가 발생하는 경우가 있음


#파이썬 객체로 변환한 d4를 dataFrame으로 전환하기
pd.DataFrame(d4)  


# print(d4[0]['year'])

gdown.download('https://bit.ly/3q9SZix', '20s_best_book.json', quiet=False)
#  ㄴ검색 결과 페이지 html 가져오기

# json 파일로 읽어오기
books_df = pd.read_json('20s_best_book.json')

# books_df 의 'no' 열부터 'isbn13'열 까지만 선택 
books = books_df.loc[:, 'no' : 'isbn13']
print(books.head())