
from typing import Any, Iterator, Optional
from collections import deque


Tree = Optional[list[Any]]

t: Tree = \
    ['A',
     ['B',
      ['D', None, None],
      None],
     ['C',
      None,
      ['E',
       ['F', None, None],
       ['G', None, None]]]]


def in_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield from in_order(left)
        yield value
        yield from in_order(right)


def pre_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield value
        yield from pre_order(left)
        yield from pre_order(right)


def post_order(root: Tree) -> Iterator[str]:
    if root:
        value, left, right = root
        yield from post_order(left)
        yield from post_order(right)
        yield value


def level_order(root: Tree) -> Iterator[str]:
    queue: deque[Tree] = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current:
            value, left, right = current
            queue.append(left)
            queue.append(right)
            yield value


if __name__ == '__main__':
    # g = in_order(t)
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # for x in in_order(t):
    #     print(f'{x = }')
    print(f'{list(in_order(t)) = }')
    print(f'{list(pre_order(t)) = }')
    print(f'{list(post_order(t)) = }')
    print(f'{list(level_order(t)) = }')
