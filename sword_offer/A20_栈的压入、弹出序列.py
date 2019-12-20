"""
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


def stack_push_pop(push_list, pop_list):
    stack = []
    while pop_list:
        # 如果第一个元素相同，可以直接弹出
        if push_list and push_list[0] == pop_list[0]:
            push_list.pop(0)
            pop_list.pop(0)
        # 如果堆栈栈顶元素和弹出列表第一个元素相同，可以同时弹出
        elif stack and stack[-1] == pop_list[0]:
            stack.pop()
            pop_list.pop(0)
        elif push_list:
            stack.append(push_list.pop(0))
        else:
            return False
    return True


"""
【思路】借用一个辅助的栈，遍历压栈顺序，先将第一个放入栈中，这里是1，然后判断栈顶元素是不是出栈顺序的第一个元素，这里是4，很显然1≠4，所以我们继续压栈，直到相等以后开始出栈，出栈一个元素，则将出栈顺序向后移动一位，直到不相等，这样循环等压栈顺序遍历完成，如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序。

举例：

入栈1,2,3,4,5

出栈4,5,3,2,1

首先1入辅助栈，此时栈顶1≠4，继续入栈2

此时栈顶2≠4，继续入栈3

此时栈顶3≠4，继续入栈4

此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，,辅助栈里面是1,2,3

此时栈顶3≠5，继续入栈5

此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，,辅助栈里面是1,2,3

….

依次执行，最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序。
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        pop_index = 0
        for i in pushV:
            stack.append(i)
            # 栈顶元素等于当前弹出列表对应元素
            while stack and stack[-1] == popV[pop_index]:
                stack.pop()
                pop_index += 1
        return len(stack) == 0


def main(pushs, pops):
    stack = list()
    index = 0
    for i in pushs:
        stack.append(i)
        while stack and stack[-1] == pops[index]:
            index += 1
            stack.pop()
    return len(stack) == 0


class Solution2:
    def IsPopOrder(self, pushV, popV):
        stack = list()
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack:
            return False
        return True



if __name__ == '__main__':
    print(stack_push_pop([1,2,3,4,5],[4,5,3,2,1]))
    print(stack_push_pop([1,2,3,4,5],[4,3,5,1,2]))
