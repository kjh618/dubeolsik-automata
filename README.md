# 두벌식 오토마타 (Dubeolsik Automata)
![GitHub repo size](https://img.shields.io/github/repo-size/kjh618/dubeolsik-automata)

간단한 두벌식 한글 입력 오토마타

A simple Dubeolsik Hangul input automata

## 예시 (Examples)
```python
>>> from dubeolsik_automata import join_jamos, qwerty_to_dubeolsik
>>> qwerty_to_dubeolsik('dkssud')
'ㅇㅏㄴㄴㅕㅇ'
>>> join_jamos('ㅇㅏㄴㄴㅕㅇ')
'안녕'
```

## 설치 (Install)
* `pip install dubeolsik-automata`
* PyPI: https://pypi.org/project/dubeolsik-automata/
* Or just download `dubeolsik_automata/dubeolsik_automata.py`. (There are no dependencies.)

## 사용 방법
* 함수 `qwerty_to_dubeolsik(qwerty)`: 퀴티 키 입력 리스트 `qwerty`를 두벌식 기준 한글 자모로 변환한 문자열 리턴
* 클래스 `HangulCharacter`: 한글 한 글자를 나타냄. `join_jamos`에서 내부적으로 사용
* 함수 `join_jamos(keys)`: 두벌식 키 입력 리스트 `keys`를 키보드로 친 것처럼 합친 문자열 리턴

## (How to Use)
* Function `qwerty_to_dubeolsik(qwerty)`: Converts a list `qwerty` of Qwerty key inputs to a Hangul jamo string based on Dubeolsik layout, and returns it.
* Class `HangulCharacter`: Represents one Hangul character. Used internally by `join_jamos`.
* Function `join_jamos(keys)`: Joins a list `keys` of Dubeolsik key inputs to a string as if it was typed on a keyboard, and returns the result.
