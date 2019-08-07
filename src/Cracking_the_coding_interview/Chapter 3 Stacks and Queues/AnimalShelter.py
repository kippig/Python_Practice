from Queue import Queue


class AnimalShelter:

    def __init__(self, types=None):
        self.types = {x for x in types}
        self.type_stacks = dict()
        self.main_q = Queue()

    def new_type(self, type):
        self.types.add(type)
        self.type_stacks[type] = Queue()

    def del_type(self, type):
        self.types.remove(type)
        # go through the main queue and remove all elements of this type

    def enqueue(self, item):
        "item is a tuple (name, type)"
        self.main_q

    def dequeue_any(self):
        pass

    def dequeue_type(self, type):
        if type not in self.types:
            raise Exception("Invalid type please enter one of: {}".format(self.types))

