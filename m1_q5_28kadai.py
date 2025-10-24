day = ['月', '月', '火', '水', '木', '金', '金']

for d in day:
    # if文で、その要素が2回以上あるときに1つ削除
    if day.count(d) > 1:
        day.remove(d)  # removeで最初に見つかった重複を削除

# insertメソッドで'土'と'日'を追加
day.insert(5, '土')  # 5番目の位置に'土'を追加
day.insert(6, '日')  # 6番目の位置に'日'を追加

print(day)

