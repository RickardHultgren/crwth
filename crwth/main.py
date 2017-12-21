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
		
#	sound.seek(self.inputlabel1)	
	def update(self,dt):
		soundG = ''
		soundC = ''
		soundD = ''
		if self.inputlabel1 == 0:
			self.Gvar0.play()
		elif self.inputlabel1 == 1:
			self.Gvar1.play()
		elif self.inputlabel1 == 2:
			self.Gvar2.play()
		elif self.inputlabel1 == 3:
			self.Gvar3.play()
		elif self.inputlabel1 == 4:
			self.Gvar4.play()
		elif self.inputlabel1 == 5:
			self.Gvar5.play()
		elif self.inputlabel1 == 6:
			self.Gvar6.play()
		elif self.inputlabel1 == 7:
			self.Gvar7.play()
		elif self.inputlabel1 == 8:
			self.Gvar8.play()
		elif self.inputlabel1 == 9:
			self.Gvar9.play()
		elif self.inputlabel1 == 10:
			self.Gvar10.play()
		elif self.inputlabel1 == 11:
			self.Gvar11.play()
		elif self.inputlabel1 == 12:
			self.Gvar12.play()

		if self.inputlabel2 == 0:
			self.Cvar0.play()
		elif self.inputlabel2 == 1:
			self.Cvar1.play()
		elif self.inputlabel2 == 2:
			self.Cvar2.play()
		elif self.inputlabel2 == 3:
			self.Cvar3.play()
		elif self.inputlabel2 == 4:
			self.Cvar4.play()
		elif self.inputlabel2 == 5:
			self.Cvar5.play()
		elif self.inputlabel2 == 6:
			self.Cvar6.play()
		elif self.inputlabel2 == 7:
			self.Cvar7.play()
		elif self.inputlabel2 == 8:
			self.Cvar8.play()
		elif self.inputlabel2 == 9:
			self.Cvar9.play()
		elif self.inputlabel2 == 10:
			self.Cvar10.play()
		elif self.inputlabel2 == 11:
			self.Cvar11.play()
		elif self.inputlabel2 == 12:
			self.Cvar12.play()

		if self.inputlabel3 == 0:
			self.Dvar0.play()
		elif self.inputlabel3 == 1:
			self.Dvar1.play()
		elif self.inputlabel3 == 2:
			self.Dvar2.play()
		elif self.inputlabel3 == 3:
			self.Dvar3.play()
		elif self.inputlabel3 == 4:
			self.Dvar4.play()
		elif self.inputlabel3 == 5:
			self.Dvar5.play()
		elif self.inputlabel3 == 6:
			self.Dvar6.play()
		elif self.inputlabel3 == 7:
			self.Dvar7.play()
		elif self.inputlabel3 == 8:
			self.Dvar8.play()
		elif self.inputlabel3 == 9:
			self.Dvar9.play()
		elif self.inputlabel3 == 10:
			self.Dvar10.play()
		elif self.inputlabel3 == 11:
			self.Dvar11.play()
		elif self.inputlabel3 == 12:
			self.Dvar12.play()
	
		#stringG = SoundLoader.load('%s' % soundG)
		#stringG.play()
		#stringG.stop()
		#stringC = SoundLoader.load('%s' % soundC)
		#stringC..play()
		#stringD = SoundLoader.load('%s' % soundD)
		#stringD.play()
		
class PongApp(App):
	def build(self):
		game = PongGame()
		Clock.schedule_interval(game.update, 0.1)
		return game

if __name__ == '__main__':
	PongApp().run()
