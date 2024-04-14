# basic

**命名**

- 变量名只能包含字母、数字、下划线。变量名不可以以数字打头。




## 类型提示

我们知道 Python 是一种动态语言，变量以及函数的参数是**不区分类型**。因此我们定义函数只需要这样写就可以了：

```python3
def add(x, y):
    return x + y
```

这样的好处是有极大的灵活性，但坏处就是对于别人代码，无法一眼判断出参数的类型，IDE 也无法给出正确的提示。

于是 Python 3 提供了一个新的特性：**类型提示**

用 `: datatype` 指定函数的参数类型，用 `-> datatype` 指定函数的返回值类型, `|` 表明可返回多种返回值类型

```python
def add(x:int = 5, y:int = 0) -> int | None:
    return x + y
```

- **ATTENTION** : Python 解释器并不会因为这些注解而提供额外的校验，没有任何的类型检查工作。也就是说，这些类型注解加不加，对你的代码来说没有任何影响





## numbers



整数

- `**` 表示乘方运算

- 除法运算符 `/` 执行浮点数除法， `//` 执行整数除法，也就是取商的整数部分



**浮点数**

带小数点的数字。

注意运算结果包含的小数位数可能是不确定的



使用函数 str() 避免类型错误。

![image-20240126183927923](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240126183927923.png)

这是一个类型错误，意味着python无法识别你使用的信息。

python发现你使用了一个值为int的变量，但它不知道该如何解读这个值，python知道这个变量表示的可能是数值23，也可能是字符2和3 。像上面这样在字符串中使用整数时，需要显式地指出你希望python将这个整数用作字符串。

调用函数 str() ，将非字符串值表示为字符串

```python
age = 23
message = "Happy" + str(age) + "Birthday!"

print(message)
```





# Text Sequence Type : str













Textual data in Python is handled with `str` object , or strings. Strings are immutable sequences of Unicode code points. 

- **String literals are written in a variety of ways:**

  - Single quotes: `'allows embedded "double" quotes'`

  - Double quotes: `"allows embedded 'single' quotes"`

  - Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`
    - Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

  - Strings may also be created from other objects using the [`str`](https://docs.python.org/3/library/stdtypes.html#str) constructor.



- Since there is no separate “character” type, indexing a string produces strings of length 1. That is, for a non-empty string *s*, `s[0] == s[0:1]`.



```python
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
```

return a string version of object ,























## Escape sequences

Unless an `'r'` or `'R'` prefix is present, escape sequences in string and bytes literals are interpreted according to rules similar to those used by Standard C. The recognized escape sequences are:

| Escape Sequence | Meaning                          |
| :-------------- | :------------------------------- |
| `\`< newline >  | Backslash and newline ignored    |
| `\\`            | Backslash (`\`)                  |
| `\'`            | Single quote (`'`)               |
| `\"`            | Double quote (`"`)               |
| `\b`            | ASCII Backspace (BS)             |
| `\f`            | ASCII Formfeed (FF)              |
| `\n`            | ASCII Linefeed (LF)              |
| `\r`            | ASCII Carriage Return (CR)       |
| `\t`            | ASCII Horizontal Tab (TAB)       |
| `\v`            | ASCII Vertical Tab (VT)          |
| `\ooo`          | Character with octal value *ooo* |
| `\xhh`          | Character with hex value *hh*    |



Escape sequences only recognized in string literals are:

| Escape Sequence | Meaning                                        |
| :-------------- | :--------------------------------------------- |
| `\N{name}`      | Character named *name* in the Unicode database |
| `\uxxxx`        | Character with 16-bit hex value *xxxx*         |
| `\Uxxxxxxxx`    | Character with 32-bit hex value *xxxxxxxx*     |



**concatenation**

A backslash can be added at the end of a line to ignore the newline:

```python
'This string will not include \
backslashes or newline characters.'
# 'This string will not include backslashes or newline characters.'
```

The same result can be achieved using triple-quoted strings, or parentheses and string literal concatenation



**String literal concatenation**

Multiple adjacent string or bytes literals (delimited by whitespace), possibly using different quoting conventions, are allowed, and their meaning is the same as their concatenation.

Thus, `"hello" 'world'` is equivalent to `"helloworld"`. This feature can be used to reduce the number of backslashes needed, to split long strings conveniently across long lines, or even to add comments to parts of strings, for example:

```python
re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"   # letter, digit or underscore
          )
```





## RegEx 

First import `re` module



### raw

```python
import re

s = 'GeeksforGeeks: A computer science portal for geeks'

match = re.search(r'portal' , s)

print('Start Index:' , match.start())
print('End Index: ', match.end())
```

-  Here `r` character stands for raw, not regex .The raw string is slightly different from a regular string : It won't interpret the `\` character as an escape character. 

  This is bacause the regular expression engine uses `\` character for its own escaping purpose .



### Metacharacters

| MetaCharacters |                         Description                          |
| :------------: | :----------------------------------------------------------: |
|       \        |      drop the special meaning of character following it      |
|       []       |                      a character class                       |
|       ^        |   Matches the beginning(When not inside a character class)   |
|       $        |                       Matches the end                        |
|       .        |             Matches any character except newline             |
|       \|       | Means OR (Matches with any of the characters separated by it. |
|       ?        |                Matches zero or one occurrence                |
|       *        |     Any number of occurrences (including 0 occurrences)      |
|       +        |                   One or more occurrences                    |
|       {}       | Indicate the number of occurrences of a preceding regex to match. |
|       ()       |                   Enclose a group of Regex                   |





### details



#### `\` 

The blackslash makes sure that the characteris not treated in a special way . This can be considered a way of escaping metacharacters.

- For example : If you want to search for the `.` in the string then you will find that dot will be treated as a special character as is one of the metacharacters.

  So for this case, we will use the blackslash just before the dot so that it will lose its specialty.

  ```python
  s = 'greeks.forgeeks'
  
  match = re.search(r'.', s)	# Outupt :<re.Match object; span=(0, 1), match='g'>
  
  match = re.search(r'\.', s)	  # output: <re.Match object; span=(5, 6), match='.'>
  ```

  

#### []

The Square Brackets represent a character class consisting of a set of characters that we wish to match.

- example : the character class [abc] will match any single a, b, or c.

- **specify a range of characters using `-`**

  [a-c] is same as [abc]

- **invert the character class**

  using `^` inside the character class

  [^0-3] means any number except 0,1,2,3

  [^a-c] means any character except a, b, c

```python
string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string) 
```



#### `^`  `$`

`^`match the begging of the string

- example :

  `^eg` will check if the string starts with `eg` such as egg



```python
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']

for string in strings :
    if re.match(regex, string):
        print(f'Matched: {string}')
    else :
        print(f'Not matched: {string}')
        
        
"""
Matched: The quick brown fox
Matched: The lazy dog
Not matched: A quick brown fox
"""
```

same for `$`



#### `.`

Dot matches only a single character except for the newline character( `\n` ) 

- example :

  `a.b` will check for the string that contains any characer at the place of the dot ( such as abb, acb , adbb )

  `..` will check if the string contains at least 2 characters

  

```python
string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(patter, string)
if match:
    print("Match found!")
