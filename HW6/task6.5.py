class Stationery:
    def __init__(self, title):
        self.st_title = title

    def draw(self):
        print("start rendering")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("start rendering: Thin")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("start rendering: Bold")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("start rendering: Bold font")


stationary = Stationery(title="felt-tip pen")
stationary.draw()

pen = Pen(title="white pen")
pen.draw()

pencil = Pencil(title="pencil")
pencil.draw()

handle = Handle(title="handle")
handle.draw()
