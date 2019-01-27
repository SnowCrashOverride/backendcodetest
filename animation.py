#Import math to use math.ceil to round numbers up to whole number in final loop 
import math

init = input("What is the initial state? ")
speed = int(input("What is the speed? "))

#Class object for building the room
class Animation(object):
    #Function defines initial state of room
    def __init__(self, room):
        self.room = []
        self.particles = []
        self.len_room = len(room)      
        for i in range(len(room)):
            self.room.append(['.'])
            if room[i] is not '.':
                self.particles.append(Particle(room[i],i,self.len_room))
    #Function to build room as particle moves through it
    def animate(self, speed):
        for particle in self.particles:
            particle.move_particle(speed)
        animation.build_room()
    #Function to build a temporary room of '.''s, repaced by 'X''s if a particles occupies a space
    def build_room(self):
        temp_room = []
        temp_index = '.'
        result = ''
        #Build temporary room
        for i in range(len(self.room)):
            temp_room.append(['.'])

        for particle in self.particles:
            if particle.exists:
                temp_room[particle.position].append(particle)

        #Print temporary room
        for i in range(len(temp_room)):
            for j in range(len(temp_room[i])):
                if type(temp_room[i][j]) is Particle:
                    temp_index = 'X'
                else:
                    temp_index = '.'
            result += temp_index
        print(result)
        return(result)

#Class object for building the particle
class Particle(object):
    def __init__(self, direction, position, len_room):
        #Map attributes
        self.direction = direction
        self.position = position
        self.len_room = len_room
        self.exists = True
    #Function for moving the particle, dependent on initial position and speed
    def move_particle(self,speed):
        if self.direction == 'R':
            self.position = self.position + speed
            if self.position > self.len_room - 1:
                self.exists = False
        else:
            self.position = self.position - speed
            if self.position < 0:
                self.exists = False

#Apply function to display initial state
animation = Animation(init)
animation.build_room()
#Loop through init as particle moves to print function needed number of times
if init.find('R') == -1:
    print_range = math.ceil((len(init)-init[::-1].find('L'))/speed)
elif init[::-1].find('L') == -1:
    print_range = math.ceil((len(init)-init.find('R'))/speed)
else:
    print_range = math.ceil((len(init)-min(init.find('R'),init[::-1].find('L')))/speed)
#For every needed space in the initail state, animation is called    
for i in range(print_range):
    animation.animate(speed)