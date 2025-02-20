# 学习目标
1.掌握Python字符串和文件操作核心方法. <br>
2.实现基础的FASTA文件解析功能. <br>
3.建立规范的代码编写习惯<br>

## 字符串操作
### 字符串方法
name.title(): 字符串方法，以⾸字⺟⼤写的⽅式显⽰每个单词，如:name="aMe box"，name.title()即为"Ame Box"<br>
name.upper(): 字符串方法，将单词全改成大写，如:name="AbCDEFG",name.upper()输出"ABCDEFG"<br>
name.lower(): 字符串方法,将单词全改成小写，如:name="ABCDEFg",name.lower()输出"abcdfg"<br>
name.rstrip(): 字符串方法,删除字符串右侧所有空白,如:name="Ptyhon ",name.rstrip()输出"Python"<br>
name.lstrip(): 字符串方法,删除字符串左侧所有空白<br>
name.strip(): 字符串方法,删除字符串两侧所有空白<br>
name.removeprefix("前缀"): 字符串方法,去掉指定前缀,如:name="https://www.baidu.com",name.removeprefix("https://"),输出"www.baidu.com".<br>
name.count('G'): 计算字符串中指定字符的个数。<br>

### 高级字符串
import string<br>
string.ascii_letters: 输出大小写字母,52个<br>
string.ascill_lowercase: 小写字母<br>
string.ascill_uppercase: 大写字母<br>
string.digits: 数字0-9，十进制<br>
string.hexdigits: 十六进制0-9A-Fa-f<br>
string.octdigits: 八进制0-7<br>
string.punctuation: 字符".C!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"<br>


### f字符串，f-strings
#### 添加变量
f字符串: 在字符串中使用format缩写f加上花括号，能够在字符串中插入变量的值，如:name="Adam",print(f"{name} is a boy")，输出"Adam is a boy"<br>
#### 可以调用对象的方法
#### 可以使用函数
#### 可以在对象的字符串方法中直接使用
#### 可以多行使用
name = (<br>
    f"My {name}."<br>
    f"You {name}."<br>
)<br>
#### 引号需要用\转义
#### 使用{}需要两个{{}}
制表符或换行符: print("\n\tPython")<br>

### 内置函数
map(函数，对象): 对一个可迭代的对象如列表或元组调用函数。<br>
lambda: 快速定义一个函数，而不使用def，通常和map连用如map(lambda x: x * x,number),也可以针对多个对象处理，如map(lambda x,y:x+y,list1,list2)<br>

### 名词解释
方法(method): 是Python对可数据执行的操作,通常加在变量后面,如name.title()。方法通常需要额外的信息来执行，包含在括号里面，这里不需要，所以是空的。<br>
空白符:是指制表符\t和空格\s以及\b<br>
模块<br>
