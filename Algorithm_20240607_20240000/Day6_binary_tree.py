"""

    6일차: 트리 (기본적인 개념)
    트리는 중요한 자료구조 중 하나로, 특히 계층적 데이터를 다루는 데 유용합니다. 6일차에는 트리의 기본 개념을 배우고, 이진 트리의 구현과 기초적인 트리 순회 방법을 익힙니다. 

    학습목표 
        - 트리의 기존 개념 이해 
        - 이진 트리의 구조와 구현
        - 트리 순회 방법 (전위, 중위, 후위 순회)

    6일차 학습 내용 

    1. 트리의 기본 개념 
        - 트리의 정의 : 노드와 간선으로 구성된 계층적 자료구조. 루트 노드부터 시작해 자식 노드로 뻗어 나가는 구조. 
        - 트리의 용어 : 
            - 루트(Root) : 트리의 시작 노드 
            - 노드(Node) : 데이터를 저장하는 기본 단위 
            - 간선(Edge) : 노드 간의 연결을 나타내는 선 
            - 리프(Leaf) : 자식 노드가 없는 노드 
            - 부모(Parent)와 자식(Child) : 노드 간의 관계 
    2. 이진 트리의 구조와 구현 
        - 이진 트리 (Binary Tree) : 각 노드가 최대 두 개의 자식 노드를  가지는 트리 
        - 이진 트리의 구현 : 
            - 노드 클래스와 트리 클래스 정의
            - 이진 트리으 ㅣ사입과 탐색 메서드 구현 
    3. 트리 순회의 종류 : 
        - 전위 순회 (Preorder Traversal) 
        - 중위 순회 (Inorder Traversal)
        - 후위 순회 (Postorder Traversal)
                
"""

# 예제 코드 

class TreeNode: 
    def __init__(self, key):
        self.left = None 
        self.right = None
        self.value = key 

class BinaryTree: 
    def __init__(self):
        self.root = None 

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else: 
                self._insert(root.right, key)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left) 
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node: 
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# 예제 사용 
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)
bt.insert(12)
bt.insert(20)

print("Preorder traversal: ")
bt.preorder_traversal(bt.root) # 출력: 10 5 2 7 15 12 20

print("\nInorder traversal: ")
bt.inorder_traversal(bt.root) # 출력: 2 5 7 10 12 15 20

print("\nPostorder traversal: ")
bt.postorder_traversal(bt.root) # 출력: 2 7 5 12 20 15 10


# 그림 그리면 이해 쉬움. 