```





#### `|`

Or symbol works as the operator meaning it checks whether the pattern before or after the or symbol is present in the string or not .

- example : `a|b` will match any string that contains a or b 



#### `?`

a quantifier in re that indicates that the preceding element should be matched zero or one time .

It allows you to specify that the element is optional  .

- `ab?c` will be matched for the string ac, acb, abcc ...



#### `*` vs `+`

`*`  **match zero or more occurrences of the regex preceding the** `*` 

`+`  matchh one or more occurences of the regex preceding the `+`



####  {m, n} 

Braces match any repetitions preceding regex from m to n both inclusive.

- a{2, 4} will be matched for the string aaab, baaaac, gaad



#### (regex) 

Group symbol is used to group sub-patterns

- (a|b)cd will match for strings like acd, abcd, gacd, etc.





### Special Sequences

Special sequences do not match for the actual character in the string instead it tells the specific location in the search string where the match must occur

| Special Sequence |                         Description                          | Examples |                 |
| :--------------: | :----------------------------------------------------------: | :------: | --------------- |
|        \A        |    Matches if the string begins with the given character     |  \Afor   | for me          |
|        \b        | Matches if the word begins or ends with the given character. `\b(string)` will check for the beginning of the word and `(string)\b` will check for the ending of the word. |   \bge   | geeks, get      |
|        \B        | the opposite of the \b i.e. the string should not start or end with the given regex. |   \Bge   | together, forge |
|        \d        |    Matches any decimal digit, equivalent to  class [0-9]     |    \d    | 123, gee1       |
|        \D        |   Matches any non-digit character, equivalent to `[^0-9]`    |    \D    | geeks           |
|        \s        |              Matches any whitespace character.               |    \s    | gee ks          |
|        \S        |             Matches any non-whitespace character             |    \S    | a bd            |
|        \w        | Matches any alphanumeric character, equivalent to the class [a-zA-Z0-9_]. |    \w    | 123             |
|        \W        |           Matches any non-alphanumeric character.            |    \W    | >$              |
|        \Z        |       Matches if the string ends with the given regex        |   ab\Z   | abcdab          |



### SETS

|     Set      |                         Description                          |
| :----------: | :----------------------------------------------------------: |
|    \{n,\}    | Quantifies the preceding character or group and matches at least n occurrences. |
|      *       | Quantifies the preceding character or group and matches zero or more occurrences. |
|    [0123]    |         Matches the specified digits (0, 1, 2, or 3)         |
|    [^arn]    |         matches for any character EXCEPT a, r, and n         |
|      \d      |                   Matches any digit (0-9).                   |
| `[0-5][0-9]` |       matches for any two-digit numbers from 00 and 59       |
|      \w      |  Matches any alphanumeric character (a-z, A-Z, 0-9, or _).   |
|    [a-n]     |       Matches any lower case alphabet between a and n.       |
|      \D      |               Matches any non-digit character.               |
|    [arn]     | matches where one of the specified characters (a, r, or n) are present |
|   [a-zA-Z]   | matches any character between a and z, lower case OR upper case |
|    [0-9]     |              matches any digit between 0 and 9               |





### Match Object

A Match object contains all the information about the search and the result and if there is no match found then None will be returned.



#### Getting the string and  regex

***match.re*** 	attribute returns the regular expression passed 

 ***match.string***	attribute returns the string passed.

 ```python
 s = "Welcome to GeeksForGeeks"
 res = re.search(r"\bG", s) 
   
 print(res.re) # re.compile('\\bG')
 print(res.string) # Welcome to GeeksForGeeks
 ```



#### Getting index of matched object

- `start()  `returns the starting index of the matched substring
- `end()` returns the ending index of the matched substring
- `span() `returns a tuple containing the starting and the ending index of the matched substring

```python
  
s = "Welcome to GeeksForGeeks"
  
res = re.search(r"\bGee", s) 
  
print(res.start())  # 11
print(res.end())  # 14 
print(res.span()) # (11, 14)
```





#### Getting matched substring

group() method returns the part of the string for which the patterns match. 



```python
s = "Welcome to GeeksForGeeks"
res = re.search(r"\D{2} t", s) 
print(res.group()) # me t
# The code searches for a sequence of two non-digit characters followed by a space and the letter ‘t’
```









### RegEx Functions

|   Function   |                         Description                          |
| :----------: | :----------------------------------------------------------: |
| re.findall() |     finds and returns all matching occurrences in a list     |
| re.compile() |    Regular expressions are compiled into pattern objects     |
|  re.split()  | Split string by the occurrences of a character or a pattern. |
|   re.sub()   | Replaces all occurrences of a character or patter with a replacement string. |
| re.escape()  |                  Escapes special character                   |
| re.search()  |    Searches for first occurrence of character or pattern     |

example :

- set class `[\s,.]` will match any whitespace character `,` or `.`



#### re.findall()

Return all non-overlapping matches of pattern in string, **as a list of strings**. 

The string is scanned left-to-right, and matches are returned in the order found.

**example :**

```python
string = """Hello my Number is 123456789 and 
            my friend's number is 987654321"""
regex  = '\d+'

match = re.findall(regex, string)
print(match)

# output : ['123456789', '987654321']
```



#### re.compile()

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions .



**demo 1**

```python
p = re.compile('[a-e]')

print(p.findall("Aye, said Mr. Gibenson Stark"))

# use a regular expression pattern [a-e] to find and list all lowercase letters from 'a' to 'e' in the input string .

# output: ['e', 'a', 'd', 'b', 'e', 'a']
```



 **demo 2** 

```python
p = re.complie('\d')
print(p.findall(""I went to him at 11 A.M. on 4th July 1886""))
# output : ['1', '1', '4', '1', '8', '8', '6']



p = re.complie('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
# output : ['11', '4', '1886']
```



**demo3**

```python
p = re.compile('\w')
print(p.findall("He said * in some_lang."))
#  ['H', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']

p = re.compile('\w+')
print(p.findall("He said * in some_lang."))
# ['H', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']

p = re.compile('\W')
print(p.findall("he said *** in some_language."))
# [' ', ' ', '*', '*', '*', ' ...
```





**demo 4**

```python
p = re.compile('ab*')
print(p.findall("ababbaabbb"))

# * match zero or more character preceding the * character .
# ['ab', 'abb', 'a', 'abbb']
```

explanation :

`ab*` : a accompanied by any number of b.





#### re.split()

Split string by the occurrences of a character or a pattern. 

`re.split(pattern, string, maxsplit=0, flags=0)`

maxsplit if not provied is considered to be 0, and if any nonzero value is provided, then at most that many splits occur. If maxsplit = 1, then the string will split once only, resulting in a list of length 2 .

The flags are very useful and can help to shorten code, they are not necessary parameters, eg: flags = re.IGNORECASE, in this split, the case, i.e. the lowercase or the uppercase will be ignored.



**demo 1**

```python
from re import split

# Splits a string using non-word characters and spaces as delimiters

print(split('\W+', 'Words, words , Words'))
# returning ['Words', 'words', 'Words']

print(split('\W+', "Word's words Words")) 
# returning ['Words', 'words', 'Words']

print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
# ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']

```





#### re.sub()

`re.sub(pattern, replace_statement, string, count=0, flags=0)`

```python
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',  
             flags=re.IGNORECASE))
# Baked Beans & Spam

print(re.sub('ub', '~*', 'Subject has Uber booked already',  
             flags=re.IGNORECASE)) 
# S~*ject has ~*er booked already
```





- #### **re.subn()**

  **`re.subn()`** replaces all occurrences of a pattern in a string and returns a tuple with the modified string and the count of substitutions made. It’s useful for both case-sensitive and case-insensitive substitutions.

```python
t = re.subn('ub', '~*', 'Subject has Uber booked already', 
            flags=re.IGNORECASE) 
print(t) 
print(len(t)) 
print(t[0]) 

"""
('S~*ject has ~*er booked already', 2)
2
S~*ject has ~*er booked already
"""

```



#### re.escape()

Returns string with all non-alphanumerics backslashed, this is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it.

`re.escape(string)`

```python
print(re.escape("I Asked what is this [a-9], he said \t ^WoW")) 

# I\ Asked\ what\ is\ this\ \[a\-9\]\,\ he\ said\ \    \ \^WoW
```



#### re.search()

return either None( if the pattern doesn't match) or a `re.MatchObject` contains infromation about the matching part of the string .

- **This method stops after the first match, so this is best suited for testing a regular expresson more than extracting data .**



```python
regex = r"([a-zA-Z]) (\d+)"

match = re.search(regex, "I was born on June 24")
if match != None :
    print ("Match at index %s, %s" % (match.start(), match.end())) 
    print ("Full match: %s" % (match.group(0))) 
    print ("Month: %s" % (match.group(1))) 
    print ("Day: %s" % (match.group(2))) 
  
else: 
    print ("The regex pattern does not match.") 
 
"""
Match at index 14, 21
Full match: June 24
Month: June
Day: 24
"""

