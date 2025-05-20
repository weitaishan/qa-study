def merge_sf():
    num2_str=input("请输入列表2的元素，用空格分隔：")
    num2=list(map(int,num2_str.split( )))
    a=len(num2)
    num1_str=input("请输入列表1的元素，用空格分隔：")
    num1=list(map(int,num1_str.split( )))
    for i in range(0,a):
        num1.append(0)
    num1[-a:]=num2
    print(num1)
    #使用冒泡排序将列表中的数据从小到达排列：相邻两两比较
    b=len(num1)
    for i in range(b-1):

merge_sf()
