counter=10

def func1():
    print(f"func1内は{counter}です")


def func2():
    global counter
    counter+=10
    print(f"func2内は{counter}です")

func1()
func2()
print(f"関数の外側は{counter}です")

texts ="How are you?"\
        "How old are you?"\
        "What kind do you like?"\
        "Where are you live in?"\
        "Where are you favorite place?"

def get_moji_count(texts):
    return len(texts)

def get_word_count(texts):
    word_count=texts.split(" ")
    return len(word_count)

def get_bunn_count(texts):
    bunn_count=texts.split("?")
    return len(bunn_count)-1

def text_analysis(texts):
    return get_moji_count(texts),get_word_count(texts),get_bunn_count(texts)
moji_count,word_count,bunn_count=text_analysis(texts)
print(f"文字数は{moji_count}、単語数は{word_count}、文章数は{bunn_count}です。")

name=input("あなたの名前を入力してください：")
point=int(input("あなたのテストの点数を入力してください："))
def grade_judge(points):
    if points>=90:
        hanntei="S"
        print("あなたの評価はSです")
        return hanntei
    elif points>=80:
        hanntei="A"
        print("あなたの評価はAです")
        return hanntei
    elif points>=70:
        hanntei="B"
        print("あなたの評価はBです")
        return hanntei
    elif points>=60:
        hanntei="C"
        print("あなたの評価はCです")
        return hanntei
    else:
        hanntei="E"
        print("あなたの評価はEです")
        return hanntei
    
def up_judge(points):
    grade_judge(points)
    print(f"{name}さん")
    hanntei=grade_judge(points)
    if hanntei=="E":
        print("あなたは不合格です")
    else:
        print("あなたは合格です")

up_judge(point)