```







# Sequence Types

There ar three basic sequence types : lists, tuples, and range objects.



## Common Sequence Operations

 *s* and *t* are sequences of the same type, *n*, *i*, *j* and *k* are integers and *x* is an arbitrary object that meets any type and value restrictions imposed by *s*.

| Operations           | Result                                                       |
| -------------------- | ------------------------------------------------------------ |
| `x in s`             | True if an item of s is equal to x, else False , also can be used as `x not in s` |
| `s + t`              | the concatenation of  s and t                                |
| `s * n` or `n * s`   | equivalent to adding s to itself n times                     |
| `s[i]`               | i th item of s, origin 0                                     |
| `s[i:j]`             | slice of s from i to j                                       |
| `len(s)`             | length of s                                                  |
| `min(s)` or `max(s)` | the smallest or largest item of s                            |
| s.count(x)           | total number of occurrences of x in s                        |

- Forward and reversed iterators over mutable sequences access values using an index. That index will continue to forward or backward even if the underlying sequence is mutated.

  The iterator terminates only when an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError) or a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) is encountered (or when the index drops below zero).



`in`

While the `in` and `not in` are used only for simple containment testing in the general case, **some specialised   sequences( such as str ) also use them for subsequence testing:**

```python
>>> "gg" in "eggs"
```





### Immutable Sequence Types





### Mutable Sequence Types





























## Ranges

**The range type represents an immuable sequence of numbers and is commonly used for looping a specific number of times in for loops .**



```python
class range(stop)
class range(start, stop[, step])
```

- Default value of `start` is 0
- Default value of `step` is 1 

For a positive *step*, the contents of a range `r` are determined by the formula `r[i] = start + step*i` where `i >= 0` and `r[i] < stop`.

For a negative *step*, the contents of the range are still determined by the formula `r[i] = start + step*i`, but the constraints are `i >= 0` and `r[i] > stop`.



The advantage of the range type over a regular list or tuple is that a range object will always take the same( small ) amount of memory, no matter the size of the range it represents( as it only stores the start, stop, and step values, caluculating individual items and subranges as needed)





## 列表

`class list([iterable])`

Lists may be constructed in several ways:

- Using a pair of square brackets to denote the empty list: `[]`
- Using square brackets, separating items with commas: `[a, b, c]`
- Using a list comprehension: `[x for x in iterable]`
- Using the type constructor: `list()` or `list(iterable)`

The constructor builds a list whose items are the same and in the same order as *iterable*’s items. *iterable* may be either a sequence, a container that supports iteration, or an iterator object. If *iterable* is already a list, a copy is made and returned, similar to `iterable[:]`. For example, `list('abc')` returns `['a', 'b', 'c']` and `list( (1, 2, 3) )` returns `[1, 2, 3]`. If no argument is given, the constructor creates a new empty list, `[]`.







### 列表基本操作



#### 访问列表元素

```python
print(bicycles[0])
```

- 第一个列表元素的索引为0
- 将索引指定为 -1 ，返回最后一个列表元素。
  - 这种约定也使用于其它附属索引，例如 索引  - 2 返回倒数第二个列表元素 索引 -3 返回倒数第三个列表元素。 



#### 修改、添加、删除元素

你创建的大多数列表都将是动态的 。例如你创建一个游戏，要求玩家射杀从天而降的外星人 ；为此，可在开始时将一些外星人存储在列表中，然后每当有外星人被射杀时，都将其从列表中删除，而每次有新的外星人出现在屏幕上时，都将其添加到列表中。整个游戏运行期间，外星人列表的长度将不断变化。



**修改元素值**

```python
motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
```



**添加元素**

- **在列表末尾添加元素 ：  append( value )** 

```python
motorcycles.append('ducati')
```

方法 append() 可动态地创建列表 。例如你可以先创建一个空列表，再使用一系列的 append() 语句添加元素 。

```python
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
```

这种创建列表的方式极其常见，因为经常要等程序运行后，才知道用户要在程序中存储哪些数据。为控制用户， 可首先创建一个空列表，然后将用户提供的每个新值添加到列表中 。



- **在列表任意位置插入元素 ： insert( index ，value )**

​	将列表中既有的每个元素都右移一个位置 。

```python
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')

# motorcycles = ['ducati' , 'honda' , 'yamaha' , 'suzuki' ]
```





 **删除**

*根据位置或值来删除列表中的元素*



- ***del 语句 : del list_name[index]***

```python
del motorcycles[0]
# 该索引右侧元素左移一个单位 

```



- ***pop()***

有时候要将元素从列表中删除，并接着使用它的值。例如，你可能需要获取刚被射杀的外星人的x和y坐标，以便在响应的位置显示爆炸效果； 在web应用程序中，你可能要将用户从活跃成员列表中删除，并将其加入到非活跃成员列表中。

*方法 pop() 删除列表末尾的元素，并允许你继续使用它*

pop就源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。

```python
popped_motorcycle = motorcycles.pop() 
print(poped_motorcycles)

#suzuki
```

​       

- ***pop( index )***

  弹出列表中任何位置处的元素

```python
# 假设列表中的摩托车是按照购买时间存储的
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned is a " + first_owned.title() + "." )
```



- ***remove(value)***

根据值删除元素  

方法remove() 只删除列表中找到的第一个匹配元素，**如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。**

```python
motorcycles = ['honda','yamaha','suzuki','ducati','yemaha']
for i in range(len(motorcycles)):
    

```



**ATTENTION** ：

Do not loop over the same list and modify it while iterating!

Removing an item will shift all following items one place to the left, thus in the next iteration one item will be skipped. This can lead to incorrect results.

 iterate over a copy of the list (A copy is simply created by using `a[:]`) and  remove items from the original list if the condition is true.

```python
# wrong version
for item in a:
    if even(item):
        a.remove(item)
        
# right version
for item in a[:]:
    if even(item):
        a.remove(item)
```





#### sort()



1. **使用方法 sort() 对列表进行永久性排序**

```python
cars = ['bmw','audi','toyota','subaru']
cars.sort()
# ['audi', 'bmw', 'subaru', 'toyota']

# 逆序
cars.sort(reverse = True)
```



2. **使用方法 sorted(list) 对列表进行临时排序**

函数 sorted()  : 按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序



3. **反转列表元素顺序**

```python
car.reverse()
```

reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序



4. **确定列表的长度**

```python
>>> len(cars) 
```



#### for 遍历列表

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

python 首先获取列表 magicians 中的第一个值 'alice' , 并将其存储到变量 magician 中, 然后执行print 

由于该列表中还包含其他值，python返回到循环的第一行，python获取列表中的下一个名字，'david' ,并将其存储到变量 magician 中



#### List Comprehensions

List Comprehensions provide a concise way to create lists. 

A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. 

Note how the order of the `for`and `if` statements is the same in both these snippets.

If the expression is a tuple (e.g. the `(x, y)` in the previous example), it must be parenthesized.



- example 1

```
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Note that this creates (or overwrites ) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:

`squares = list(map(lambda x: x**2, range(10)))`

or , equivalently :

`squares = [x**2 for x in range(10)]`



- another example

  ```python
  >>> [(x,y) fpr x in [1,2,3] for y in [3,1,4] if x != y]
  [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
  ```

  equivalent to :

  ```
  >>> combs = []
  >>> for x in [1,2,3]:
  ...     for y in [3,1,4]:
  ...         if x != y:
  ...             combs.append((x, y))
  ...
  >>> combs
  [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
  ```



List comprehensions can contain complex expressions and nested functions:

```
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```





**Nested List Comprehensions**

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```



The following list comprehension will transpose rows and columns:

```
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

 equivalent to:

```
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

which, in turn, is the same as:

```
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```



In the real world, you should prefer built-in functions to complex flow statements. The [`zip()`](https://docs.python.org/3.12/library/functions.html#zip) function would do a great job for this use case:

```
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```





### 切片

**处理列表的所有元素 -- 切片**



#### 创建切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与 range() 函数一样，python在**到达你指定的第二个索引前面的元素后停止**。

```python
players = ['charles', 'martina', 'michael', 'fkirebce', 'eli']
print(players[0:3])

