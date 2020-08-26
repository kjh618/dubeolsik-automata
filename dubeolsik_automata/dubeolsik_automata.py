from enum import Enum

KEY_JAEUM = set('ㅂㅃㅈㅉㄷㄸㄱㄲㅅㅆㅁㄴㅇㄹㅎㅋㅌㅊㅍ')
KEY_MOEUM = set('ㅛㅕㅑㅐㅒㅔㅖㅗㅓㅏㅣㅠㅜㅡ')

CHOSEONG_LIST = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
JONGSEONG_LIST = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'

#qwerty looks like : "dkssudgktpdy" -> dubeolsik : "ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ"
def qwerty_to_dubeolsik(qwerty):
    dubeolsik = ""
    qwerty_dubeolsik = {'q':'ㅂ','w':'ㅈ','e':'ㄷ','r':'ㄱ','t':'ㅅ','y':'ㅛ','u':'ㅕ',
           'i':'ㅑ','o':'ㅐ','p':'ㅔ','a':'ㅁ','s':'ㄴ','d':'ㅇ','f':'ㄹ',
           'g':'ㅎ','h':'ㅗ','j':'ㅓ','k':'ㅏ','l':'ㅣ','z':'ㅋ','x':'ㅌ',
           'c':'ㅊ','v':'ㅍ','b':'ㅠ','n':'ㅜ','m':'ㅡ', 'Q':'ㅃ', 'W':'ㅉ',
           'E':'ㄸ', 'R':'ㄲ', 'T':'ㅆ', 'O':'ㅒ', 'P':'ㅖ'}

    for i in range(len(qwerty)):
        dubeolsik += qwerty_dubeolsik[qwerty[i]]

    return dubeolsik

class State(Enum):
    START = 0
    CHOSEONG = 1
    JUNGSEONG1 = 2
    JUNGSEONG2 = 3
    JONGSEONG1 = 4
    JONGSEONG2 = 5

class HangulCharacter:
    COMBINE_JUNGSEONG = {
        'ㅗ': { 'ㅏ': 'ㅘ', 'ㅐ': 'ㅙ', 'ㅣ': 'ㅚ' },
        'ㅜ': { 'ㅓ': 'ㅝ', 'ㅔ': 'ㅞ', 'ㅣ': 'ㅟ' },
        'ㅡ': { 'ㅣ': 'ㅢ' }
    }
    COMBINE_JONGSEONG = {
        'ㄱ': { 'ㅅ': 'ㄳ' },
        'ㄴ': { 'ㅈ': 'ㄵ', 'ㅎ': 'ㄶ' },
        'ㄹ': { 'ㄱ': 'ㄺ', 'ㅁ': 'ㄻ', 'ㅂ': 'ㄼ', 'ㅅ': 'ㄽ', 'ㅌ': 'ㄾ', 'ㅍ': 'ㄿ', 'ㅎ': 'ㅀ' },
        'ㅂ': { 'ㅅ': 'ㅄ' }
    }

    def __init__(self, choseong=None, jungseong=None, jongseong1=None, jongseong2=None):
        self.choseong = choseong
        self.jungseong = jungseong
        self.jongseong1 = jongseong1
        self.jongseong2 = jongseong2

    def add_choseong(self, jaeum):
        assert jaeum in KEY_JAEUM
        assert self.choseong == None
        self.choseong = jaeum
  
    def can_combine_jungseong(self, moeum):
        return self.jungseong in HangulCharacter.COMBINE_JUNGSEONG \
            and moeum in HangulCharacter.COMBINE_JUNGSEONG[self.jungseong]

    def add_jungseong(self, moeum):
        assert moeum in KEY_MOEUM
        if self.jungseong == None:
            self.jungseong = moeum
        elif self.can_combine_jungseong(moeum):
            self.jungseong = HangulCharacter.COMBINE_JUNGSEONG[self.jungseong][moeum]
        else:
            assert False
    
    def can_combine_jongseong(self, jaeum):
        return self.jongseong1 in HangulCharacter.COMBINE_JONGSEONG \
            and jaeum in HangulCharacter.COMBINE_JONGSEONG[self.jongseong1]

    def add_jongseong(self, jaeum):
        assert jaeum in KEY_JAEUM
        if self.jongseong1 == None:
            self.jongseong1 = jaeum
        elif self.can_combine_jongseong(jaeum):
            self.jongseong2 = jaeum
        else:
            assert False

    def join(self):
        kor_one = 0
        giyuk_list = ['','ㄱ','ㅅ']
        nieun_list = ['','ㅈ','ㅎ']
        rieul_list = ['','ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']
        bieup_list = ['','ㅅ']
        siot_list = ['','ㅅ']

        if self.choseong == None and self.jungseong != None and self.jongseong1 == None and self.jongseong2 == None:
            return self.jungseong
        elif self.choseong != None and self. jungseong == None and self.jongseong1 == None and self.jongseong2 == None:
            return self.choseong
        elif self.choseong != None and self. jungseong != None and self.jongseong1 == None and self.jongseong2 == None:
            kor_one = 0xAC00 + CHOSEONG_LIST.index(self.choseong) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + 0
        elif self.choseong != None and self. jungseong != None and self.jongseong1 != None and self.jongseong2 == None:
            jong1 = JONGSEONG_LIST.index(self.jongseong1) + 1
            kor_one = 0xAC00 + CHOSEONG_LIST.index(self.choseong) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + jong1
        elif self.choseong != None and self. jungseong != None and self.jongseong1 != None and self.jongseong2 != None:
            jong1 = JONGSEONG_LIST.index(self.jongseong1) + 1
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
                assert False
            kor_one = 0xAC00 + CHOSEONG_LIST.index(self.choseong) * 588 + \
                      (ord(self.jungseong) - 0x314F) * 28 + jong1 + jong2
        else:
            return ''
        return chr(kor_one)

