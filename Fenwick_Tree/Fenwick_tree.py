class Fenwick_tree:
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = [0] *n
        self.tree = [0] * (n + 1)
        for i, val in enumerate(nums):
            self.update(i, val)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) ->int:
        s = 0
        while i > 0:
            s += self.tree[i]
            # 注意位运算的 加括号
            i = i - (i & -i) 
        return s
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right + 1) - self.prefix_sum(left)