#  ['charles', 'martina', 'michael']
```

你可以生成列表的任何子集，例如如果你要提取列表的第 2-4 个元素，可将起始索引指定为1 ，并将终止索引指定为4 。



```python
print(players[:4]) # 不指定起始索引 python会从列表开头开始提取
print(players[2:]) # 提取从第三个元素到列表末尾的所有元素

print(players[-3:]) #打印列表最后三名成员的名字
```



#### 遍历切片

```python
players = ['charles', 'martina', 'michael', 'fkirebce', 'eli']

for player in players[:3]:
    print(player.title())
```



在很多情况下切片都很有用。

例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入到一个列表中，然后为获取该玩家的三个最高得分，你可以将该列表降序排列 ，再创建一个只包含前三个得分的切片 。

处理数据时可以利用切片来批量处理 ；

编写web应用程序时 ，可使用切片来分页显示信息，并在每页显示数量合适的信息 。



#### 复制列表

要复制列表，可**创建一个包含整个列表的切片** ，方法是**同时省略起始索引和终止索引  [ : ] **

```python
my_foods = ['pizza', 'falafel', 'carrit cake']
friend_foods = my_foods[ : ]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
print(my_foods)

print("My friend's favourite foods ard: ")
print(friend_foods)

""" 
My favorite foods are:
 ['pizza', 'falafel', 'carrot cake', 'cannoli']
My friend's favorite foods are:
 ['pizza', 'falafel', 'carrot cake', 'ice cream']
 
 表明此时存在两个表 。
 倘若我们只是简单地将 my_foods 赋给 friend_foods ,就不能得到两个列表
"""

```



易犯的错误 ：

```python
friend_foods = my_foods
```

这里将 my_foods 赋给 friend_foods , 而不是将 **my_foods 的副本存储到 friend_foods** ，这种语法实际上是让python将新变量 friend_foods 关联到包含在 my_foods 中的列表，因此**这两个变量都指向同一个列表** 。



### 元组

**不可变的列表称为元组**



元组使用圆括号而不是方括号来表示 。

定义元组后 ，就可以使用索引来访问其元素 ，就像访问列表元素一样。

例如，如果有一个大小不应改变的矩形 ，可将其长度和宽度存储在一个元组中 ，从而确保它们是不能修改的 。

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```



如果 修改tuple ：

![image-20240203113234940](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240203113234940.png)



#### **遍历元组**

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```



#### **修改元组变量**

**虽然不能修改元组的元素 ，但可以给存储元组的变量赋值。**

因此，如果要修改前述矩形的尺寸，可重新定义整个元组。

```python
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
    
# 将一个新元组存储到变量 dimensions中 ，这次python不会报告任何错误，因为给元组变量赋值是合法的
```





# Binary Sequence Types





## charset

![image-20240407130342973](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240407130342973.png)





### Unicode

**Universal Coded Character Set**





Unicode uses two encoding forms: 8-bit and 16-bit, based on the data type of the data being encoded. 

The default encoding form is 16-bit, that is, each character is 16 bits  wide, and is usually shown as U+hhhh, where hhhh is the hexadecimal code point of the character. 



### UTF-8

- UTF-8 序列的第一个字节被称为 "leader byte" , leader byte 提供了关于序列中有多少个字节的信息，以及字符的码位值是什么

  单字节序列的 leader byte 总是在（0-127）范围内。两字节序列的 leader byte 在（194-223）范围内。三字节序列的 leader byte 在（224-239）范围内。四字节序列的 leader byte 在（240-247）范围内。



- 序列中剩余的字节被称为 “**trailing bytes**”





### ASCII

可显示字符编号范围是32-126（0x20-0x7E），共95个字符。

32～126(共95个)是字符(32是空格)，其中48～57为0到9十个阿拉伯数字。

65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等。

![image-20240407130000559](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240407130000559.png)



![image-20240407130038339](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240407130038339.png)





### EASCII

**Extended ASCII**，延伸美国标准信息交换码）是将[ASCII](https://zh.wikipedia.org/wiki/ASCII)码由7位扩充为8位而成。EASCII的内码是由0到255共有256个字符组成。EASCII码比ASCII码扩充出来的符号包括表格符号、计算符号、希腊字母和特殊的拉丁符号。





## chr() and ord()

**chr**(*i*)

Return the string representing a character whose Unicode code point is the integer *i*. For example, `chr(97)` returns the string `'a'`, while `chr(8364)` returns the string `'€'`. This is the inverse of [`ord()`](https://docs.python.org/3/library/functions.html#ord).

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) will be raised if *i* is outside that range.



**ord**(*c*)

Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, `ord('a')` returns the integer `97` and `ord('€')` (Euro sign) returns `8364`. 





## Bytes Objects



```python
class bytes(source=b'')
class bytes(source, encoding)
class bytes(source, encoding, errors)
```

- Return a new “bytes” object which is an immutable sequence of integers in the range `0 <= x < 256`. 

- The syntax for bytes literals is largely the same as  string literals, except that a `b` prefix is added :

  ```python
  Single quotes: b'still allows embedded "double" quotes'
  
  Double quotes: b"still allows embedded 'single' quotes"
  
  Triple quoted: b'''3 single quotes''', b"""3 double quotes"""
  ```

  Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding). Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.
  
- In addition to the literal forms, bytes objects can be created in a number of other ways:

  - A zero-filled bytes object of a specified length: `bytes(10)`
  - From an iterable of integers: `bytes(range(20))`
  - Copying existing binary data via the buffer protocol: `bytes(obj)`

- As with string literals, bytes literals may also use a `r` prefix to disable processing of escape sequences




### classmethod `fromhex(string)`

This bytes class method returns a bytes object , decoding the given string object. The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored .

```python
>>> bytes.fromhex('2EF0 F1F2')
b'.\xf0\xf1\xf2'
```



- A reverse conversion function to transform a bytes object into its hexadecimal representation : `hex([sep[, bytes_per_sep]])`

  ```python
  >>> b'\xf0\xf1\xf2'.hex()
  'f0f1f2'
  ```

  If you want to make the hex string easier to read, you can specify a single character separator *`sep`* parameter

  By default, this separator will be included between each byte. A second optional *`bytes_per_sep`* parameter controls the spacing. Positive values calculate the separator position from the right, negative values from the left.

  ```python
  >>> value = b'\xf0\xf1\xf2'
  >>> value.hex('-')
  'f0-f1-f2'
  
  >>> value.hex('_', 2)
  'f0_f1f2'
  >>>b'UUDDLRLRAB'.hex(' ', -4)
  '55554444 4c524c52 4142'



- Since bytes objects are sequences of integers (akin to a tuple), for a bytes object *b*, `b[0]` will be an integer, while `b[0:1]` will be a bytes object of length 1. (This contrasts with text strings, where both indexing and slicing will produce a string of length 1)
- The representation of bytes objects uses the literal format (`b'...'`) since it is often more useful than e.g. `bytes([46, 46, 46])`. You can always convert a bytes object into a list of integers using `list(b)`.



## `bytearray` Objects

`bytearray `objects are a mutable counterpart to `bytes` objects

```python
class bytearray([source[, encoding[, errors]]])
```

There is no dedicated literal syntax for bytearray objects, instead they are always created by calling the constructor:

- Creating an empty instance: `bytearray()`
- Creating a zero-filled instance with a given length: `bytearray(10)`
- From an iterable of integers: `bytearray(range(20))`
- Copying existing binary data via the buffer protocol: `bytearray(b'Hi!')`



### `classmethod fromhex(strin)`

This [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray) class method returns bytearray object, decoding the given string object. The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.



A reverse conversion function exists to transform a bytearray object into its hexadecimal representation.

- **hex**([*sep*[, *bytes_per_sep*]])

  Return a string object containing two hexadecimal digits for each byte in the instance.

  `bytearray(b'\xf0\xf1\xf2').hex() 'f0f1f2'`



## Bytes and Bytearray Operations



### decode

```python
bytes.decode(encoding='utf-8', errors='strict')
bytearray.decode(encoding='utf-8', errors='strict')
```

- Return the bytes decoded to a str

- *encoding* defaults to `'utf-8'`; 

  [Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings) for possible values.

