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
        kor_one = 0
        jongseong_list = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ',
                          'ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ',
                          'ㅎ']
        giyuk_list = ['','ㄱ','ㅅ']
        nieun_list = ['','ㅈ','ㅎ']
        rieul_list = ['','ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']
        bieup_list = ['','ㅅ']
        siot_list = ['','ㅅ']
        if self.jongseong1 == None and self.jongseong2 == None:
            kor_one = 0xAC00 + (ord(self.choseong) - 0x3131) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + 0
        elif (self.jongseong1 != None) and self.jongseong2 == None:
            jong1 = jongseong_list.index(self.jongseong1) + 1
            kor_one = 0xAC00 + (ord(self.choseong) - 0x3131) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + jong1
        elif (self.jongseong1 != None) and (self.jongseong2 != None):
            jong1 = jongseong_list.index(self.jongseong1) + 1
            if self.jongseong1 == 'ㄱ':
                jong2 = giyuk_list.index(self.jongseong2)
            elif self.jongseong1 == 'ㄴ':
                jong2 = nieun_list.index(self.jongseong2)
            elif self.jongseong1 == 'ㄹ':
                jong2 = rieul_list.index(self.jongseong2)
            elif self.jongseong1 == 'ㅂ':
                jong2 = bieup_list.index(self.jongseong2)
            elif self.jongseong1 == 'ㅅ':
                jong2 = siot_list.index(self.jongseong2)
            else:
                print("no such jongseong")
            kor_one = 0xAC00 + (ord(self.choseong) - 0x3131) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + jong1 + jong2
        else:
            print("CurrentCharacter - join function error")
    return kor_one

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