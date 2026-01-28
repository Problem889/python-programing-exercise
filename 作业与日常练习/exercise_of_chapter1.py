#--------------------------------------------------------
#1.怎么计算2的三次方？

a=2
b=a**3
print(b)

#--------------------------------------------------------
#2.怎么找出序列中的最大最小值？

a = [17,9,4,14,10]
print(max(a))
print(min(a))

#--------------------------------------------------------
#3.怎么将字符列表转为字符串

a = {' hello',', i',' am',' xiongheng'}
b = ''.join(a)
print(b)

#--------------------------------------------------------
#4.将字符串 "abcd" 转成大写

print('abcd'.upper())

#--------------------------------------------------------
#5.去掉字符串数组中每个字符串的空格

list_before = ['Go od','D ay','Wha t',' Name']
print(list_before)
list_after = []
for factor in list_before:
    index = ''
    for i in factor:
        if i != '':
            index += i
    list_after.append(index)
print(list_after)


#--------------------------------------------------------
#6.随意输入一个书名，并列出书名的字符长度
book_name = str(input('请输入书名:'))
num = 0
for i in book_name:
    num += 1
print(len(book_name))