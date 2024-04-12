# 读Python 代码解题

加密原理 ：参数 key 为密钥 ，首先采用循环重复的方式扩展密钥长度，使其长度与flag相同 。将flag与密钥进行按位异或运算即可得到密文  即 .enc 文件  。又由于异或运算的可逆性 ，将密文与密钥再次异或就得到flag 。



(1) 下载对应的压缩包（Crack-1、Crack-2、Crack-3、Crack-4、Crack-5），按要求分析得到Flag；

(2) Crack-1：下载密码检查器，同时还需要同一目录下的经过加密后的Flag 文件。

![image-20240409190148926](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409190148926.png)

由`user_pw == "8713"`  知 user_pw = 8713



(3) Crack-2：下载密码检查器，同时还需要同一目录下的经过加密后的Flag 文件。

由` user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)` 知 user_pw= 4ec9

![image-20240409191323485](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409191323485.png)



(4) Crack-3：下载密码检查器，同时还需要同一目录下的经过加密后的Flag 文件与哈希值。有7 个可能的密码，其中1 个是正确的。你可以通过分析密码检查器脚本找到这些密码。

分析得题目将输入的 user_pw hash后与 correct_pw_hash 比较，若一致则输出 flag ， 因此编写脚本获取正确密码 。

![image-20240409191936798](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409191936798.png)

![image-20240409192150208](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409192150208.png)





(5) Crack-4：下载密码检查器，同时还需要同一目录下的经过加密后的Flag 文件与哈希值。有100 个可能的密码，其中只有1 个是正确的。你可以通过分析密码检查器脚本找到这些密码。

思路与 (4) 同

![image-20240409192308829](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409192308829.png)



 (6) Crack-5：下载密码检查器，同时还需要同一目录下的经过加密后的Flag 文件与哈希值。这里有一本字典，根据我们目前看到的密码惯例，收录了所有可能的密码。

首先读取 dictionary.txt 的文件内容，然后用 split() 函数按空格拆分获得字符串列表 ，剩余思路与上两题一致 。

![image-20240409192611689](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409192611689.png)

![image-20240409192556260](C:\Users\89388\AppData\Roaming\Typora\typora-user-images\image-20240409192556260.png)







# z3

```
from z3 import *

solver = z3.Solver()
a = Int('a')
b = Int('b')
c = Int('c')
nums = ['291','245','463','578','569']
solver.add(1 <= a, a <= 9, a != 5, a != 7,a != 8)
solver.add(1 <= b, b <= 9, b != 5, b != 7,b != 8)
solver.add(1 <= c, c <= 9, c != 5, c != 7,c != 8)

for num in nums :
    ca = And(a != num[0],a != num[1],a != num[2])
    cb = And(b != num[0], b != num[1], b != num[2])
    cc = And(c != num[0], c != num[1], c != num[2])

    if(num == nums[0]):
        solver.add(Or(
        And(a == num[0] , cb, cc),
            And(ca , b == num[1], cc),
            And(ca , cb, c == num[2])
        ))
    if(num == nums[1]):
        solver.add(Or(
            And(ca, b == num[0] , cc) ,
        And(ca, cb , c == num[0]),
        And(a == num[1], cb , cc) ,
        And(ca, cb, c == num[1]),
        And(a == num[2], cb , cc) ,
        And(ca, b == num[2] , cc)
        ))

    if (num == nums[2]):
        solver.add(Or(
            And(ca, b == num[0], c == num[1]),
            And(a == num[1], b == num[0], cc),
            And(a == num[1], cb, c == num[0]),

            And(a == num[1], b == num[2], cc),
            And(a == num[2], cb, c == num[1]),
            And(ca, b == num[2], c == num[1]),

            And(a == num[2], b == num[0], cc),
            And(a == num[2], cb, c == num[0]),
            And(ca, b == num[2], c == num[0]),
        ))

    if(num == nums[3]):
        solver.add(
            And(ca, cb, cc)
        )

    if(num == nums[4]):
        solver.add(Or(
        And(ca, b==num[0],cc),
            And(ca, cb, c == num[0]),

            And(a==num[1], cb, cc),
            And(ca, cb, c == num[1]),

            And(a == num[2], cb, cc),
            And(ca, b == num[2], cc ),)
        )




if solver.check() == sat:
    model = solver.model()
    print("a =", model[a])
    print("b =", model[b])
    print("c =", model[c])

```

