# reaquests 패키지로 URL 호출 후 데이터 받기
import requests


url = "https://data4library.kr/api/itemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&" \
"age=20&authKey=3c1911db25b9b8dc63298008d0ad7e1de5cf2b5af0072d7e785e90acd2e3a879"


#FIXME : 도서관 정보나루 API 아직 미승인이므로 url 접속 불가능 / 승인까지 대기
# r = requests.get(url)
'''
ㄴ get()함수 return 값 : API 호출 결과 담고있는 requests package > Response class object
'''
data = r.json()
print(data)
# ㄴ json() : 웹으로부터 받은 JSON 문자열 > python object로 변환