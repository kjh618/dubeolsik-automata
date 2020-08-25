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
