import math

class Node:
    def __init__(self, val: int, cumul_p: float) -> None:
        self.val = val
        self.cumul_p = cumul_p
        self.win = None
        self.loss = None

    def esperance(self) -> float:
        # not sure, messemble y'avait un LN
        return self.val * self.cumul_p

    def __repr__(self) -> str:
        return f"({self.val}; {self.cumul_p})"


class TreeMaker:
    def __init__(self, win_val: int, loss_val: int, win_p: float) -> None:
        self.win_val = win_val
        self.loss_val = loss_val
        self.win_p = win_p
        self.loss_p = 1 - win_p

    def make(self, n: int) -> Node:
        root = Node(0, 1)
        self._create_next_node(root, n)

        return root

    def _create_next_node(self, node: Node, n: int) -> None:
        if n == 0:
            return

        node.win = Node(node.val + self.win_val, self.win_p * node.cumul_p)
        node.loss = Node(node.val - self.loss_val, self.loss_p * node.cumul_p)

        self._create_next_node(node.win, n - 1)
        self._create_next_node(node.loss, n - 1)


tree_maker = TreeMaker(200, 50, 0.3)
root = tree_maker.make(18)

def x(l, n):
    if n.win is None:
        if n.val < 0:
            l.append((-1.5 * math.log(-1 * n.val))* n.cumul_p)
        else:
            l.append((math.log(n.val) * n.cumul_p))
        #l.append([n.val, n.cumul_p])
        return
    x(l, n.win)
    x(l, n.loss)

a = []
x(a, root)
print(a)
print(sum(a))
