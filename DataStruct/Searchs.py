#这个文件是存查找算法的各种常见的查找算法


# 首先是二分查找
# 有一个先决条件是，输入的数组必须是已经排好序的，默认从小到大
def binary_search(key,lists)->int:   # 返回下标  
    front = 0  # 下标
    end = len(lists)-1
    half = (front+end)//2  # 取整数
    while front<=end:
        if lists[half] == key:
            print(f"找到值为{key}的值在列表的{half}下标的位置")
            return half-1
        elif lists[half]>key:
            end = half-1
            half = (front+end)//2
            # print("估大了")
        elif lists[half]<key:
            front = half+1
            half = (front +end)//2
            # print("估小了")
    # print("没有找到这个")
    return -1

binary_search(6,[1,2,3,4,5,6])
