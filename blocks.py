import play
from numpy.linalg import norm

class block():
    def __init__(self,x,y,width,height,stiffness):
        self.object = play.new_box(color='red',x=x,y=y,width=width,height=height)
        self.object.start_physics(can_move=True,stable=False,x_speed=0,y_speed=0)
        self.x=self.object.x
        self.y=self.object.y
        self.angle=self.object.angle
        self.stiffness=stiffness
        self.connected=False

class connection():
    def __init__(self,blocks):
        self.blocks=blocks
        self.length = norm([blocks[0].x-blocks[1].x,blocks[0].y-blocks[1].y])
        self.stiffness = sum([b.stiffness for b in self.blocks])/len(self.blocks)


