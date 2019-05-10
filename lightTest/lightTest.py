import matplotlib.pyplot as plt
import numpy as np





class Space():
    def __init__(self):
        self.worldx = 1000
        self.worldy = 1000
        self.world = np.zeros([self.worldx,self.worldy])

        self.light_position = [400,400]
        self.beams = 100

        self.walls = [
            [[100,100],[400,200]],
            [[100,200],[500,800]],
            [[100,100],[300,700]]
        ]

        for wall in self.walls:
            self.add_wall(wall)
    

    def add_wall(self, wall):
        xdiff = wall[1][0] - wall[0][0]
        ydiff = wall[1][1] - wall[0][1]

        x = wall[0][0]
        y = wall[0][1]

        xlen = (wall[1][0] - x)
        ylen = (wall[1][1] - y)
        
        nop = xdiff + ydiff

        xinc = xlen/nop
        yinc = ylen/nop

        self.set_point(self.world, x,y)
        lastx = x
        lasty = y

        while ((x < wall[1][0]) & (y < wall[1][1])):
            x = x + xinc
            y = y + yinc
            self.set_point(self.world, x,y)
            self.set_point(self.world, x-1,y-1)
        
    def set_point(self, mapp, x,y):
        mapp[int(np.round(x-0.5)), int(np.round(y-0.5))] = 1

    def point_filled(self, mapp, x, y):
        return (mapp[int(np.round(x-0.5)), int(np.round(y-0.5))] == 1)

    def draw_frame(self):
        pass

    def draw_pixel(self):
        pass

    def draw_map(self):
        plt.imshow(self.world*255)
        plt.show()

    def draw_light(self):
        light_map = np.zeros([self.worldx,self.worldy])
        beam_angle_inc = 360/self.beams
        beam_angle = 0

        for beam in range(self.beams):
            x = self.light_position[0]
            y = self.light_position[1]

            xinc = np.sin(beam_angle)
            yinc = np.cos(beam_angle)
            

            while True:
                self.set_point(light_map, x,y)

                x = x + xinc
                y = y + yinc
                #edge of world check
                if((x >= self.worldx) 
                or (y >= self.worldy)
                or (x <= 0)
                or (y <= 0)):
                    break
                
                if self.point_filled(self.world, x, y):
                    break
                
            beam_angle = beam_angle + beam_angle_inc
        return light_map
        

space = Space()

light = space.draw_light()

plt.subplot(1,3,1)
plt.imshow(space.world*255)
plt.subplot(1,3,2)
plt.imshow(light*255)
plt.subplot(1,3,3)
new = light + (space.world*2)
plt.imshow(new)
plt.show()