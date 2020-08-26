# 두벌식 오토마타 (Dubeolsik Automata)
![GitHub repo size](https://img.shields.io/github/repo-size/kjh618/dubeolsik-automata)

파이썬으로 구현된 간단한 두벌식 한글 입력 오토마타

A simple Dubeolsik Hangul input automata implemented in Python

## 예시 (Examples)
```python
>>> from dubeolsik_automata import qwerty_to_dubeolsik, join_jamos
>>> qwerty_to_dubeolsik('dkssud')
'ㅇㅏㄴㄴㅕㅇ'
>>> join_jamos('ㅇㅏㄴㄴㅕㅇ')
'안녕'
```

## 설치 (Install)
* `pip install dubeolsik-automata`
* PyPI: https://pypi.org/project/dubeolsik-automata/
* Or just download `dubeolsik_automata/dubeolsik_automata.py`. (There are no dependencies.)

## 도큐멘테이션
* 함수 `qwerty_to_dubeolsik(qwerty)`: 퀴티 키 입력 리스트 `qwerty`를 두벌식 기준 한글 자모로 변환
* 클래스 `HangulCharacter`: 한글 한 글자를 나타냄. `join_jamos`에서 내부적으로 사용
* 함수 `join_jamos(keys)`: 두벌식 키 입력 리스트 `keys`를 키보드로 친 것처럼 합침

## (Documentation)
* Function `qwerty_to_dubeolsik(qwerty)`: Converts a list `qwerty` of Qwerty key inputs to a Hangul jamo string based on Dubeolsik layout.
* Class `HangulCharacter`: Represents one Hangul character. Used internally by `join_jamos`.
* Function `join_jamos(keys)`: Joins a list `keys` of Dubeolsik key inputs into a string as if it was typed on a keyboard.
