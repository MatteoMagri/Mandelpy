from math import log, e, sqrt
from PIL import Image
from numpy import linspace
from time import time


class MandelbrotSet():

# coordinate for the center
    coordinatex = -0.7
    coordinatey = 0.0

# number of points 
    xpoints = 124
    ypoints = 93

# radius value for the picture
    radius = 1.8

# radius projection
    radiusx = radius*xpoints/sqrt(xpoints**2+ypoints**2)
    radiusy = radius*ypoints/sqrt(xpoints**2+ypoints**2)


# image name
    name = "Mandelbrot_"+str(int(time()))[-4:-1]

# data image
    data = []

# mandelbrot data
    mandelbrot_data = []

# typography
    unit = [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 248, 255, 255, 253, 253, 255, 255, 253, 255, 253, 251, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 254, 249, 255, 255, 250, 250, 255, 255, 255, 253, 253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 252, 255, 255, 255, 249, 255, 254, 251, 255, 254, 249, 251, 255, 253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 251, 251, 253, 227, 93, 96, 99, 96, 104, 101, 102, 167, 250, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 250, 255, 255, 254, 255, 237, 7, 0, 3, 0, 0, 0, 0, 122, 249, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 252, 255, 253, 253, 255, 24, 0, 0, 0, 2, 3, 0, 168, 255, 254, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 254, 250, 255, 251, 253, 254, 56, 0, 1, 0, 2, 0, 3, 207, 255, 249, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 250, 255, 255, 250, 255, 250, 78, 0, 0, 0, 2, 0, 9, 235, 251, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 253, 255, 254, 251, 255, 250, 255, 251, 255, 255, 250, 251, 255, 109, 2, 2, 0, 0, 0, 22, 255, 251, 255, 255, 255, 255, 255, 253, 252, 255, 251, 255, 255, 255], [255, 253, 255, 255, 254, 255, 255, 255, 255, 245, 250, 255, 254, 253, 151, 0, 0, 0, 6, 2, 35, 255, 255, 255, 255, 249, 255, 255, 255, 255, 251, 255, 255, 255, 255], [252, 255, 255, 254, 215, 224, 255, 253, 249, 255, 255, 252, 255, 255, 177, 0, 3, 5, 0, 0, 64, 255, 249, 255, 254, 254, 255, 250, 252, 251, 205, 254, 255, 255, 255], [255, 251, 255, 254, 72, 12, 100, 198, 255, 253, 255, 253, 253, 255, 208, 7, 0, 2, 0, 2, 93, 255, 254, 255, 254, 250, 254, 213, 136, 35, 6, 234, 255, 255, 255], [253, 254, 253, 255, 41, 0, 0, 0, 52, 140, 225, 255, 255, 255, 237, 0, 11, 0, 0, 3, 134, 251, 255, 249, 252, 173, 79, 5, 0, 0, 0, 221, 255, 255, 255], [255, 255, 255, 238, 6, 1, 4, 0, 0, 3, 1, 82, 179, 242, 255, 44, 0, 0, 0, 0, 200, 255, 195, 107, 13, 0, 2, 0, 0, 2, 5, 180, 255, 255, 255], [255, 254, 255, 207, 0, 1, 0, 0, 0, 3, 0, 2, 0, 40, 121, 34, 0, 0, 2, 7, 112, 65, 6, 0, 4, 0, 3, 6, 2, 0, 0, 123, 255, 255, 255], [254, 254, 255, 175, 0, 1, 0, 0, 0, 4, 1, 0, 5, 0, 0, 2, 2, 1, 0, 0, 1, 1, 0, 0, 0, 3, 0, 0, 2, 4, 0, 83, 255, 255, 255], [255, 251, 255, 97, 2, 3, 2, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0, 1, 0, 0, 2, 3, 0, 0, 0, 0, 4, 3, 0, 0, 2, 246, 254, 255], [255, 255, 247, 91, 0, 0, 7, 0, 2, 3, 0, 0, 0, 0, 1, 2, 0, 0, 6, 1, 0, 2, 0, 2, 0, 5, 0, 0, 0, 2, 1, 12, 240, 248, 254], [255, 251, 255, 243, 238, 231, 220, 202, 187, 171, 161, 141, 126, 138, 15, 0, 3, 0, 0, 0, 0, 96, 143, 130, 147, 168, 189, 191, 216, 222, 236, 245, 247, 252, 255], [255, 255, 255, 255, 255, 252, 253, 255, 251, 255, 251, 255, 255, 230, 13, 0, 0, 5, 0, 7, 0, 107, 247, 255, 255, 246, 252, 255, 250, 255, 251, 255, 255, 255, 255], [255, 255, 255, 251, 254, 255, 253, 252, 255, 255, 255, 255, 202, 0, 3, 0, 0, 1, 0, 2, 3, 5, 92, 255, 254, 255, 255, 254, 255, 254, 255, 250, 255, 255, 254], [255, 249, 255, 255, 255, 253, 247, 255, 253, 255, 250, 204, 0, 9, 3, 0, 5, 83, 19, 0, 0, 0, 0, 96, 255, 247, 253, 253, 251, 255, 254, 254, 253, 254, 255], [255, 255, 255, 251, 254, 255, 255, 254, 255, 254, 200, 0, 6, 0, 0, 6, 7, 255, 154, 0, 5, 3, 0, 1, 86, 255, 255, 255, 251, 254, 255, 255, 255, 255, 255], [253, 255, 255, 253, 255, 252, 255, 252, 254, 197, 0, 9, 0, 0, 6, 0, 160, 255, 254, 1, 1, 0, 1, 0, 1, 93, 251, 252, 255, 255, 252, 255, 255, 255, 255], [255, 255, 255, 255, 252, 253, 255, 251, 214, 3, 0, 2, 0, 0, 3, 17, 255, 252, 255, 154, 0, 3, 0, 1, 0, 0, 104, 255, 253, 253, 255, 253, 255, 255, 255], [255, 253, 252, 253, 255, 253, 253, 218, 5, 0, 1, 5, 0, 9, 0, 182, 250, 254, 254, 251, 26, 2, 1, 0, 2, 1, 0, 112, 255, 249, 255, 255, 255, 255, 255], [253, 251, 255, 255, 247, 254, 187, 5, 0, 3, 4, 0, 1, 0, 35, 255, 255, 255, 255, 255, 178, 0, 5, 0, 0, 2, 3, 0, 109, 246, 253, 253, 255, 255, 255], [255, 254, 252, 252, 255, 252, 40, 0, 0, 5, 0, 2, 1, 8, 191, 255, 250, 255, 246, 255, 255, 43, 0, 3, 0, 0, 0, 0, 0, 165, 255, 250, 255, 255, 255], [245, 255, 255, 252, 255, 252, 217, 83, 0, 0, 1, 0, 0, 53, 255, 255, 255, 255, 255, 255, 252, 212, 2, 0, 10, 0, 6, 5, 130, 242, 255, 254, 255, 255, 255], [255, 252, 255, 254, 250, 255, 255, 255, 141, 4, 0, 6, 4, 199, 253, 255, 255, 244, 255, 255, 255, 251, 66, 0, 1, 0, 30, 192, 255, 255, 249, 255, 255, 255, 255], [255, 255, 247, 255, 255, 247, 255, 251, 254, 191, 13, 1, 68, 254, 255, 252, 253, 255, 247, 255, 254, 253, 224, 0, 0, 99, 244, 255, 247, 253, 254, 255, 255, 255, 255], [254, 255, 255, 254, 251, 255, 253, 255, 253, 255, 242, 75, 184, 255, 251, 255, 255, 253, 255, 254, 255, 255, 247, 99, 121, 252, 253, 250, 255, 255, 255, 254, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]

