import random       #导入模块或函数

print("============以下是for循环示例===================")
for i in range(1, 10):
    print(str(i) + " ---> " + str(random.randint(10, 99)))
    print(i)
print("============以下是字符串示例===================")
str0 = "1234567890abcdefghij"
print(len(str0))
print(str0[8])
print(str0[5:])
print(str0[:10])
print(str0[5:10] + "我的世界")
print(str0[6:12], end="")   #默认结束符为“\n”，设置为空就是不换行了
print("我的世界")
print("============以下是列表示例===================")
numbers = [45, 785, 18, 666, "abc", "desk", "hello world", "2000", "3000", "book", ["Tom", "Jerry"], True]
print(len(numbers))
print(numbers[5])
print(numbers[3:])
print(numbers[6])
print(numbers[6][1])
print(numbers[-1])      #下标倒数第一个；-2：倒数第二个
numbers[4] = 888
print(numbers)
numbers[4] = "888"
print(numbers + [104, "minecraft"])
print(random.choice(numbers))       #随机选择列表中的一项
print("============以下是列表的方法示例===================")
numbers2 = numbers[:4]
print(numbers2)
numbers2.sort()
print(numbers2)
numbers2 = numbers[4:10]
print(numbers2)
numbers2.sort()
print(numbers2)
numbers2.pop()
print(numbers2)
numbers2.pop(2)         #最多只能指定一个参数
print(numbers2)
numbers2.insert(2, [4234243, "abcde"])      #只能插入一个值
print(numbers2)
print("============以下是函数的示例===================")
def addWord(str000):
    newString = str000 + " please请！"
    return newString        #用元组可以返回多个值

print(addWord("Seat down"))
print("============以下是字典的示例===================")
score= {"zhangsan": False, 666: "85aaa", "lisi": 92}
print("lisi: " + str(score["lisi"]))
score["lisi"] = 88
print(score)
print("============以下是元组的示例===================")
tuple = 1, 3, 5.0
print(tuple)
print(tuple[2])
aaa, bbb, ccc = tuple     #多重赋值
print(aaa)
print(ccc)
print(bbb)
print("============以下是异常处理的示例===================")
try:
    list000 = [1, 2, 3, 4, 5]
    print(list000[5])
except IndexError:
    print("肯定出错啦！")
print("============以下是面向对象的示例===================")
print(aaa.__class__)
print(ccc.__class__)
print(str0.__class__)
print(numbers.__class__)
print(score.__class__)
print(tuple.__class__)
print("============以下是定义类的示例===================")
import classlib_ywh
c1 = classlib_ywh.class_ywh('英寸', '毫米', 25.4)
print(c1.description())
print('转换10' + c1.units_from)
print('等于：' + str(c1.convert(10)) + c1.units_to)
print("============以下是定义类的继承示例===================")
c2 = classlib_ywh.class_ywh1('摄氏度', '华氏度', 1.8, 32)
print(c2.description())
print('转换37' + c2.units_from)
print('等于：' + str(round(c2.convert(37), 2)) + c2.units_to)
print("============以下是读文件的示例===================")
try:
    with open('word.txt') as f:     #这样写就不要每次写ff.close()了
        words = f.read()       #把文件全部读入内存，如果大文件就不合适了
    print("文件存在。")
except IOError:
    print("文件不存在。")
    exit()
print(words.__class__)
print(words)
print(words.split().__class__)
print(words.split())
print("============以下是文件读行的示例===================")
try:
    f = open('word.txt')
    print("文件存在。")
    line = f.readline()    #每次读取文件的一行，如果大文件就比较合理
    while line != "":
        #print(line, end="")
        print(line)
        if line == "cat\n":
            print("结束。")
            break
        line = f.readline()
    f.close()
except IOError:
    print("文件不存在。")
    exit()
print("============以下是文件写的示例===================")
with open('word3.txt', 'a') as ff:      #这样写就不要每次写ff.close()了
    ff.write('asldj567中国字asjdffl\n')
print("============以下是文件系统操作的示例===================")
import shutil
shutil.copy('word2.txt', 'word22.txt')
shutil.move('word22.txt', 'word222.txt')
import glob
print(glob.glob('*'))
print(glob.glob('*.*'))     #结果不一样
print(glob.glob('*.txt'))
print("============以下是序列化的示例===================")
import pickle
with open('mylist.pickle0', 'wb') as f:
    pickle.dump(numbers, f)
with open('mylist.pickle0', 'rb') as f:
    print(pickle.load(f))
print("========最后是网络编程的示例，这个很重要，单独学===========")
from urllib import request
u = "http://www.yaowenhong.com"
with request.urlopen(u) as f:
    print(f)
    print()
    print(f.read())
    print()
    hhh = f.read().decode('utf-8')      #暂时没成功
    print(hhh)