"""

    * Chapter 9 : 고급 자료구조 - 이진 탐색 트리 및 AVL 트리 

    1. 이진 탐색 트리 (Binary Search Tree, BST)
        이진 탐색 트리는 각 노드가 최대 두 개의 자식 노드를 가지는 트리 구조입니다. 각 노드는 키(key)와 해당 키에 대한 값을 가지며, 다음과 같은 속성을 만족합니다: 
        - 왼쪽 서브트리의 모든 키는 현재 노드의 키보다 작다. 
        - 오른쪽 서브트리의 모든 키는 현재 노드의 키보다 크다. 
        - 왼쪽 및 오른쪽 서브트리도 각각 이진 탐색 트리이다. 
        
        기본 연산 
        1. 삽입 (Insert)
            - 새로운 키를 적절한 위치에 삽입하여 BST 속성을 유지합니다. 
        2. 삭제 (Delete)
            - 삭제할 노드가 자식이 없는 경우, 하나의 자식이 있는 경우, 두 개의 자식이 있는 경우에 따라 다르게 처리됩니다. 
        3. 탐색 (Search)
            - 키를 찾기 위해 루트에서부터 시작하여, 현재 노드의 키와 비교하면서 왼쪽 또는 오른쪽 서브트리로 이동합니다. 
        
        시간 복잡도 
            - 평균 : O(log n)
            - 최악 : O(n) (트리가 한쪽으로 치우친 경우)
    
            
    2. AVL 트리 (Adelson-Velsky and Landis Tree)
        AVL 트리는 이진 탐색 트리의 일종으로, 모든 노드에서 왼쪽 서브트리와 오른쪽 서브트리의 높이 차이가 최대 1이 되도록 균형을 유지합니다. 이를 통해 최악의 경우에도 로그 시간 복잡도를 보장합니다. 

        기본 연산 
        1. 삽입 (Insert)
            - 새로운 노드를 삽입한 후, 트리가 불균현해지면 회전 연산을 통해 균형을 맞춥니다.
        2. 삭제 (Delete)
            - 노드를 삭제한 후, 트리가 불균형해지면, 회전 연산을 통해 균형을 맞춥니다. 
        3. 탐색 (Search)
            - 이진 탐색 트리와 동일하게 수행됩니다. 

        회전 연산 
        - 단일 회전 (Single Rotation)
            - 왼쪽 회전 
            - 오른쪽 회전 
        - 이중 회전 (Double Rotation)
            - 왼쪽-오른쪽 회전
            - 오른쪽-왼쪽 회전 
        
        시간 복잡도 
        - 모든 연산에 대해 O(log n)를 보장합니다. 
"""

###### 예제 코드 

### 이진 탐색 트리 (BST)
class TreeNode:
    def __init__(self, key):
        self.key = key 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
        
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node 
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
        
    def delete(self, key): 
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

# ## 이진 탐색 트리 사용 예제 
# bst = BinarySearchTree()

# # 노드 사입
# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)

# # 탐색 
# search_result = bst.search(40)
# if search_result:      
#     print("Search for 40 : ", search_result.key)
# else:
#     print("Search for 40 : Not found")

# search_result = bst.search(100)
# if search_result:      
#     print("Search for 100 : ", search_result.key)
# else:
#     print("Search for 100 : Not found")

# search_result = bst.search(80)
# if search_result:      
#     print("Search for 100 : ", search_result.key)
# else:
#     print("Search for 100 : Not found")

# # 삭제 
# bst.delete(20)
# bst.delete(30)
# bst.delete(50)

# # 삭제 후 탐색 
# print("Search for 20 (after delete) : ", bst.search(20))




### AVL 트리
class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
        self.height = 1 

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else: 
            node.right = self._insert(node.right, key)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z 
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3 
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y 
    
    def _get_height(self, node):
        if not node: 
            return 0 
        return node.height
    
    def _get_balance(self, node):
        if not node: 
            return 0 
        return self._get_height(node.left) - self._get_height(node.right)
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node: 
            return node 
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key: 
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key 
            node.right = self._delete(node.right, temp.key)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0 : 
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node
    
    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node 
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    

# ## AVL 트리 사용 예제 
# avl = AVLTree()

# # 노드 삽입 
# avl.insert(50)
# avl.insert(30)
# avl.insert(20)
# avl.insert(40)
# avl.insert(70)
# avl.insert(60)
# avl.insert(80)

# # 탐색 
# search_result = avl._search(avl.root, 40)
# if search_result:
#     print("Search for 40: ", search_result.key) 
# else:
#     print("Search for 40: Not found")

# search_result = avl._search(avl.root, 100)
# if search_result:
#     print("Search for 100:", search_result.key)
# else:
#     print("Search for 100: Not found")

# # 삭제 
# avl.delete(20)
# avl.delete(30)
# avl.delete(50)

# # 삭제 후 탐색 
# search_result = avl._search(avl.root, 20)
# if search_result:
#     print("Search for 20 (after delete):", search_result.key)
# else:
#     print("Search for 20 (after delete): Not found")


## 균형 유지 테스트 예제 작성해 
avl = AVLTree()

# 노드 삽입 
nodes_to_insert = [10, 20, 30, 40, 50, 25]
for node in nodes_to_insert:
    avl.insert(node)
    print(f"Inserted {node} into the AVL tree.")

# 트리의 균형을 확인하기 위해 각 노드의 높이와 균형 인수를 출력 
def print_tree_balance(node):
    if node is not None:
        print(f"Node {node.key}: Height = {node.height}, Balance = {avl._get_balance(node)}")
        print_tree_balance(node.left)
        print_tree_balance(node.right)

print("\nAVL Tree Balance After Insertions:")
print_tree_balance(avl.root)

# 특정 노드를 삭제하고 균형을 확인 
nodes_to_delete = [10, 20]
for node in nodes_to_delete: 
    avl.delete(node)
    print(f"\nDeleted {node} from the AVL tree.")
    print("AVL Tree Balance After Delete:")
    print_tree_balance(avl.root)

# 예제 설명 
"""
    1. 노드 삽입 : [10,20,30,40,50,25]의 순서로 노드를 삽입한다. AVL 트리는 삽입 후 자동으로 균형을 유지한다.   
    2. 트리의 균형 확안 : 삽입 후 각 노드의 높이(Height)와 균형 인수(Balance)를 출력하여 AVL 트리가 잘 균형을 유지하고 있는지 확인한다.
    3. 노드 삭제 및 균형 확인 : 특정 노드 [10, 20]를 삭제하고, 삭제 후 AVL 트리가 여전히 균형을 유지하는지 확인한다. 

    이 예제를 통해 AVL 트리의 균형 유지 능력을 테스트할 수 있다. 트리에 노드를 삽입하고 삭제하는 동안 트리가 자동으로 균형을 유지하는 과정을 시각적으로 확인할 수 있다.  
"""






