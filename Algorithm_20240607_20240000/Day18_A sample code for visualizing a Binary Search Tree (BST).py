import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

def build_graph(G, node, pos={}, x=0, y=0, layer=1):
    if node is not None:
        pos[node.val] = (x, y)
        if node.left:
            G.add_edge(node.val, node.left.val)
            build_graph(G, node.left, pos, x - 1 / layer, y - 1, layer + 1)
        if node.right:
            G.add_edge(node.val, node.right.val)
            build_graph(G, node.right, pos, x + 1 / layer, y - 1, layer + 1)

def visualize_bst(root):
    G = nx.Graph()
    pos = {}
    build_graph(G, root, pos)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=16, font_weight='bold')
    plt.show()

# 테스트용 데이터
nums = [-10, -3, 0, 5, 9]
bst_root = sorted_array_to_bst(nums)
visualize_bst(bst_root)