- *errors* controls how decoding errors are handled. If `'strict'` (the default), a [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError) exception is raised. 









# 字典

字典是一系列键值对 ，每个键都与一个值相关联 ，你可以使用键来访问与之关联的值 。

与键相关联的值可以是数字、字符串、列表乃至字典 。事实上，可将任何python对象用作字典中的值 。



字典用放在 {} 中的一系列键值对表示 。键和值之间用冒号分隔 ，而键值对之间用逗号分隔 。

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```



## 基本操作



### 添加键值对

依次指定字典名、**键名 和相关联的值** 。

```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```



### 修改字典中的值

```python
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'
```



```python
alien_0 = {'x_position': 0, 'y_posiiton': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
```



### 删除键值对

对于字典中不再需要的信息，可使用 del语句将相应的键值对彻底删除 。

使用del语句时，需要指定字典名和要删除的键

```python
alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
```





## 遍历字典



### 遍历键值对

**方法 items()** 返回一个键值对列表

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi', 
}

for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value + "\n")
```

- 声明两个变量， 用于存储键值对中的键和值 。(这两个变量可使用任何名称)`for k,v in user_0.items()`


- for 语句的第二部分包含字典名和方法 items() , 它返回一个键值对列表。


即便遍历字典时 ，键值对的返回顺序也与存储顺序不同。 python不关心键值对的存储顺序，而只跟踪键和值之间的关联关系



字典存储不同人的同一种信息

```python
favourite_languages = {
    'jen': 'python',
    'sarah': 'c'
    'edward': 'ruby'
    'phil': 'python',   
}
for name, language in favourite_language.items():
    print(name.title() + "'s favourite language is "+ language.title() + ".")
```





### 遍历键

在不需要使用字典中的值时，keys() 返回一个列表 ,包含字典中所有的键.

```python
friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favourite language is " +
             favourite_languages[name].title() + "!")
```

- 遍历字典时，默认遍历所有的键，因此如果将上述代码中的 `for name in favourite_languages。keys(): ` 替换为 `for name in favourite_languages: ` 输出不变

  

字典获取顺序不可预测。要以特定的顺序返回元素，可在for循环中对返回的键进行排序。

为此，可使用函数 sorted()来获得按特定顺序排列的键列表的副本。

```python
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")
```





### 遍历值

方法 values() 返回一个值列表，而不包含任何键 。

````python
for language in favourite_languages.values():
    print(language.title())
````



为剔除重复项，可使用集合set ，集合类似于列表，但每个元素都必须唯一

```python
for language in set(favourite_languages.values())

# 通过对包含重复元素的列表调用set(), 可让python找出列表中独一无二的元素，并使用这些元素来创建一个集合。
```



## 嵌套

**有时候需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。**



### 字典列表

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```



用代码自动生成外星人

```python
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
   
print("Total number of aliens: " + str(len(aliens)))

"""
这些外星人具有相同的特征，但在python看来，每个外星人都是独立的 ，这让我们能够独立地修改每个外星人。
在什么情况下需要处理成群结队的外星人呢？ 想象一下，可能随着游戏的进行，有些外星人会变色且移动速度会加快 。必要时，我们可以使用 for循环和 if语句来修改某些外星人的颜色 。
"""

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
```





### 在字典中存储列表

```python
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese'], 
}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
     "with the following toppings: ")

for topping in pizza['toppings'] :
    print("\t" + topping)
```





```python
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are :")
    for language in languages:
        print("\t" + language.title())
```



### 在字典中存储字典



如果有多个网站用户 ，每个都有独特的用户名，可在字典中将用户名作为键 ，然后将每位用户的信息存储在一个字典中 ，并将该字典作为与用户相关联的值 。

```python
users = {
    'asinstein': {
        'fisrt': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    }
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie', 
        'location': 'paris',
    }
    
}

for username, user_info in users.items() :
    print("\nusername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
```



## functions









## Dictionary view objects

The objects returned by [`dict.keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys), [`dict.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values) and [`dict.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items) are *view objects*. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.



### **len(dictview)**

Return the number of entries in the dictionary.



### **iter(dictview)**

Return an iterator over the keys, values or items (represented as tuples of `(key, value)`) in the dictionary.

- Keys and values are iterated over in insertion order.
  -  This allows the creation of `(value, key)` pairs using [`zip()`](https://docs.python.org/3/library/functions.html#zip): `pairs = zip(d.values(), d.keys())`. 
  - Another way to create the same list   `pairs = [(v, k) for (k, v) in d.items()]`.





### `zip(*iterables, strict=False)`

Iterate over several iterables in parallel, producing tuples with an item from each one.

```python
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
```

returns an iterator of tuples, where the *i*-th tuple contains the *i*-th element from each of the argument iterables.





# if 语句

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```





## 条件测试

**python 中检查是否相等时区分大小写**

```python
car = 'Audi'
if car.lower == 'audi':
    print("Yes")
```



### 检查多个条件

**关键字 and 和 or** 

```python
age_0 = 22
age_2 = 18
if age_0>=21 and age_1 >=21 :
    print("Yes")
```



### 检查特定值是否包含在列表中

要判断特定的值是否已经包含在列表中，可使用**关键字 in** 

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("True")
```



**关键字 not_in** 

例如 ，有一个列表，其中包含被禁止在论坛上发表评论的用户 ，就可在允许用户提交评论前检查他是否被禁言

```python
banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not_in banned_users:
    print(user.title() + " , you can post a response if you wish .")
```



### 布尔表达式

布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容

```python
game_active = True
can_edit = False
```

在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。



## 语句

**if-else 语句**



**if-elif-else 语句**

检查超过两个的情形 。python只执行 if-elif-else 结构中的一个代码块，遇到测试通过时，跳过余下的测试

```python
age = 12

if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is $5')
else :
    print("Your admission cost is $10")
```



better:

```python
age = 12

if age<4:
    price = 0
elif age < 18 :
    price = 5
else :
    price = 10
    
print("Your admission cost is $" + str(price) + ".")
```



**省略 else 代码块**

else 的特性可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替else 代码块 



**测试多个条件**

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings :
    print("Adding mushrooms")   
if 'pepperoni' in requested_toppings :
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
   
print("\nFinished making your pizza!")
```



## if 语句处理列表



```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers' :
        print("Sorry, we are out of green peppers right now") 
    else:
        print("Adding" + requested_topping + ".")
```



**确定列表不是空的**

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping + ".")
    print("\nFinished making your pizza!")

else :
    print("Are you sure you want a plain pizza?")
```



**使用多个列表**

```python
avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
```







# 用户输入



## **函数input()**

函数 input() 让程序暂停运行，等待用户输入一些文本 。获取用户输入后 ，python将其存储在一个变量中，以方便你使用。

**函数 input() 接收一个参数 ：即要向用户显示的提示或说明，让用户知道该如何做 。**

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

"""
python 在运行第1行代码时 ，用户将看到提示 ：Tell me something, and I will repeat it back to you: ， 程序等待用户输入 ，并在用户按回车键后继续运行 。
输入存储在变量 message中 ，接下来 print(message) 将输入呈现给用户 。
"""
```



### 使用 int() 来获取数值输入

**使用 input() 时，python将用户输入解读为字符串 。**

```python
height = input("How tall are you, in inches?")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride !")
else :
    print("\nYOu'll be able to ride when you're a little older.")
```







## while循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```



可使用while循环让程序在用户愿意时不断地运行

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the programe. "

message = ""
while message != 'quit' :
    message = input(prompt)
    if message != 'quit' :
    	print(message)
```





### 使用标志

导致程序结束的事件有很多时，如果在一条 while语句中检查所有这些条件，将既复杂又困难

在要求很多条件都满足才继续运行的程序中，可定义一个变量 ，用于判断整个程序是否处于活动状态。这个变量被称为**标志**

这样在while语句中就只需检查一个条件，并将所有测试都放在其他地方

```python
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
# 简化了while语句，因为不需要在其中做任何比较 —— 相关的逻辑由程序的其他部分处理
```



### break退出循环

```python
prompt = "\nPlease enter the name of a city you have visited: "
prompt+= "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title())
```



### 循环中使用 continue

continue 回到循环开头，并根据条件测试结果决定是否继续执行循环

```python
current_number = 0
while current_number < 10:
    current_number += 1 
    if current_number % 2 ==0 :
        continue
    print(current_number)
```



### while循环处理列表和字典

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    #函数 pop()从列表末尾删除元素
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
```



#### 删除**包含特定值的所有列表元素**

函数 remove() 删除特定值但只删除第一次出现的该值

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')  
```





#### 使用用户输入来填充字典

```python
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond?(Yes/ No) ")
    if repeat = 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name+ " would like to climb "+ response+ ".")
