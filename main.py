from sphere import Sphere, Material, Light
from raytracer import Raytracer
from lib import *
ivory = Material(diffuse=color(100, 100, 80), albedo=(0.6,  0.3), spec=50)
rubber = Material(diffuse=color(80, 0, 0), albedo=(0.9,  0.1), spec=10)


r = Raytracer(500, 500)
redColor = color(255,0,0)
blueColor = color(0,0,255)
grayColor = color(68,78,97)
glass = Material(diffuse=color(150, 180, 200), albedo=(0.1, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
red = Material(diffuse=redColor, albedo=(.2,  0,0.7, 0.9), spec=115,refractive_index=2)
blue = Material(diffuse=blueColor, albedo=(.2,  0,0.7, .9), spec=115,refractive_index=2)
gray = Material(diffuse=grayColor, albedo=(0.3,  0.3,0, 0.6), spec=150)


r.light = Light(
  position=V3(-20, 0, 40),
  intensity=1
)
bg = 0
r.background_color = color(bg ,bg,bg)
reds = [Sphere(V3(-2.3 + 1.7 * i, -1, -12), 1, red) for i in range(4)]
blues = [Sphere(V3(-2.4 + 1.7 * i, -1, -12), 1, blue) for i in range(4)]
reds = [Sphere(V3(-2.3 + 1.7 * i, 1.3, -12), 1.3, red) for i in range(4)]
blues = [Sphere(V3(-2.4 + 1.7 * i, 1.3, -12), 1.3, blue) for i in range(4)]
r.scene = reds + blues
r.render()
r.write('out.bmp')