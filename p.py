ip_address = "192.168.3.1"
ip_spl = ip_address.split('.') # '.'で分割してリストに
bin_exp = '' # 空の文字列
for num in ip_spl:
    bin_exp += bin(int(num))[2:a] + '.' # [2:]で'0b'を取り除き、末尾に'.'を追加
print(bin_exp[:-1])
