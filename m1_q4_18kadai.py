phrase = 'PythonProgramming'
list_p = []
for p in phrase:
    if p not in list_p:
        list_p.append(p)
print(len(phrase) - len(list_p))

for i in list_p: #ループ処理で一文字ずつリストから取る
    print(i,end="") #改行はしたくないのでend=""で改行しないで出力する
print() #改行の出力
