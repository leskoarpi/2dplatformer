import streamlit as st

st.code('''
from ursina import *
from random import randint
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


app = Ursina()
#jatekos inicializalasa
player = PlatformerController2d(y=1)

#kamera kovet
camera.add_script(SmoothFollow(target = player, offset=[0,0,-40], speed=15))


#mozgasi sebessegek allitasa
player.jump_height = 10
player.walk_speed = 20

#falak
ground = Entity(model="quad",y=-3, scale_x=40,collider="box",color = color.blue)
rightwall = Entity(model="quad", scale=(1,500000), x=12,y=249996.8, collider="box", color = color.blue)
leftwall = Entity(model="quad", scale=(1,500000), x=-12,y=249996.8, collider="box", color = color.blue)
bg = Entity(model="quad", texture="Assets/hatter.jpg", z=1, scale=(50,50))
duplicate(bg, y = 50)

#plathorm generáció
platform = Entity(
    model='cube',
    color=color.green,
    texture='white_cube',
    collider='box',
    scale=(3,0.5))
app.run()



''')