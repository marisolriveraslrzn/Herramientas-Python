class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def toggle(self):
        self.done = not self.done
