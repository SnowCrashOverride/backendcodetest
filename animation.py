import math

init = input("What is the initial state? ")
speed = int(input("What is the speed? "))

#Class object for building the chamber
class Animation(object):
    def __init__(self, chamber):
        self.chamber = []
        self.particles = []
        self.len_chamber = len(chamber)

        #Loop to make an empty chamber
        for i in range(len(chamber)):
            self.chamber.append(['.'])
            if chamber[i] is not '.':
                self.particles.append(Particle(chamber[i],i,self.len_chamber))

    def animate(self, speed):
        for particle in self.particles:
            particle.move_particle(speed)
        animation.build_chamber()

    def build_chamber(self):
        temp_chamber = []
        temp_index = '.'
        result = ''

        # building temp chamber
        for i in range(len(self.chamber)):
            temp_chamber.append(['.'])

        for particle in self.particles:
            if particle.exists:
                temp_chamber[particle.position].append(particle)

        # print(temp_chamber)
        for i in range(len(temp_chamber)):
            for j in range(len(temp_chamber[i])):
                if type(temp_chamber[i][j]) is Particle:
                    temp_index = 'X'
                else:
                    temp_index = '.'
            result += temp_index
        print(result)
        return(result)

#Class object for building the particle
class Particle(object):
    def __init__(self, direction, position, len_chamber):
        # map attributes
        self.direction = direction
        self.position = position
        self.len_chamber = len_chamber
        self.exists = True

    def move_particle(self,speed):
        if self.direction == 'R':
            self.position = self.position + speed
            if self.position > self.len_chamber - 1:
                self.exists = False
        else:
            self.position = self.position - speed
            if self.position < 0:
                self.exists = False

animation = Animation(init)
animation.build_chamber()

if init.find('R') == -1:
    print_range = math.ceil((len(init)-init[::-1].find('L'))/speed)
elif init[::-1].find('L') == -1:
    print_range = math.ceil((len(init)-init.find('R'))/speed)
else:
    print_range = math.ceil((len(init)-min(init.find('R'),init[::-1].find('L')))/speed)
    
for i in range(print_range):
    animation.animate(speed)