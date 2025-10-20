from node import Node

class MovieList:
    def __init__(self):
        self.head = None

    def add_movie(self, title, year, duration):
        new_node = Node(title, year, duration)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(f"Movie '{title}' added.")
            return
        

        current = self.head
        while True:
            if current.title.lower() == title.lower():
                print(f"Movie '{title}' already exists.")
                return
            current = current.next
            if current == self.head:
                break

        # Insert
        current = self.head
        while (current.next != self.head and
               current.title.lower() < title.lower()):
            current = current.next

        if current == self.head and title.lower() < current.title.lower():
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node

        elif current.next == self.head and current.title.lower() < title.lower():
            new_node.next = self.head
            new_node.prev = current
            current.next = new_node
            self.head.prev = new_node
            
        else:
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

        print(f"Movie '{title}' added.")

    #DELETE MOVIE
    def delete_movie(self, title):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while True:
            if current.title.lower() == title.lower():
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                print(f"Movie '{title}' deleted.")
                return
            current = current.next
            if current == self.head:
                break
        print(f"Movie '{title}' not found.")


    #FIND MOVIE
    def find_movie(self, title):
        if self.head is None:
            print("List is empty.")
            return None

        current = self.head
        while True:
            if current.title.lower() == title.lower():
                print(f"Found: {current.title}, Year: {current.year}, Duration: {current.duration} min")
                return current
            current = current.next
            if current == self.head:
                break
        print(f"Movie '{title}' not found.")
        return None


    def print_movies(self):
        if self.head is None:
            print("No movies in List")
            return
        print("\nMovies in List:")
        current = self.head
        while True:
            print(f"Title: {current.title}, Year: {current.year}, Duration: {current.duration} min")
            current = current.next
            if current == self.head:
                break



    def save_to_file(self, filename):
        if self.head is None:
            print("List is empty.")
            return
        with open(filename, 'w') as f:
            current = self.head
            while True:
                f.write(f"{current.title},{current.year},{current.duration}\n")
                current = current.next
                if current == self.head:
                    break
        print(f"Data saved to '{filename}'.")


    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        title, year, duration = data
                        self.add_movie(title, int(year), int(duration))
            print(f"List loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")