# workfolw options:
    off = False
    on = True

# define if the point is or not in the Mandelbrot Set
    def mandelbrot(self,z , c , n = 180):
        if abs(z) > 2:
            return 1
        elif n > 0:
            return self.mandelbrot(z ** 2 + c, c, n - 1) 
        else:
            return 0

# create the image data
    def image_data(self, workflow = off):
        yaxis = list(linspace(self.coordinatey+self.radiusy,self.coordinatey-self.radiusy,self.ypoints))        
        if workflow == True:
            print ("Building the Mandelbrot Set ...")
        for i in yaxis:
            if workflow == True:                
                print (str(int(10000*yaxis.index(i)/len(yaxis))/100.0)+"%")
            l = []
            xaxis = linspace(self.coordinatex-self.radiusx,self.coordinatex+self.radiusx,self.xpoints)
            for j in xaxis:
                l.append(self.mandelbrot(0,complex(j,i)))
            self.mandelbrot_data.append(l)
        if workflow == True:
            print ("100.00%") 


# save the image 
    def image_save(self, workflow = off):
        if workflow == True:
            print ("Saving the image ...")
        img = Image.new("L", (self.xpoints*len(self.unit[0]),self.ypoints*len(self.unit)), "white")
        img.putdata(self.data)
        img.save(self.name+".png")

# map the typography to the mandelbrot
    def map(self, workflow = off):
        if workflow == True:
            print ("Mapping the Mandelbrot Set image ...")
        for k in self.mandelbrot_data:
            for i in self.unit:
                for j in k:
                    if j == 0:
                        self.data += i
                    else:
                        self.data += [255]*len(self.unit[0])

# generate automaticly the image
    def image(self, workflow = off):
        self.image_data(workflow)
        self.map(workflow)
        self.image_save(workflow)

# set zoom radius
    def zoom(self, n = -0.5):
        self.radius = e**(-n)
        self.radiusx = self.radius*self.xpoints/sqrt(self.ypoints**2+self.xpoints**2)
        self.radiusy = self.radius*self.ypoints/sqrt(self.xpoints**2+self.ypoints**2)

# set coordinates
    def coordinates(self, l = (-1.75,0)):
        self.coordinatex = l[0]
        self.coordinatey = l[1]

# set image size:
    def size(self, l = (120,90)):
        self.xpoints = l[0]
        self.ypoints = l[1]

# set typography
    def typo(self, path):

        self.unit = path

# set name
    def set_name(self,img_name = "Mandelbrot_"+str(int(time()))[-4:-1]):
        self.name = img_name


