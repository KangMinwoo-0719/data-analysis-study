import xml.etree.ElementTree as et

x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""


book = et.fromstring(x_str)  #fromstring() :  str > XML file 변경 함수
# print(type(book))   # >> <class 'xml.etree.ElementTree.Element'>
# print(book.tag)    # >> 객체의 tag 속성 출력 : 부모 Element 이름 확인 쉬움

book_childs = list(book)
# print(book_childs)


# name, author, year = book_childs    #자식 Element를 각각의 변수에 삽입
# print(name.text)
# print(author.text)
# print(year.text)
'''
ㄴ 하지만 자식 Element가 항상 순서대로 있지 않기 때문에
위 코드는 조금 위험도가 높음
'''

name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')
'''
ㄴ findtext() : 부모 객체의 해당하는 자식 Element를 텍스트에 맞게 탐색하여 자동으로 반환해 줌
'''
# print(name)
# print(author)
# print(year)

x2_str = """
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼자 공부하는 머신러닝 + 딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""
'''
ㄴ books 라는 부조 엘리먼트 안에 book 이라는 동일한 이름의 자식 엘리먼트가 있음
'''

books = et.fromstring(x2_str)
# ㄴ부모 엘리먼트

for book in books.findall('book'):
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')

    print(name)
    print(author)
    print(year)
    print()
'''
ㄴ findall() : 동일한 이름을 가진 여러 자식 엘리먼트를 찾을 때 쓰는 메서드
   + for 문과 함께 사용하면 매우 편리
'''