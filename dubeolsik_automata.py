from enum import Enum

KEY_JAEUM = set('ㅂㅈㄷㄱㅅㅁㄴㅇㄹㅎㅋㅌㅊㅍㅃㅉㄸㄲㅆ')
KEY_MOEUM = set('ㅛㅕㅑㅐㅔㅗㅓㅏㅣㅠㅜㅡㅒㅖ')

class State(Enum):
    START = 0
    CHOSEONG = 1
    JUNGSEONG1 = 2
    JUNGSEONG2 = 3
    JONGSEONG1 = 4
    JONGSEONG2 = 5

class CurrentCharacter:
    def __init__(self):
        self.choseong = None
        self.jungseong = None
        self.jongseong1 = None
        self.jongseong2 = None

    def join(self):
        return '각'

def join_jamos(jamos):
    cur_state = State.START
    result = []

    for jamo in jamos:
        if cur_state == State.START:
            pass
    return '안녕하세요'

#engs looks like : "dkssudgktpdy" -> kors : "ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ"
def change_input_eng_kor(engs):
    kors = ""
    eng_kor = {'q':u'ㅂ','w':u'ㅈ','e':u'ㄷ','r':u'ㄱ','t':u'ㅅ','y':u'ㅛ','u':u'ㅕ',
           'i':u'ㅑ','o':u'ㅐ','p':u'ㅔ','a':u'ㅁ','s':u'ㄴ','d':u'ㅇ','f':u'ㄹ',
           'g':u'ㅎ','h':u'ㅗ','j':u'ㅓ','k':u'ㅏ','l':u'ㅣ','z':u'ㅋ','x':u'ㅌ',
           'c':u'ㅊ','v':u'ㅍ','b':u'ㅠ','n':u'ㅜ','m':u'ㅡ', 'Q':u'ㅃ', 'W':u'ㅉ',
           'E':u'ㄸ', 'R':u'ㄲ', 'T':u'ㅆ', 'O':u'ㅒ', 'P':u'ㅖ'}

    for i in range(len(engs)):
        kors += eng_kor[engs[i]]

    return kors
