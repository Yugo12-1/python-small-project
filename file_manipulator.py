import os
import sys

# 引数のリストを作成
argList = sys.argv

# 引数によってコマンドを呼び出す
def file_manipulator():
    if argList[1] == "reverse": fileReverse(argList)
    elif argList[1] == "copy": fileCopy(argList) 
    elif argList[1] == "duplicate-contents": fileDuplicateContents(argList)
    elif argList[1] == "replace-string": fileReplaceString(argList)
    else: printHowToUse()

def printHowToUse():
    print("Select right arguments\n"
        "##########################################\n"
        "reverse inputpath outputpath\n"
        "copy inputpath outputpath\n"
        "duplicate-contents inputpath n\n"
        "replace-string inputpath needle newstring")

# ファイルの中身を逆にして出力
def fileReverse(argList):
    # 引数の個数が適切かどうか確認
    if len(argList) != 4:
        return printHowToUse()
    
    inputPath = argList[2]
    outputPath = argList[3]

    # inputPathのファイルが存在するかどうかを確認
    if not os.path.isfile(inputPath):
        return print("Input file doesn't exist!")
    
    # inputファイルの中身の各行をリストとして読み込む
    with open(inputPath) as f:
        lineList = f.readlines()
        lineList.reverse()
        # はじめの行の改行コードの追加
        fistLine = lineList[0]
        lineList[0] = fistLine + "\n"

        # 最後の行の改行コードを削除
        lastLine = lineList[-1]
        lineList[-1] = lastLine.replace("\n", "")
        
        reversedContents = "".join(lineList)
    
    # outputfileの作成(新規作成)
    with open(outputPath, "w") as f:
        f.write(reversedContents)

# inputファイルをコピーする
def fileCopy(argList):
    # 引数の個数が適切かどうか確認
    if len(argList) != 4:
        return printHowToUse()
    
    inputPath = argList[2]
    outputPath = argList[3]

    # inputPathのファイルが存在するかどうかを確認
    if not os.path.isfile(inputPath):
        return print("Input file doesn't exist!")
    
    # inputファイルの中身を読み込む
    with open(inputPath) as f:
        contents = f.read()
    
    # outputファイルに書き込む
    with open(outputPath, "w") as f:
        f.write(contents)

# 指定回数の内容を複製する
def fileDuplicateContents(argList):
    # 引数の個数が適切かどうか確認
    if len(argList) != 4:
        return printHowToUse()
    
    inputPath = argList[2]
    n = int(argList[3])

    # inputPathのファイルが存在するかどうかを確認
    if not os.path.isfile(inputPath):
        return print("Input file doesn't exist!")
    
    # inputPathの内容を読み込む
    with open(inputPath) as f:
        contents = f.read()
    
    newContents = ""
    for i in range(n):
        newContents = newContents + contents

    with open(inputPath, "w") as f:
        f.write(newContents)

# 指定した文字列のを置き換える
def fileReplaceString(argList):
    # 引数の個数が適切かどうか確認
    if len(argList) != 5:
        return printHowToUse()
    
    inputPath = argList[2]

    # inputPathのファイルが存在するかどうかを確認
    if not os.path.isfile(inputPath):
        return print("Input file doesn't exist!")
    
    needle = argList[3]
    newString = argList[4]

    # inputファイルの内容を読み込み、置き換える
    with open(inputPath) as f:
        contents = f.read()
    
    newContents = contents.replace(needle, newString)

    with open(inputPath, "w") as f:
        f.write(newContents)

# argList = ["file_manipulator", "reverse", "test.txt", "output.txt"] # debug用
# argList = ["file_manipulator", "copy", "test.txt", "output.txt"] # debug用
# argList = ["file_manipulator","duplicate-contents", "test.txt", "2"] # debug用
# argList = ["file_manipulator","replace-string", "test.txt", "line 2", "Apple"] # debug用

# スクリプトの実行
file_manipulator()