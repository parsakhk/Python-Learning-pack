from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
class Vovel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y = 0.5,
            texture= 'white_cube',
            color= color.white,
            highlight_color = color.lime,
        )
    def Input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                vovel = Vovel(position= self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
app = Ursina()
for z in range(8):
    for x in range(8):
        vovel = Vovel(position=  (x,0,z))
player = FirstPersonController()
app.run()