# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        """使用递归实现，思路：找出左右字串，分别递归返回"""
        if s is None or s == '':
            return None
        
        int_index = 0  # 记录前缀整数的索引
        while int_index < len(s) and s[int_index] != '(':
            int_index += 1 
        
        val = int(s[:int_index])
        root = TreeNode(val) # 获取整数，创建结点

        if len(s) == int_index:   # 只有一个整数，没有子节点时直接返回。
            return root
        
        # 通过栈的压入推出，找出左右子串
        stack = []
        mid_index = 0 # 左右子串分隔的右括号(')')索引
        for i in range(int_index, len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()     
                
                if len(stack) == 0:
                    mid_index = i
                    break
        
        left_str = s[int_index + 1:mid_index] # 注意：要去掉括号
        if mid_index + 1 == len(s):
            right_str = ""
        else:
            right_str = s[mid_index + 1 + 1 : -1]
            
        root.left = self.str2tree(left_str)
        root.right = self.str2tree(right_str)
        
        return root
            
            
            
