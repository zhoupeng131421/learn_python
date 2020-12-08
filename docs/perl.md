# 1 Introduction
### sample program:
```perl
#!/usr/bin/perl
use v5.10;

say "hello world!";
```
unix类系统时，第一行用 _#！_ 开头说明系统中perl安装运行路径，其他系统不需要。  
say 比 print 多一个换行符。


# 2 Scalar Data
Perl 没有具体的数据类型
### Numbers
* int float long 等类型在 Perl 中都是 double_float 类型存储的。  
* 61298040283768 可以写成 61_298_040_283_768（61,298,040,283,768也可以，但不常用），方便人看。  
* 0377 表示八进制数字  
0xff 表示16进制数字  
过长也可使用 `_` 或 `,` 分割，例如： 0x50_65_32_32
* float 类型  
```perl
1.25
111.000
7.28e12   # 7.28 times 10 to the 28th power
-7.19e23
-1.2e-3
-1.2E-3
```
* number operation:  
\+ - * /

### Strings
perl 完全支持 Unicode。如果要使用 Unicode，需要用:
```perl
use utf-8;
```
* Single-Quoted String Literals
```perl
'fred'  # those four characters: f, r, e, and d
'barney'
''
'@#&$*'
'hello
world'  # 两行表示一个字符串，共11个字符
'hello\nworld'  # hellonworld
'hello/\nworld' # 需要转义字符才能换行
```
单引号用于表示，反斜杠用来转义  
* Double-Quoted String Literals
```Perl
"abrney"
"hello world\n"
```
该种类型表示时，不需要转义
* 字符操作
```perl
"hello" . "world"   # same as "helloworld"
"hello" . ' ' . "world" # same as 'hello world'
"fred" x 3 # is "fredfredfred"
"barney" x (2+1) # is "barney" x 5, or "barneybarneybarney"
"5" x 4.8 # is really "5" x 4, which is "5555"
```
* perl 会自动转换数字、字符
```perl
0377 # that's octal for 255 decimal
'0377' # that's 377 decimal
"Z" . 5 * 7 # same as "Z" . 35, or "Z35"
```