```





# 函数



## 基操

- **定义函数**

```python
def greet_user(username): 
    print("Hello," + username.title() + "!")
    
greet_user('jesse') #函数调用
```



- **传递实参的两种方式**

  **位置实参**:  实参和形参的顺序相同

  **关键字实参**：每个实参都由变量名和值组成

  - **位置实参**

    基于形参位置传递实参

    ```python
    def describe_pet(animal_type, pet_name):
        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
        
    describe_pet('hamster', 'harry')
    describe_pet('dog', 'willie')
    ```

  - **关键字实参**

    关键字实参 : 传递给函数的 *名称-值* 对, 因此实参和形参顺序无需一致 。

    ```python
    describe_pet(animal_type='hamster', pet_name='harry')
    describe_pet(pet_name='harry', animal_type='hamster')
    ```





- **默认值**

  - **给形参指定默认值时，等号两边不要有空格** 

  - 调用函数时若提供实参，则使用指定的实参值；否则，使用形参的默认值 。

  - 形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。否则可能导致没有默认值的实参没有值 。

```python
def describe_pet(pet_name, animal_type = 'dog'):
    ...
    
describe_pet(pet_name='willie')
```

**应用 ：让实参变成可选的**

这样函数调用者只需在必要时才提供额外的信息。

```python
def get_formatted_name(first_name,  last_name, middle_name=' '):
	full_name = first_name + middle_name + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
musician = get_formatted_name('jimi','hendrix', 'm')
```





- **传递列表**

  - *在函数中对列表所做的任何修改都是永久性的*

  - *若要禁止函数修改列表* ：向函数传递列表的副本，这样函数所做的任何修改都只影响副本，而不影响原件 `function(list[:])`

    切片表示法[:]  : 创建列表的副本。

    虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，可避免花时间和内存创建副本，从而提高效率





## `*args` and `**kwargs`



**传递任意数量的实参 : *args**

The ` args ` stands for arguments that are passed to the function ,`*args `can also print data of various types which is passed into the function

python允许函数从调用语句中收集任意数量的实参。

```python
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

`*`让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。



**结合使用 位置实参 和 任意数量实参**

python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。**因此函数定义中需将接纳任意数量实参的形参放在最后**

```python
def make_pizza(size, *toppings):
    print("\nMaking a "+ str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+ topping)
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```



**传递任意数量的关键字实参 ： `**args`**

`kwargs` stands for keyword arguments which are passed along with the values into the function（和值一起传递到函数中的关键字参数）



有时需要接收任意数量的实参，但预先不知道传给函数的会是什么样的信息 ： 可将函数设为能够接受任意数量的键值对

Example：创建用户简介，你知道将收到有关用户的信息，但不确定会是什么样的信息。

```python
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
      profile['key'] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
```

形参 `**user_info `中的`**`让 python 创建一个名为 user_info 的空字典，并将收到的所有 `key-value`键值对封装到这个字典中。









## 将函数存储在模块中

**将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。** **import语句允许在当前运行的程序文件中使用模块中的代码**



### PYTHONPATH

```
pip install DBUtils==1.3
Requirement already satisfied: DBUtils==1.3 in ./venv/lib/python3.9/site-packages (1.3)
```

复制上面的路径,然后在terminal终端执行下面这条命令，即可将刚才的包路径添加到环境变量中。

```
export PYTHONPATH=./venv/lib/python3.9/site-packages:$PYTHONPATH
```







### `import module_name`



- **指定导入模块的名称和函数名来调用被导入的模块中的函数**

```python
module_name.function_name()
```



- **Example :**

module pizza.py

```python
def make_pizza(size, *toppings):
    print("\nMaking a "+ str(size)+ "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```



在pizza.py 所在的目录中创建一个名为 making_pizzas.py 的文件， 这个文件导入刚创建的模块，再调用make_pizza()

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

python 读取这个文件时， `import pizza`让python 读取文件 pizza.py , **并将其中的所有函数都复制到这个程序中**。

你看不到复制的代码，程序运行时python后台自动复制这些代码。 







### `from module_name import function_name`



```python
#通过逗号分隔函数名，可根据需要从模块中导入任意数量的函数
from module_name import function_0, function_1, function_2
```



- 若导入特定函数，调用函数时就无需 `.`

  由于在import语句中显式地导入了函数 , 因此调用它时只需指定其名称，而不用指定模块名

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```





### `from module_name import *`



**由于导入了所有函数，可通过名称来调用每个函数，而无需使用`.`**

```python
from module_name import *
```

然而，使用并非自己编写的大型模块时，最好不要采用这种方法： 如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意向不到的结果：python可能遇到多个相同名称的函数或变量，进而覆盖函数，而不是分别导入所有的函数







###  as 给函数/模块指定别名

如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定别名。

```python
from module_name import function_name as fn
```



- **as给模块指定别名**

通过给模块指定简短的别名，让你能够更轻松地调用模块中的函数。这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。

```python
import module_name as mn
```



### lambda 

An anonymous inline function consisting of a single expression which is evaluated when the function is called. 

syntax : `lambda [parameters]: expression





## `__main__`



When a developer executes a Python program, the interpreter sets several variables, including *__name__.* 

two outcomes for the *__name__* variable:

- If the script is run as a standalone application, __name__ is set to __main__.

- If the script is imported, __name__ is set to the name of the module.

  When a python module or package is imported,  `__name__` is set to the module's name. 

  However, if the module is executed in the top-level code environment, its `__name__` is set to the string `'__main__'`.

```python
>>> import configparser
>>> configparser.__name__
'configparser'
```





- **What is the “top-level code environment”  ?**

  `__main__` is the name of the environment where top-level code is run. “Top-level code” is the first user-specified Python module that starts running. It’s “top-level” because it imports all other modules that the program needs. Sometimes “top-level code” is called an *entry point* to the application.

  

  **The top-level code environment can be :**

  - **the scope of an interactive prompt :**

    ```python
    >>> __name__
    '__main__'
    ```

  

  - **the Python module passed to the Python interpreter as a file argument:**

    ```python
    $ python helloworld.py
    Hello, world!
    ```

  

  - Python code passed to the Python interpreter with the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) argument:

    ```
    $ python -c "import this"
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    ...
    ```

​			and more ...

In each of these situations, the top-level module’s `__name__` is set to `'__main__'`.



#### Executing modules as scripts

When you run a python module with `python fibo.py <arguments>`  , the code in the module will be executed, just as if you imported it, but with the `__name__` set to `"__main__" ` ，

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

 you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as "main" file:

