# python
## 语法元素
### 变量类型
- int
- float
- str
- bool
- 复数
### 变量命名
- 硬性规则：
  - 变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
  - 大小写敏感（大写的`a`和小写的`A`是两个不同的变量）。
  - 不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
- PEP 8要求：
  - 用小写字母拼写，多个单词用下划线连接。
  - 受保护的实例属性用单个下划线开头。
  - 私有的实例属性用两个下划线开头。
  ### 运算符
  | 运算符                                                       | 描述                           |
  | ------------------------------------------------------------ | ------------------------------ |
  | `[]` `[:]`                                                   | 下标，切片                     |
  | `**`                                                         | 指数                           |
  | `~` `+` `-`                                                  | 按位取反, 正负号               |
  | `*` `/` `%` `//`                                             | 乘，除，模，整除               |
  | `+` `-`                                                      | 加，减                         |
  | `>>` `<<`                                                    | 右移，左移                     |
  | `&`                                                          | 按位与                         |
  | `^` `|`                                                      | 按位异或，按位或               |
  | `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
  | `==` `!=`                                                    | 等于，不等于                   |
  | `is`  `is not`                                               | 身份运算符                     |
  | `in` `not in`                                                | 成员运算符                     |
  | `not` `or` `and`                                             | 逻辑运算符                     |
  | `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=` | （复合）赋值运算符             |

## 常见函数 用法
### print()
- print('')
- print((%d %x %.1f) % (a, b, c))
### type()
- type(a) 输出a的数据类型
### 分支 `if` `elif` `else`
>Python中没有用花括号来构造代码块而是使用了缩进的方式来设置代码的层次结构，如果`if`条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了，换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
``` python
if x > 0:
  y = 0
elif x >= -1:
  y = 1
else:
  y = 2

if x > 0:
  y = 0
else:
  if x >= -1:
    y = 1
  else:
    y = 2
#第一种优于第二种
```
### range()
- `range(101)`可以产生一个0到100的整数序列。
- `range(1, 100)`可以产生一个1到99的整数序列。
- `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。
### 循环 `for-in` `while`
- for-in
``` python
sum = 0
for x in range(1, 101):
  if x % 2 == 0:
    sum += x
print(sum)
```
- while condition:
> `break`关键字提前终止循环，需要注意的是`break`只能终止它所在的那个循环，这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。除了`break`之外，还有另一个关键字是`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

## function and module
- def xxx :   ... return
> 在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持[函数的重载](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0%E9%87%8D%E8%BD%BD)

- 我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过`import`关键字导入指定的模块就可以区分到底要使用的是哪个模块中的`foo`函数
``` python
from module1 import foo
# 输出hello, world!
foo()
from module2 import foo
# 输出goodbye, world!
foo()

#or:
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()
```
- \__main__
> 如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“\_\_main\_\_”。

``` python
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

- 变量作用域
> Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些隐含标识符`min`、`len`等都属于内置作用域.

函数内部如果要修改全局变量，需要在变量前加`global`声明;同理函数内部的函数如果修改嵌套作用域变量，可以加`nonlocal`声明。实际中尽量减少对全局变量的使用，如果在函数结束仍然想使用局部变量，可以使用[闭包]（跟匿名函数不同概念）。
常规Python格式：
```python
def main():
	# Todo: Add your code here
	pass

if name == '__main__':
	main()
```

## 字符串和常用数据结构
- 字符串
``` python
  str1 = 'abcdefghigklmn'
  print(len(str1))
  print(str1.find('ab'))
  
```
