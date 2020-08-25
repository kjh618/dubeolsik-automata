def assert_eq(left, right):
    if left == right:
        print('PASS: {} == {}'.format(left, right))
    else:
        print('FAIL: {} != {}'.format(left, right))
        
from dubeolsik_automata import join_jamos

assert_eq(join_jamos('ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ'), '안녕하세요')
assert_eq(join_jamos('ㅌㅔㅅㅡㅌㅡ'), '테스트')
