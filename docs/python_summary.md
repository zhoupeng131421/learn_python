##正则表达式常用语法
- '{}' 定义之前分组个数  
    {3} {3，5} {，3} {3，}
- '|' 匹配多个分组
- '?' 之前分组可有（一次）可无    {0， 1}
- '+' 之前分组至少出现一次        {1， }
- '\*' 之前分组匹配0次或多次      {0， }
- '?' {x, x}? 非贪心匹配，尽可能匹配最短字符串

- \d  0-9数字
- \D  除了0-9数字以外的任意字符
- \w  任意字母数字或下划线（匹配‘单词’字符）
- \W  除了字母数字下划线以外的任意字符
- \s  空格 制表符 换行符 （匹配空白字符）
- \S  除了空格 制表符 换行符以外的任意字符

- '[]'  定义字符分类：[^abc]匹配不在方括号内的任意字符
- '^' '$' 表示匹配必须发生在被查找文本的开始（末尾）
- '.' 通配符，匹配换行之外所有字符
- '.\*' 匹配所有字符（除换行）  
    传入 re.DOTALL 可使'.\*'包换换行符
- re.IGNORECASE re.I  不关心大小写
- sub() 第一个参数替换第二个参数中匹配到的字符
- re.VERBOSE  可以允许正则表达式写成多行，自动忽略空格

<div STYLE="page-break-after: always;"></div>

##OS模块文件常用操作
