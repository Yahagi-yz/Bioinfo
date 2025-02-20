# 学习目标
1.掌握Python字符串和文件操作核心方法. 
2.实现基础的FASTA文件解析功能. 
3.建立规范的代码编写习惯

## 字符串操作
### 字符串方法
name.title(): 字符串方法，以⾸字⺟⼤写的⽅式显⽰每个单词，如:name="aMe box"，name.title()即为"Ame Box"
name.upper(): 字符串方法，将单词全改成大写，如:name="AbCDEFG",name.upper()输出"ABCDEFG"
name.lower(): 字符串方法,将单词全改成小写，如:name="ABCDEFg",name.lower()输出"abcdfg"
name.rstrip(): 字符串方法,删除字符串右侧所有空白,如:name="Ptyhon ",name.rstrip()输出"Python"
name.lstrip(): 字符串方法,删除字符串左侧所有空白
name.strip(): 字符串方法,删除字符串两侧所有空白
name.removeprefix("前缀"): 字符串方法,去掉指定前缀,如:name="https://www.baidu.com",name.removeprefix("https://"),输出"www.baidu.com".
name.count('G'): 计算字符串中指定字符的个数。

### 高级字符串
import string
string.ascii_letters: 输出大小写字母,52个
string.ascill_lowercase: 小写字母
string.ascill_uppercase: 大写字母
string.digits: 数字0-9，十进制
string.hexdigits: 十六进制0-9A-Fa-f
string.octdigits: 八进制0-7
string.punctuation: 字符".C!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


### f字符串，f-strings
#### 添加变量
f字符串: 在字符串中使用format缩写f加上花括号，能够在字符串中插入变量的值，如:name="Adam",print(f"{name} is a boy")，输出"Adam is a boy"
#### 可以调用对象的方法
#### 可以使用函数
#### 可以在对象的字符串方法中直接使用
#### 可以多行使用
name = (
    f"My {name}."
    f"You {name}."
)
#### 引号需要用\转义
#### 使用{}需要两个{{}}
制表符或换行符: print("\n\tPython")

### 内置函数
map(函数，对象): 对一个可迭代的对象如列表或元组调用函数。
lambda: 快速定义一个函数，而不使用def，通常和map连用如map(lambda x: x * x,number),也可以针对多个对象处理，如map(lambda x,y:x+y,list1,list2)

### 名词解释
方法(method): 是Python对可数据执行的操作,通常加在变量后面,如name.title()。方法通常需要额外的信息来执行，包含在括号里面，这里不需要，所以是空的。
空白符:是指制表符\t和空格\s以及\b
模块
