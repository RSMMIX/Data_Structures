from unittest.mock import NonCallableMagicMock


def insert(self,data):
    if self.root == None:
        self.root = Node(data)
    else:
        cur = self.root
        while True:
            if data < cur.data:
                if cur.left == None:
                    cur.left = Node(data)
                    break
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = Node(data)
                    break
                else:
                    cur = cur.right
    return self.root