def join_jamos(keys):
    cur_state = State.START
    cur_char = HangulCharacter()
    result = ''

    for key in keys:
        if key not in KEY_JAEUM | KEY_MOEUM:
            result += cur_char.join()
            cur_char = HangulCharacter()
            result += key
            cur_state = State.START

        if cur_state == State.START:
            if key in KEY_JAEUM:
                cur_char.add_choseong(key)
                cur_state = State.CHOSEONG
            elif key in KEY_MOEUM:
                cur_char.add_jungseong(key)
                cur_state = State.JUNGSEONG1

        elif cur_state == State.CHOSEONG:
            if key in KEY_JAEUM:
                result += cur_char.join()
                cur_char = HangulCharacter(key)
                cur_state = State.CHOSEONG
            elif key in KEY_MOEUM:
                cur_char.add_jungseong(key)
                cur_state = State.JUNGSEONG1

        elif cur_state == State.JUNGSEONG1:
            if key in KEY_JAEUM:
                if cur_char.choseong == None or key not in JONGSEONG_LIST:
                    result += cur_char.join()
                    cur_char = HangulCharacter(key)
                    cur_state = State.CHOSEONG
                else:
                    cur_char.add_jongseong(key)
                    cur_state = State.JONGSEONG1
            elif key in KEY_MOEUM:
                if cur_char.can_combine_jungseong(key):
                    cur_char.add_jungseong(key)
                    cur_state = State.JUNGSEONG2
                else:
                    result += cur_char.join()
                    cur_char = HangulCharacter(None, key)
                    cur_state = State.JUNGSEONG1
        
        elif cur_state == State.JUNGSEONG2:
            if key in KEY_JAEUM:
                if cur_char.choseong == None or key not in JONGSEONG_LIST:
                    result += cur_char.join()
                    cur_char = HangulCharacter(key)
                    cur_state = State.CHOSEONG
                else:
                    cur_char.add_jongseong(key)
                    cur_state = State.JONGSEONG1
            elif key in KEY_MOEUM:
                result += cur_char.join()
                cur_char = HangulCharacter(None, key)
                cur_state = State.JUNGSEONG1
        
        elif cur_state == State.JONGSEONG1:
            if key in KEY_JAEUM:
                if cur_char.can_combine_jongseong(key):
                    cur_char.add_jongseong(key)
                    cur_state = State.JONGSEONG2
                else:
                    result += cur_char.join()
                    cur_char = HangulCharacter(key)
                    cur_state = State.CHOSEONG
            if key in KEY_MOEUM:
                new_choseong = cur_char.jongseong1
                cur_char.jongseong1 = None
                result += cur_char.join()
                cur_char = HangulCharacter(new_choseong, key)
                cur_state = State.JUNGSEONG1
        
        elif cur_state == State.JONGSEONG2:
            if key in KEY_JAEUM:
                result += cur_char.join()
                cur_char = HangulCharacter(key)
                cur_state = State.CHOSEONG
            elif key in KEY_MOEUM:
                new_choseong = cur_char.jongseong2
                cur_char.jongseong2 = None
                result += cur_char.join()
                cur_char = HangulCharacter(new_choseong, key)
                cur_state = State.JUNGSEONG1
        
        else:
            assert False
    
    result += cur_char.join()

    return result
