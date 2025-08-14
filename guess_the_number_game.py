import random

def guessNumberGame():
    minNum = int(input("Write min number: "))
    maxNum = int(input("Write max number: "))
    # 数字の大小チェック
    while maxNum < minNum:
        print("Max number must be higher than min number")
        maxNum = int(input("Write max number: "))

    # 最大値と最小値の間のランダム整数の作成
    targetNum = random.randint(minNum, maxNum)

    guessNum = int(input("Guess the number between the min and max number: "))
    # 正解するまでループ処理を行う
    while guessNum != targetNum:
        if guessNum < targetNum:
            print("Target number is higher")
        else:
            print("Target number is lower")
        guessNum = int(input("Guess the number between the min and max number: "))

    print("###############################")
    print("The answer is " + str(targetNum))
    print("Conguraturation!!")

guessNumberGame()