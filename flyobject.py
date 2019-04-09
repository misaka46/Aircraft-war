import abc


class Flyobject(object):
    def __int__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.image = image
