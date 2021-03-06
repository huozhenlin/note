# 什么是dict(字典)  
字典，又称关联数组或哈希数组，其实也是一个数组类型的对象，和普通的数组不一样，哈希数组的索引是通过哈希函数处理
后得到的散列值。哈希函数的目的主要是为了让value能够均匀的分布在数组中，使得插入，删除，查找的时间复杂度都为
O(1)。

哈希函数设计的困难点在于如何让值均匀分布在数组中，从而减少哈希冲突。  

课外拓展：  
所谓哈希冲突，其实就是对不同的文本进行哈希计算，得出的哈希值是一样的。这一碰撞实验早在2003年让中国的某一大学教授发现，并且于
一周后，也实现了sha128的碰撞实验。因此，在后续密码学领域中，sha128加密算法升级到了sha256和sha512。

# 建立哈希表的过程  

1. 把key通过哈希函数处理后得到一个整数值，将此整数值对数据长度进行一个取余操作，从而计算出value该存放在数组的哪个位置
中。在[list底层实现](./list底层实现.md)中提到，数组的一个动态扩容机制，首先是开辟长度为8的内存空间，当数组元素长度阈值
时，触发动态扩容机制，已4倍的容量进行扩容，当数据的长度到达50000时，扩容速度降低为2倍。  

2. 字典查询的话，和添加一样。对key进行哈希求余，得到数组的下标索引，准确定位并取出元素。  

什么对象可哈希呢？  
在python中，所有不可变的数据类型都可哈希，如String,tuple,int。可变的数据类型，如list,dict,set是不可哈希的。

# 常见的解决哈希冲突的办法  
## 开放寻址法  
开放寻址法，将所有元素都放在散列表中，当产生哈希冲突时，通过探测函数计算下一个存放位置，若依旧冲突，则递归寻找，直到
找到位置。  

## 再哈希法  
按照顺序规定多个哈希函数，每次查询的时候按顺序调用哈希函数，调用到第一个为空的时候返回不存在，调用到此键的时候返回其值。

## 链地址法  
将所有哈希值相同的记录放在同一个链表中，这样子就不占用其他的哈希地址，相同的哈希值存放在同一个链表中，按顺序遍历即可找到。 

## 公共溢出区
所有关键字和基本表中的关键字为相同的哈希记录，不管他们的哈希函数得到的哈希地址是什么，都存入到公共溢出区。

[参考链接：Python字典（dict）底层实现原理](https://blog.csdn.net/limengshi138392/article/details/97929500)  


