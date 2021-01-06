from .house import House
from .battery import Battery

class Graph():
    def __init__(self, source):
        self.graph = load_houses