def assert_eq(left, right):
    if left == right:
        print('PASS: {} == {}'.format(left, right))
    else:
        print('FAIL: {} != {}'.format(left, right))
        
from dubeolsik_automata import join_jamos, change_input_eng_kor, CurrentCharacter

assert_eq(join_jamos('ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ'), '안녕하세요')
assert_eq(join_jamos('ㅌㅔㅅㅡㅌㅡ'), '테스트')
assert_eq(join_jamos('ㄱㅣㅅㅁㅏㅅㅡㅌㅓ'), '깃마스터')

assert_eq(change_input_eng_kor('dkssudgktpdy'),'ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ')

character1 = CurrentCharacter('ㄱ','ㅘ','ㄹ','ㅎ')
assert_eq(character1.join(),'괋')