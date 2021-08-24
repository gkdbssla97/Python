# default_value

def profile(name, age, main_lang) :
    print("이름 : {0}\n나이: {1}\n주 사용 언어: {2}"
    .format(name, age, main_lang))

profile("HA", 20, "python")
profile("QA", 24, "java")

def profile(name, age = 17, main_lang = "pyhon") :
    print("이름 : {0}\n나이: {1}\n주 사용 언어: {2}"
    .format(name, age, main_lang))

profile("LIM")
profile("CHOI", 20)


# 가변인자 (variable factor)
#def profile(name, age, lang1, lang2, lang3) :
#    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end = " ")
#    print(lang1, lang2, lang3)

def profile(name, age, *language) :
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end = " ")
    for lange in language :
        print(lange, end=" ")
    print()

profile("HA", 25, "C", "C#", "Kotlin")
profile("CHOI", "java")