def join_jamos(jamos):
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