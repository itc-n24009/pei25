num = 3
list_a = []
while num < 5:
    for i in range(num, 10 ,3): #num = 3の場合、3から10まで3つおき、[3,6,9]
        i -= 6 #i-6をiに代入
        list_a.append(i) # list_aにiを追加
    num += 1 # numを1増やす
print(sum(list_a))
