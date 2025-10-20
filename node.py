class Node:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration
        self.next = None
        self.prev = None
