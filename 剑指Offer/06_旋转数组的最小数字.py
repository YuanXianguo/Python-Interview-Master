"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
"""
"""
分析：二分查找的变形，注意到旋转数字的首元素肯定不小于尾元素，设置中间点。
如果中间点大于首元素，说明最小数字在后面一半，反之在前一半，依次循环。
同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。
但是，当首元素等于尾元素等于中间值，只能在这个区域顺序查找
"""


def find_min_num_in_rotate_array(array):
    if not array:
        return 0
    front = 0
    rear = len(array) - 1
    min_index = 0
    # 初始最小位置设在首元素，如果首元素小于尾元素，不经while循环直接返回
    while array[front] >= array[rear]:  # 进入二分查找
        if rear - front == 1:  # 二分查找结束
            min_index = rear
            break
        mid = (rear + front) // 2
        # 如果首元素，尾元素，中间元素都相等，对该段数组进行遍历
        if array[mid] == array[front] and array[mid] == array[rear]:
            for i in range(front, rear + 1):
                if array[i] < array[mid]:
                    return i, array[i]
        # 类似[3,4,5,6,0,1,2]
        if array[mid] >= array[rear]:
            front = mid
        # 类似[2,2,3,4,5,6,6]
        elif array[mid] <= array[rear]:
            rear = mid
    return min_index, array[min_index]


def minNumberInRotateArray(rotateArray):
    # write code here
    if not rotateArray:
        return 0
    res = 0
    left, right = 0, len(rotateArray) - 1
    while rotateArray[left] >= rotateArray[right]:
        if right - left == 1:
            res = right
            break
        mid = (left + right) // 2
        if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
            for i in range(left, right):
                if rotateArray[i] < rotateArray[left]:
                    return rotateArray[i]
            return rotateArray[left]
        elif rotateArray[left] <= rotateArray[mid]:
            left = mid
        elif rotateArray[left] > rotateArray[mid]:
            right = mid
    return rotateArray[res]


def min_num(rotateArray):
    if not rotateArray:
        return 0
    left, right = 0, len(rotateArray) - 1
    while left < right:
        mid = (left + right) // 2
        if rotateArray[mid] > rotateArray[right]:
            left = mid + 1
        elif rotateArray[mid] == rotateArray[right]:
            right -= 1
        else:
            right = mid
    return rotateArray[left]


if __name__ == '__main__':
    lst = [4,5,6,7,1,2,3]
    print(find_min_num_in_rotate_array(lst))
    print(minNumberInRotateArray(lst))
    print(min_num(lst))
    lst2 = [5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5]
    print(find_min_num_in_rotate_array(lst2))
    print(minNumberInRotateArray(lst2))
    print(min_num(lst2))
