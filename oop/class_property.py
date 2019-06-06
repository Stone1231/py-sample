import math


class Ball:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def volumn(self):
        return 4.0 / 3.0 * math.pi * self.__radius ** 3
    
    @volumn.setter
    def volumn(self, volumn):
        if volumn <= 0:
            raise ValueError('必須是正數')
        self.__radius = ((3.0 * volumn) / (4.0 * math.pi)) ** (1.0 / 3.0)
        
ball = Ball(10.0)
print(ball.volumn)
ball.volumn = 5000
print(ball.radius)