```
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

If the module is imported, the code is not run:

```
>>> import fibo
>>>
```



**When not to use *`if __name__ == "__main__"`***

The *if name equals main* syntax is not required if all you want to do is run a Python script. New Python developers can code and explore a wide variety of AI, [machine learning](https://www.techtarget.com/searchapparchitecture/tip/Frameworks-libraries-and-languages-for-machine-learning) and [statistics libraries](https://www.techtarget.com/searchbusinessanalytics/feature/15-data-science-tools-to-consider-using) and never encounter a need to use the construct.

The use of Python's `if __name__ == "__main__"`: makes the most sense in the following three scenarios:

- You want to write code that executes only when the script is run as a main program and not when it is imported as a module.
- You want to include test routines that run independently to validate functions defined in the file.
- You want to include demonstration code that will not execute upon module import.









# 类

## **规范**

 我们通常可以认为首字母大写的名称指的是类，而小写的名称指的是根据类创建的实例。

- 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线
- 类中使用一个空行来分隔方法；而在模块中，使用两个空行来分隔类。

```python
class Dog():#这个类定义中的括号是空的，因为我们要从空白创建这个类。
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " s now sitting .")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
```

## 实参 self

- 实参self : 所有与类相关联的方法调用都**自动传递实参 self** ，它是一个指向实例本身的引用 ，让实例能够访问类中的属性和方法。

  - 以self为前缀的变量都可供类中的所有方法使用，
  - self.name = name 获取存储在形参name中的值，并将其存储到变量name中 ，然后该变量被关联到当前创建的实例

  

  

## **根据类创建实例**

可将类视为有关如何创建实例的说明。

`my_dog = Dog('willie', 6)`	**使用实参调用Dog类中的方法 `_init_()` ** ，**方法 `_init_()` 并未显式地包含return语句，但python自动返回一个表示这条小狗的实例**。



## 属性

**属性 : 可通过实例访问的变量**

. 访问实例的属性

`my_dog.name` ,在这里，python先找到**实例** my_dog, 再查找与这个实例相关联的属性name 。

**调用方法**

```python
my_dog.sit()
my_dog.roll_over()
```



## 方法` __init__()`

**类中的函数称为方法**

`__init__()`是一个特殊的方法，**每当你根据Dog 类创建新实例时，python都会自动运行它**。

`__init__()`定义中，形参self必不可少，且须位于其他形参前。

python调用 `__init__()` 来创建Dog实例时，**将自动传入实参self** ，因此通过 **实参**向Dog()传递name和age ，self 会自动传递 ，我们不需要传递它。每个与类相关联的方法调用都自动传递实参 self ，它是一个指向实例本身的引用 ，让实例能够访问类中的属性和方法。





**给属性指定默认值**

**类中的每个属性都必须有初始值**，哪怕这个值是0或空字符串。

在有些情况下，如设置默认值时，在方法 `__init__()`内指定这种初始值是可行的；如果你对某个属性这样做了 ，就无需包含为它提供初始值的形参。



## 修改属性的值

修改属性的值的两种方法：直接通过实例进行修改；通过方法进行设置



```python
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
	def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```







1. **直接修改属性的值**

```python
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```



2. **通过方法修改属性的值**

这样就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新

```python
class Car():
    --snip--
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
       
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```



**通过方法对属性的值进行递增**

```python
class Car():
    --snip--
    
    def update_odometer(self, mileage):
        --snip--
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_userd_car = Car('subaru', 'outback', 2013)

my_used_car.increment_odometer(100)
```



## 继承

一个类继承另一个类时，它将自动获取另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。

**子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。**



### 子类的方法



#### `__init__()`

创建子类的实例时，python首先要给继承自父类的所有属性赋值。

```python
class Car():
	--snip--
    
    

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

- 父类必须包含在当前文件中，且位于子类前。
- super() 函数：将父类和子类关联起来。super() 调用父类的方法 `__init__()` ， 让ElectricCar 实例包含父类的所有属性 。父类也称为超类( superclass ) ， 名称super因此得名



#### 给子类定义属性和方法

```python
class Car():
    --snip--
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery.")        
```



#### 重写父类的方法

**在子类中定义一个与要重写的父类的方法重名的方法。**

```python
def ElectronicCar(Car):
    --snip--
# 假设Car类有一个fill_gas_tank的方法，它对全电动汽车来说毫无意义    
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")
# 如果有人要对电动汽车调用方法 fill_gas_tank，python将忽略Car类中的方法，转而运行上述代码
```





### 将实例用作属性

将大型类拆分成多个协同工作的小类。

例如，不断给 ElectricCar 类添加细节时，我们可能会发现其中包含很多专门针对汽车电瓶的属性和方法，我们可将这些属性和方法提取出来，放到另一个名为 Battery 的类中，并将一个 Battery 实例作为 ElectricCar 类的一个属性

```python
class Car():
    --snip--
    
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."  
        print(message)

        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.battery = Battery()
 

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```





## 导入类

将类存储在模块中，然后在主程序中导入所需的模块

car.py

```python
"""一个可用于表示汽车的类"""
class Car():
"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
        
	def get_descriptive_name(self):
		"""返回整洁的描述性名称"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
    
	def read_odometer(self):
		"""打印一条消息，指出汽车的里程"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
        
	def update_odometer(self, mileage):
		"""将里程表读数设置为指定的值拒绝将里程表往回拨"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
            
            
	def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
		self.odometer_reading += miles

        
        
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."  
        print(message)

        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.battery = Battery()
```



### 导入多个类

import 语句让python打开模块并导入类

```python
from module_name import class_name
```



my_car.py

```python
from car import Car， ElectricCar
my_new_car = Car('audi', 'a4', 2016) ，#创建实例
```



### **导入整个模块**

使用 **module_name.class_name** 访问需要的类

导入整个模块，再使用句点表示法访问需要的类。**由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突**

```python
import car

my_beetel = car.Car('volkswagen', 'beetle', 2016)

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
```







## python标准库

python标准库是一组模块，安装的python都包含它 。



**OrderedDict 类**

字典让你能够将信息关联起来，但它们不记录你添加键值对的顺序。要创建字典并记录其中的键值对的添加顺序，可使用模块 **collections 中的 OrderedDict 类**。 

```python
from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")
```



**模块 random**

模块 random 包含以各种方式生成随机数的函数，其中的 randint() 返回一个位于指定范围内的整数

```python
from random import randint
x = randint(1,6)
```





# 文件和异常



## 从文件中读取数据



### 读取整个文件



pi_digits.txt

```
3.1415926535
  8979323846
  2643383279
```



file_reader.py

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

- **函数open() :** 

  要以任何方式使用文件都得先打开文件，这样才能访问它。

  **参数：要打开的文件 (相对路径)**  , 注意windows系统中 文件路径中使用 \ 而不是 / 

  open() 返回一个表示文件的对象。

  

- **关键字 with**

  在不再需要访问文件后将其关闭。

  也可以调用open() 和close() 来打开和关闭文件，但这样做时如果程序存在bug，导致close()语句未执行，文件将不会关闭。

  

- **方法 read()** 

  **读取文件的全部内容，并将其作为一个长字符串存储在变量 contents 中**

  - 读取文本文件时，python将其中的所有文本都解读为字符串。

    如果你读取的是数字并要将其作为数值使用 ，就必须使用函数 int() 将其转换为整数 ，

  

- **换行**

  相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。

  因为 read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。

  删除空行：`rstrip() ` , 删除字符串末尾的空白

```python
print(contents.rstrip())
```







### 逐行读取

对文件对象使用 for循环。

```python
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
# 若无 rstrip() ， 每行都会多出一个空白行。因为这个文件中，每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，因此每行末尾都有两个换行符: 一个来自文件，另一个来自 print语句
```



### 作用域

**创建一个包含文件各行内容的列表**



- 使用关键字with时，open() 返回的文件对象只在 with代码块内可用。

  要在with代码块外访问文件的内容 ，可在**with代码块内将文件的各行存储在一个列表中**

```python
with open(filename) as file_object:
    lines = file_object.readline()

string = ''
for line in lines:
 	string += line.strip()
```







## 写入文件

首先也需要先打开文件 ( `with open() as `)



### 写入空文件

要将文本写入文件，调用 open() 时需要提供模式实参

- **格式问题**

  python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str() 将其转换为字符串格式

- **模式实参**

  如果你省略了模式实参，python将以默认的只读模式打开文件。

  - r : 只读
  - w : 写入模式
  - a : 附加模式
  - r+ : 读取和写入文件

- 如果你要写入的文件不存在，函数 open() 将自动创建它。

  然而 ，以 w模式打开文件时注意 ：**如果指定的文件已经存在，python将在返回文件对象前清空该文件**

```python
with open(filename, 'w') as file_object:
    file_objcect.write("I love programming.")
```





**写入多行**

函数 write() 不会在你写入的文本末尾添加换行符 ，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样

```python
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```



### 附加到文件

- 如果你要给文件添加内容，而不是覆盖原有的内容，可以`a` 模式打开文件。

  - 以附加模式打开文件时，你写入到文件的行都将添加到文件末尾。
  - 如果指定的文件不存在，python将为你创建一个空文件。



