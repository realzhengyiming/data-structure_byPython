#encoding:utf-8
def select_sort(lists):
    min = 0
    for i in range(0,len(lists)):
        min = i
        for j in range(i+1,len(lists)):
            if lists[j]<lists[min]:
                min = j
        lists[min],lists[i] = lists[i],lists[min]
    return lists


def bubble_sort(lists):
    for i in range(0,len(lists)-1):  # 两两比较移动，n-1 次就可以，就好像分成n段，n-1 次就可以
        for j in range(len(lists)-i-1):  # 注意：这儿需要减去一轮 ，这是为什么呢
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
    return lists


# 归并排序两部分，这个是合并有序数列
def merge(left,right):
    i,j = 0,0  # 初始化i,j
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1    # 写while 的时候不要忘记了要给计数器迭代
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # 这儿直接把i后面未添加的直接加进来，以为已经排好序了
    result += right[j:]    # 两个都是直接把后面的添加进来就好，默认leftlist比较小来处理，并且有序
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2   # python3中需要使用// 来获得整数的商
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])  # 这种就是递归的思想，不过左右边都一样的
    result = merge(left,right)
    return result


# 下面是快速排序
def quick_sort(lists,left,right):
    if left>=right:
        return lists
    low = 0   # 这儿的左边必须为最左边
    high = len(lists)
    key = lists[left]  # 这个就是pivot，设定这个作为比较的枢轴 ，把值暂存
    while left<right : # 只要上层的L R没相遇在同一个下标中，那就继续
        while left<right and lists[right] >= key:
            right -= 1   # 不断的往前移动
        lists[left] = lists[right]  # 把小的值给初始的left位置 
        while left<right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]   # 把这个大于中间值的数给右边
    lists[right] = key  # 出来while循环的时候就是L 和 R 相遇的时候，这时候把key放上去与就可以了
    print(lists)
    print(f" 0  1  2  3  4  5--enter  {left}  {right}")
    quick_sort(lists,low,left-1)  # 把左右的
    quick_sort(lists,left+1,high)
    return lists


if __name__ == '__main__':
    a = [6,4,3,7,8,2,1,1]
    print(a)
    print("排序结果")
    print(select_sort(a))
    print(bubble_sort(a))
    print(merge_sort(a))
    print(quick_sort(a,0,len(a)-1))

    