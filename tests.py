def assert_eq(left, right):
    if left == right:
        print('PASS: {} == {}'.format(left, right))
    else:
        assert False, 'FAIL: {} != {}'.format(left, right)
        
from dubeolsik_automata import qwerty_to_dubeolsik, join_jamos, HangulCharacter

print('[qwerty_to_dubeolsik]')
assert_eq(qwerty_to_dubeolsik('dkssudgktpdy'), 'ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ')

print('\n[HangulCharacter]')
assert_eq(HangulCharacter('ㅇ','ㅏ','ㄴ').join(), '안')

print('\n[join_jamos]')
print(' [Simple Test]')
assert_eq(join_jamos('ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ'), '안녕하세요')
assert_eq(join_jamos('ㅌㅔㅅㅡㅌㅡ'), '테스트')
assert_eq(join_jamos('ㄱㅣㅅㅁㅏㅅㅡㅌㅓ'), '깃마스터')
assert_eq(join_jamos('ㅂㅜㅔㄹㄱㄲㅗㅣㄹㅂㄸㅜㅣㄹㅎ'), '뷁꾋뛿')
assert_eq(join_jamos('ㅇㅏㄴ'), '안')
assert_eq(join_jamos('ㅎㅗㄹㅅㅜ'), '홀수')

print(' [Sentence Test]')
assert_eq(join_jamos('ㄷㅏㄹㅏㅁㅈㅜㅣ ㅎㅓㄴ ㅊㅔㅅㅂㅏㅋㅜㅣㅇㅔ ㅌㅏㄱㅗㅍㅏ.'), '다람쥐 헌 쳇바퀴에 타고파.')

print(' [Edge Case]')
assert_eq(join_jamos(''), '')
assert_eq(join_jamos('.'), '.')
assert_eq(join_jamos('  '), '  ')
assert_eq(join_jamos('ㄱ'), 'ㄱ')
assert_eq(join_jamos('ㅏ'), 'ㅏ')
assert_eq(join_jamos('ㅏㅏㅣ'), 'ㅏㅏㅣ')
assert_eq(join_jamos('ㅏㄱ'), 'ㅏㄱ')
assert_eq(join_jamos('ㄱㅏㄱ ㅏ'), '각 ㅏ')
