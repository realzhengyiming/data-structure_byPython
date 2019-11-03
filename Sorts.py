# 都默认他们是升序，从小到大

def insert_sort(lists):  # 简单插入排序
    count = len(lists)
    for i in range(1,count):
        for j in range(i,0,-1):  # 倒叙的应该也是可以的
            if lists[j-1]>lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1]
    return lists


def select_sort(lists):
    count = len(lists)
    for i in range(0,count):   # 第一层确保逐个往后移动确认最小值
        min = i  # 最开始，最左边的数字假装已经完成了排序，所以内层j从0+1开始
        for j in range(i+1,count):    # 得到除左边排序成功后的部分的最小的值
            if lists[min]>lists[j]:
                min = j
        lists[i],lists[min] = lists[min],lists[i]   # 最小值与i交换
    return lists


def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(count-1, i, -1):   # 从后面开始比到前面,下标和长度要区分开来
            if lists[j] < lists[j-1]:
                lists[j],lists[j-1] = lists[j-1],lists[j]
    return lists



print(insert_sort([2,3,4,1]))
print(select_sort([2,3,4,1]))
print(bubble_sort([2,3,4,1]))