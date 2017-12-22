import os
from random import randint
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.screenmanager import ScreenManager
from kivy.uix.slider import Slider
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

class PongGame(FloatLayout):
#	sound 'test.wav')
	past=[0,0,0]
	inputlabel1 = NumericProperty(0)
	inputlabel2 = NumericProperty(0)
	inputlabel3 = NumericProperty(0)

	Gvar0 = SoundLoader.load('g1.wav')
	Gvar1 = SoundLoader.load('gis1.wav'	)
	Gvar2 = SoundLoader.load('a1.wav')
	Gvar3 = SoundLoader.load('ais1.wav')
	Gvar4 = SoundLoader.load('b1.wav')
	Gvar5 = SoundLoader.load('c2.wav')
	Gvar6 = SoundLoader.load('cis2.wav')
	Gvar7 = SoundLoader.load('d2.wav')
	Gvar8 = SoundLoader.load('dis2.wav')
	Gvar9 = SoundLoader.load('e2.wav')
	Gvar10 = SoundLoader.load('f2.wav')
	Gvar11 = SoundLoader.load('fis2.wav')
	Gvar12 = SoundLoader.load('g2.wav')
	#Gvar12 = Gvar0
	#Gvar12.pitch=2	
	
	Cvar0 = SoundLoader.load( 'c2.wav')
	Cvar1 = SoundLoader.load(  'cis2.wav')
	Cvar2 = SoundLoader.load(  'd2.wav')
	Cvar3 = SoundLoader.load(  'dis2.wav')
	Cvar4 = SoundLoader.load(  'e2.wav')
	Cvar5 = SoundLoader.load(  'f2.wav')
	Cvar6 = SoundLoader.load(  'fis2.wav')
	Cvar7 = SoundLoader.load(  'g2.wav')
	Cvar8 = SoundLoader.load(  'gis2.wav')
	Cvar9 = SoundLoader.load(  'a2.wav')
	Cvar10 = SoundLoader.load(  'ais2.wav')
	Cvar11 = SoundLoader.load(  'b2.wav')
	Cvar12 = SoundLoader.load(  'c3.wav')

	Dvar0 = SoundLoader.load('d2.wav')
	Dvar1 = SoundLoader.load('dis2.wav')
	Dvar2 = SoundLoader.load('e2.wav')
	Dvar3 = SoundLoader.load('f2.wav')
	Dvar4 = SoundLoader.load('fis2.wav')
	Dvar5 = SoundLoader.load('g2.wav')
	Dvar6 = SoundLoader.load('gis2.wav')
	Dvar7 = SoundLoader.load('a2.wav')
	Dvar8 = SoundLoader.load('ais2.wav')
	Dvar9 = SoundLoader.load('b2.wav')
	Dvar10 = SoundLoader.load('c3.wav')
	Dvar11 = SoundLoader.load('cis3.wav')
	Dvar12 = SoundLoader.load('d3.wav')

	for i in range(0,13):
		exec('Gvar%s.loop=True'%(str(i)))
		exec('Cvar%s.loop=True'%(str(i)))
		exec('Dvar%s.loop=True'%(str(i)))
	Gvar0.play()
	Cvar0.play()
	Dvar0.play()
#	sound.seek(self.inputlabel1)	
	def update(self,dt):
		if self.inputlabel1 != self.past[0]:
			exec('self.Gvar%s.stop()'%(str(self.past[0])))
			#for i in range(0,13):
			#	if int(i)!=int(self.inputlabel1):
			#		exec('try:self.Gvar%s.stop()\nexcept:pass'%(str(i)))
			exec('self.Gvar%s.play()'%(str(int(self.inputlabel1))))
		if self.inputlabel2 != self.past[1]:
			exec('self.Cvar%s.stop()'%(str(self.past[0])))
			#for i in range(0,13):
			#	if int(i)!=int(self.inputlabel2):
			#		exec('try:self.Cvar%s.stop()\nexcept:pass;'%(i))
			exec('self.Cvar%s.play()'%(str(int(self.inputlabel2))))
		if self.inputlabel3 != self.past[2]:
			exec('self.Dvar%s.stop()'%(str(self.past[0])))
			#for i in range(0,13):
			#	if int(i)!=int(self.inputlabel3):
			#		exec('try:self.Dvar%s.stop()\nexcept:pass;'%(i))
			exec('self.Dvar%s.play()'%(str(int(self.inputlabel3))))
		self.past[0]=int(self.inputlabel1)
		self.past[1]=int(self.inputlabel2)
		self.past[2]=int(self.inputlabel3)

class PongApp(App):
	def build(self):
		game = PongGame()
		Clock.schedule_interval(game.update, 0.5)
		return game

if __name__ == '__main__':
	PongApp().run()
