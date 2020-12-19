"""
My little Queue
"""
from typing import Any

_queue = []
def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    _queue.append(elem)



def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if len(_queue):
        return _queue.pop(0)



def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if 0 <= ind < len(_queue):
        return _queue[ind]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global _queue
    _queue = []
    return None