## 异常

python使用被称为**异常**的特殊对象来管理**程序执行期间发生的错误**。

**如果你编写了处理该异常的代码，程序将继续运行**；**如果你未对异常进行处理，程序将停止，并显示一个 traceback ， 其中包含有关异常的报告**

try-except 代码块让python执行指定的操作，同时告诉python发生异常时怎么办。使用 try-except 代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是 traceback 。

让用户看到traceback不是好主意，用户可能通过 traceback获悉你不希望他知道的信息。例如他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。



### 使用异常避免崩溃

发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中：如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。



```python
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
        
    answer = int(first_number) / int(second_number)
```

该程序没有任何处理错误的措施，因此让它执行 除数为0的除法运算时，它将崩溃。





通过将可能引发错误的代码放在 try-except 代码块中，可提高这个程序抵御错误的能力。

```python
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

依赖于 try代码块成功执行的代码都放在 else代码块中

**try-except-else 代码块的工作原理**：python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。

若try代码块成功执行：执行else代码块。

若运行try代码块引发了指定异常： 则执行except代码块





###  ZeroDivisionError异常

![image-20240217220132934](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240217220132934.png)



**使用 try-except 代码块**

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#如果try 代码块中的代码运行起来没有问题，python将跳过except代码块;如果try代码块中的代码导致了错误，python将查找这样的except代码块，并运行其中的代码
```



### FileNotFoundError 异常



```python
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
    	contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."

else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = words.len()
    print("The file " + filename " has about "+ str(num_words) + " words")
```



```python
def count_words(filename):
    try:
		with open(filename) as f_obj:
    		contents = f_obj.read()
	except FileNotFoundError:
    	msg = "Sorry, the file " + filename + "does not exist."

	else:
   	 	# 计算文件大致包含多少个单词
    	words = contents.split()
    	num_words = words.len()
    	print("The file " + filename " has about "+ str(num_words) + " words")
        
        filenames = ['alicetxt', 'siddhartha,txt', 'little_women.txt']
        for filename in filenames:
            count_words(filename)
```

两个优点：

1.避免用户看到traceback

2.让程序能够继续分析其他文件( 若中途出现找不到文件的情况， 引发FileNotFoundError 异常后程序停止运行)



**失败时一声不吭**

并非每次捕获到异常时都需要告诉用户。python有一个pass语句，可在代码块中使用它来让python什么都不要做

```python
try:
    --snip--
except FileNotFoundError:
    pass
else:
    --snip--
```



## 存储数据

程序把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，你几乎总是要保存他们提供的信息 : 一种简单的方式是使用模块json来存储数据

模块json让你能够将简单的python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。

JSON : JavaScript Object Notation 格式最初是为 JavaScript开发的，随后成立一种常见格式，被包括python在内的众多语言采用



### json.dump()  json.load()



number.josn

```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    
#json.dump() 接收两个实参：要存储的数据以及可用于存储数据的文件对象
```



```python
import json

filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
# open 函数默认以只读方式打开文件    
print(numbers)
```



**保存和读取用户生成的数据**

remember_me.py

```python
import json

username = input("What is your name? ")

filename = 'username.josn'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username)
```



greet_user.py

```python
import json

filename = 'username.josn'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username )
```



- 将两个程序合并到一个程序 remember_me.py 中。 这个程序运行时，我们将尝试从文件 username.json 中获取用户名，因此我们首先编写一个尝试恢复用户名的try代码。
- 如果这个文件不存在，我们就在except代码块中提示用户输入用户名 ，并将其存储在username.json 中

remember_me.py

```python
import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
    	username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
else:
    print("Welcome back, " + username)
```



**重构** ： 将代码划分为一系列完成具体工作的函数

```python
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("...")
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            
def greet_user():
    username = get_stored_username()
    if username:
        print("...")
	 else:
        get_new_username()
            
    
greet_user()   
```





# unittest



## Basic



https://docs.python.org/3/library/unittest.html

unittest supports concepts in an object-oriented way :

- **test fixture** 

  A test fixture represents the preparation needed to perform tests , and any associated cleanup actions .

  This may involve, for example, creating temporary or proxy databases, directories , or starting a server process.

- **test case**

  the individual unit of testing . It checks for a specific response to a particular set of inputs.

  unittest provides a base class -- TestCase , which may be used to create new test cases.

- **test suite**

  a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together .

- **test runner**

  a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.



### TestCase

`TestCase` class is intended to be used as a base class, with specific tests being implemented by concrete subclasses.

This class implements the interface needed by the test runner to allow it to drive the tests, and methods that the test code can use to check for and report various kinds of failure.



- provide 3 groups of methods:
  - used to run test
  - used to check conditions and report failures
  - inquiry methods allowing information about the test itself to be gathered



#### Second Group

The [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase) class provides several assert methods to check for and report failures.

| Method                  | checks that      |
| ----------------------- | ---------------- |
| assertEqual(a, b)       | a == b           |
| assertNotEqual(a, b)    | a != b           |
| assertTrue(x)           | bool(x) is True  |
| assertFalse(x)          | bool(x) is False |
| assertIn(item, list)    | item is in list  |
| assertNotIn(item, list) | item not in list |
| assertIsInstance(a, b)  | isinstance(a, b) |









### demo

```python
import unittest

class TestStringMethonds(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
    	self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
               
if __name__ == '__main__':
    unittest.main()
```



- **Naming Convention**
  - The three individual tests ard defined with methods whose names start with the letters `test` , **This naming convention informs the test runner about which methods represent tests .**







## 测试函数

the_function_to_be_tested

```python
def get_formatted_name(first, last):
    formatted_name = first.title() + ' ' + last.title()
    return formatted_name
```



test_name_function.py

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #创建一个名为 NamesTestCase 的类，用于包含一系列针对 get_formatted_name 的单元测试
    """ 测试 name_function.py """
    def test_first_last_name(self):
    	formatted_name = get_formatted_name('janis', 'joplin')
    	self.assertEqual(formatted_name, 'Janis Joplin')
    
unittest.main()
```





```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

# 第一行的 . 表明有一个测试通过了， 最后的 OK 表明该测试用例的所有单元测试都通过了
```



**不能通过的测试**

name_function.py

``` python
def get_formatted_name(first, middle, last):
    full_name = first + ' ' + middle + ' ' + last
    return full_name
```



![image-20240227205638904](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240227205638904.png)



improve: 将middle变为可选参数

```python
def get_formatted_name(first, last, middle=''): 
#注意默认参数需要放在参数列表的末尾，否则传参会默认按位置传参
```



## 测试类



survey.py

```python
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self):
        """存储一个问题，并未存储答案做准备"""
        self.question = question
    	self.responses = [] 
    
    def show_question(self):
        print(question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
        
    def show_results(self):
        print("Survey results:")
        for response in responses:
            print("- " + response)
    
    
```



language_survey.py

```python
from survey import AnonymousSurvey

question = "What language did you first learn to speak ? "
my_survey = AnonyousSurvey(question)
#隐式调用 class AnonyousSurvey 的构造函数 __init__ , 自动传递参数 self ，以及形参 question

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
my_survey.show_results()
```



test_survey.py

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        
        
    def test_store_three_response(self):
        ...
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
            
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()
```



### 方法setUp()

上面的 test_survey.py中， 我们在每个测试方法中都创建了一个 AnonymousSurvey 实例，并在每个方法中都创建了 responses

unittest.TestCase 类包含方法 setUp() , 让我们只需要创建这些对象一次，并在每个测试方法中使用它们。

如果你在 TestCase 类中包含了方法 setUp() , python 将先运行它，再运行各个以 test_ 打头的方法。这样，在你编写的每个测试方法中都可使用在 setUp() 中创建的对象



```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def SetUp(self):
        """创建一个question和 responses供测试方法使用"""
        question = "What languag did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
        def test_store_single_response(self):
            self.my_survey.store_response(self.resonses[0])
            self.assertIn(self.response[0], self.my_survey.responses)
            
        def test_store_three_responses(self):
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)
                
unittest.main()
```













# Functions
