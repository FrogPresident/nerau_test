import pygame


class Drawable:

    def __init__(self):
        self.children = []
        self.parent = None

    def draw(self, screen):
        raise NotImplementedError()

    def get_parent(self):
        return self.parent

    def set_parents(self, d):
        self.parent = d

    def add(self, d):
        if d in self.children:
            return
        d.kill()
        self.children.append(d)
        d.set_parents(self)

    def remove(self, d):
        self.children.remove(d)

    def kill(self):
        if self.parent is not None:
            self.parent.remove(self)
