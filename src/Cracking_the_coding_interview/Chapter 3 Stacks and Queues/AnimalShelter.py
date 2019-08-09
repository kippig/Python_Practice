from Queue import Queue
from datetime import datetime


class AnimalShelter:
    """
    Space: O(n*K) where K is categories and n is maximum number in any category
    """

    def __init__(self, categories=None):
        self.types = {x for x in categories}
        self.type_queues = dict()

    def new_type(self, category):
        self.types.add(category)
        self.type_queues[category] = Queue()

    def del_type(self, category):
        if self.type_queues.get(category) is not None:
            self.types.remove(category)
            del self.type_queues[category]

    def enqueue(self, item, category):
        """Time: O(1)"""
        if self.type_queues.get(category) is None:
            self.new_type(category)
        self.type_queues[category].add((item, datetime.now()))

    def dequeue_any(self):
        """Time: O(k), we could do O(1) with a hash O(k) if the category number gets large"""
        oldest = datetime.now()
        for category in self.types:
            val = self.type_queues[category].peek()
            if val is not None and val[1] < oldest:
                oldest_cat = category
        return self.type_queues[oldest_cat].pop()

    def dequeue_type(self, category):
        """Time: O(1)"""
        if category not in self.types:
            raise Exception("Invalid type please enter one of: {}".format(self.types))
        return self.type_queues[category].pop()

