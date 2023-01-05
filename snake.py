class Snake:

    def __init__(self, length, x, y, map_size):
        self.length = length
        self.x = x
        self.y = y
        self.map_size = map_size
        self.body = [(x, y)]
        self.tail = None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_body(self):
        return self.body

    def eat(self):
        self.length += 1
        self.body = self.body + [self.tail]

    #https://www.pygame.org/docs/tut/MoveIt.html#screen-coordinates

    #place a part of the body at the front
    #get rid of the end tail - uncolour it
    def move_up(self):
        self.y -= 1
        self.body = [(self.x, self.y)] + self.body
        self.tail = self.body.pop()
        return self.tail

    def move_down(self):
        self.y += 1
        self.body = [(self.x, self.y)] + self.body
        self.tail = self.body.pop()
        return self.tail

    def move_right(self):
        self.x += 1
        self.body = [(self.x, self.y)] + self.body
        self.tail = self.body.pop()
        return self.tail

    def move_left(self):
        self.x -= 1
        self.body = [(self.x, self.y)] + self.body
        self.tail = self.body.pop()
        return self.tail

    def is_alive(self):
      #x goes from 0-mapsize and y goes from 0-mapsize
        if (self.x < 0) or (self.x > self.map_size):
            return False
        if (self.y < 0) or (self.y > self.map_size):
            return False

        #check if snake is eating itself
        #iterate through the whole body - which is just a bunch of lists
        for body in self.body[1:]:
            if (body[0] == self.x) and (body[1] == self.y):
                return False

        return True
