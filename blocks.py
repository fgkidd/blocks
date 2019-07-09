import play


class block():
    def __init__(self,x,y,width,height):
        self.object = play.new_box(color='red',x=x,y=y,width=width,height=height)
        self.object.start_physics(can_move=True,stable=False,x_speed=0,y_speed=0)
        self.x=self.object.x
        self.y=self.object.y
        self.force=[0,0]

