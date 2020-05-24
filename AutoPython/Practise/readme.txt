1.CharacterSet 字符集处理比较重要
2.Collection 集合
3.FileOperate  常见的一些文件操作
   3.1 FileOperate.py   循环读取txt文件中的每一行，并且做到了不读取某一行的作用，另外就是两种for循环方式的比较
   3.2 FileOperate2.py  演示断电情况下如何保证写入的数据不丢失 比如f.flush()
   3.3 FileOperate3.py  truncate(10)方法的使用，从第十个字符开始截断
   3.4 FileOperate4.py  f = open("YesterDay", 'r+', encoding='utf-8') 几种模式，r+,w+,a+分别为读写，写读，追加写
   3.5 FileOperate5.py  根据字符串修改，类似于linux中的sed批量替换功能，并且保留源文件，写入内容到bak文件
   3.6 FileOperate6.py  with open('file','r') as f 这种写法避免忘记关闭文件
   3.7 ProgressBar      类似于yum下载效果的进度条



4.CarShopping。py 简易的购物车实现功能，但是for循环较多，比较low
5.ThreeLevelDictionary.py 类似于三级菜单的效果

