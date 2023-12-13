class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1  # 子树大小
        self.depth = 0  # 节点深度
        self.parent = None  # 父节点
        self.heavy = None  # 重子节点

class HLD:
    def __init__(self, root):
        self.root = root
        self._dfs(root)
        self._decompose(root, root)

    def _dfs(self, node, depth=0, parent=None):
        if not node:
            return 0
        node.depth = depth
        node.parent = parent
        size = 1
        max_c_size = 0
        for c in [node.left, node.right]:
            if c:
                c_size = self._dfs(c, depth + 1, node)
                size += c_size
                if c_size > max_c_size:
                    max_c_size = c_size
                    node.heavy = c
        node.size = size
        return size

    def _decompose(self, node, head):
        if not node:
            return
        node.head = head
        if node.heavy:
            self._decompose(node.heavy, head)
        for c in [node.left, node.right]:
            if c and c != node.heavy:
                self._decompose(c, c)

    def lca(self, u, v):
        while u.head != v.head:
            if u.head.depth > v.head.depth:
                u = u.head.parent
            else:
                v = v.head.parent
        return u if u.depth < v.depth else v

# 使用示例
# 首先构建树并初始化树链剖分
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# ... 其他节点的添加
hld = HLD(root)

# 执行LCA查询
lca = hld.lca(node1, node2)
