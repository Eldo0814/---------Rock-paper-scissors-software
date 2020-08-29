import random

print('じゃんけんをしよう')
print('1でグー 2でチョキ 3でパーを選択してね')
ai = random.randint(1, 3)
battle = input('最初はグーじゃんけんぽん:')
if int(ai) == 1 and int(battle) == 2:
    print('グーをだしたよ')
    print('私の勝ちだね')
    end = input('エンターを押して終了します')
elif int(ai) == 2 and int(battle) == 1:
    print('チョキをだしたよ')
    print('私の負けだね')
    end = input('エンターを押して終了します')
elif int(ai) == 3 and int(battle) == 1:
    print('パーをだしたよ')
    print('私の勝ちだね')
    end = input('エンターを押して終了します')
elif int(ai) == 1 and int(battle) == 1:
    print('グーをだしたよ')
    print('あいこだね')
    end = input('エンターを押して終了します')
elif int(ai) == 2 and int(battle) == 2:
    print('チョキをだしたよ')
    print('あいこだね')
    end = input('エンターを押して終了します')
elif int(ai) == 3 and int(battle) == 3:
    print('パーをだしたよ')
    print('あいこだね')
    end = input('エンターを押して終了します')
elif int(ai) == 1 and int(battle) == 3:
    print('グーをだしたよ')
    print('私の負けだね')
    end = input('エンターを押して終了します')
elif int(ai) == 2 and int(battle) == 3:
    print('チョキをだしたよ')
    print('私の勝ちだね')
    end = input('エンターを押して終了します')
elif int(ai) == 3 and int(battle) == 2:
    print('パーをだしたよ')
    print('私の負けだね')
    end = input('エンターを押して終了します')
else:
    print('ちゃんと数字を入力してよね！')
    end = input('エンターを押して終了します')