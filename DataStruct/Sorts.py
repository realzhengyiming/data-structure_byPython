# encoding:utf-8
# 默认都是从小到大排序

# 1 选择排序比冒泡好，交换次数少
def select_sort(lists):
    for i in range(0, len(lists)):
        min = i  # 不同之处
        for j in range(i + 1, len(lists)):
            if lists[j] < lists[min]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]  # 这儿才交换
    return lists


# 2
def bubble_sort(lists):
    for i in range(len(lists)):  # i没用，所以没关系，遍历全部就可以了
        for j in range(len(lists) - 1):
            if lists[j] > lists[j + 1]:  # 把大的往后面沉 沉底的意思。默认都是从小到大
                lists[j], lists[j + 1] = lists[j + 1], lists[j]  # 每次都交换
    return lists


# 3
# 归并排序两部分，这个是合并有序数列
def merge(left, right):
    i, j = 0, 0  # 初始化i,j
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # 写while 的时候不要忘记了要给计数器迭代
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # 这儿直接把i后面未添加的直接加进来，以为已经排好序了
    result += right[j:]  # 两个都是直接把后面的添加进来就好，默认leftlist比较小来处理，并且有序
    return result


def merge_sort(lists):  # 先递归后合并处理（相当于后序遍历）
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2  # python3中需要使用// 来获得整数的商
    left = merge_sort(lists[:num])  # 返回的都是后面带顺序后的
    right = merge_sort(lists[num:])  # 这种就是递归的思想，不过左右边都一样的
    result = merge(left, right)
    return result


# 4
# 下面是快速排序，这个是很省空间的，数组原地进行变化
def quick_sort(lists, left, right):  # 而这边的left一定是0，right一定是len(lists)-1,一定是头和尾，不然会漏掉
    if left >= right:
        return lists
    low = left
    high = right
    pivot = lists[left]  # 这个就是pivot，设定这个作为比较的枢轴 ，把值暂存
    while left < right:  # 只要上层的L R没相遇在同一个下标中，那就继续,中途停下交换右标比pivot小的，左标比pivot大的
        # https://www.bilibili.com/video/BV1at411T75o/?spm_id_from=333.788.videocard.1
        while left < right and lists[right] >= pivot:  # l,r没相遇；并且右边的没遇到小于pivot的  ,它这个是先移动的右边。
            right -= 1  # 不断的往前移动
        lists[left] = lists[right]  # 遇到了就把小的值放到了pivot的位置上，然后才开始移动做光标。
        while left < right and lists[left] <= pivot:
            left += 1
        lists[right] = lists[left]  # ，刚才的r光标的值已经给了pivot位置，所以现是空。把这个大于中间值的数给右边这个空的位置
    lists[right] = pivot  # 出来while循环的时候就是L 和 R 相遇的时候，所以左右都一样。放上pivot值。这时候把key放上去与就可以了


    quick_sort(lists, low, left - 1)  # 把，让这一段就开始分治疗了，有多少个部分（就分多少个部分进行递归处理）
    quick_sort(lists, left + 1, high)
    return lists


# 5 插入排序
def insert_sort(lists):
    for i in range(1, len(lists)):  # 最左边的当成已经完成排序，所以从第一个开始
        key = lists[i]  # 依次取出已经排序好的列表最左端的未排序好的那个
        j = i - 1  # 减了1后就是从前面已经排序好的下标最大的那个开始，前面的一个
        while j >= 0:  # 每次选一个key和前面的"已排序"的比，只要大于就交换两值（类局部冒泡）
            if lists[j] > key:
                lists[j + 1] = lists[j]  # 大于的话就把值和下标大于1的互换，因为一开始key已经存好，不怕
                lists[j] = key
            j -= 1
    return lists


# 6堆排序
# def adjust_head(lists,i,size):
#     lchild = 2*i+1
#     rchild = 2*i+1
#     maxs =

# 7 希尔排序  这个没问题，插入排序的改进版，所以他的核心分组操作时为了
# 最后一次的插入操作整体已经变得相对的有序了，减少了插入排序最坏情况移
# 动距离过长的问题。
# 希尔排序中的增量就 相当于机器学习的那种了，可以用来调参了
# https://www.cnblogs.com/l199616j/p/10740165.html
def shell_sort(lists):
    count = len(lists)
    step = 2  # 一般默认/2 ，取多少这个是一个数学问题。2叫希尔增量
    group = count // step  # yp3中取整使用这个样子
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]  # 这儿也和选择排序一样，每次都暂存要处理的值
                while k >= 0:  # 这部分和选择排序是一样的
                    # 区别是直接的插入排序是lists[k+1] 这样连续的
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


if __name__ == '__main__':
    a = [6, 4, 3, 7, 8, 2, 1, 1]
    print(a)
    print("排序结果")
    print(select_sort(a))
    print(bubble_sort(a))
    print(merge_sort(a))
    print(quick_sort(a, 0, len(a) - 1))
    print(insert_sort(a))
    print(shell_sort(a))


