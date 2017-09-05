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
#	sound.seek(self.inputlabel1)	
	def update(self,dt):
		soundG = ''
		soundC = ''
		soundD = ''
		if self.inputlabel1 == 0:
			soundG = 'g1.wav'
		elif self.inputlabel1 == 1:
			soundG = 'gis1.wav'	
		elif self.inputlabel1 == 2:
			soundG = 'a1.wav'
		elif self.inputlabel1 == 3:
			soundG = 'ais1.wav'
		elif self.inputlabel1 == 4:
			soundG = 'b1.wav'
		elif self.inputlabel1 == 5:
			soundG = 'c2.wav'
		elif self.inputlabel1 == 6:
			soundG = 'cis2.wav'
		elif self.inputlabel1 == 7:
			soundG = 'd2.wav'
		elif self.inputlabel1 == 8:
			soundG = 'dis2.wav'
		elif self.inputlabel1 == 9:
			soundG = 'e2.wav'
		elif self.inputlabel1 == 10:
			soundG = 'f2.wav'
		elif self.inputlabel1 == 11:
			soundG = 'fis2.wav'
		elif self.inputlabel1 == 12:
			soundG = 'g2.wav'

		if self.inputlabel2 == 0:
			soundC = 'c2.wav'
		elif self.inputlabel2 == 1:
			soundC = 'cis2.wav'
		elif self.inputlabel2 == 2:
			soundC = 'd2.wav'
		elif self.inputlabel2 == 3:
			soundC = 'dis2.wav'
		elif self.inputlabel2 == 4:
			soundC = 'e2.wav'
		elif self.inputlabel2 == 5:
			soundC = 'f2.wav'
		elif self.inputlabel2 == 6:
			soundC = 'fis2.wav'
		elif self.inputlabel2 == 7:
			soundC = 'g2.wav'
		elif self.inputlabel2 == 8:
			soundC = 'gis2.wav'
		elif self.inputlabel2 == 9:
			soundC = 'a2.wav'
		elif self.inputlabel2 == 10:
			soundC = 'ais2.wav'
		elif self.inputlabel2 == 11:
			soundC = 'b2.wav'
		elif self.inputlabel2 == 12:
			soundC = 'c3.wav'

		if self.inputlabel3 == 0:
			soundD = 'd2.wav'
		elif self.inputlabel3 == 1:
			soundD = 'dis2.wav'
		elif self.inputlabel3 == 2:
			soundD = 'e2.wav'
		elif self.inputlabel3 == 3:
			soundD = 'f2.wav'
		elif self.inputlabel3 == 4:
			soundD = 'fis2.wav'
		elif self.inputlabel3 == 5:
			soundD = 'g2.wav'
		elif self.inputlabel3 == 6:
			soundD = 'gis2.wav'
		elif self.inputlabel3 == 7:
			soundD = 'a2.wav'
		elif self.inputlabel3 == 8:
			soundD = 'ais2.wav'
		elif self.inputlabel3 == 9:
			soundD = 'b2.wav'
		elif self.inputlabel3 == 10:
			soundD = 'c3.wav'
		elif self.inputlabel3 == 11:
			soundD = 'cis3.wav'
		elif self.inputlabel3 == 12:
			soundD = 'd3.wav'
	
		stringG = SoundLoader.load('%s' % soundG)
		stringG.play()
		stringC = SoundLoader.load('%s' % soundC)
		stringC.play()
		stringD = SoundLoader.load('%s' % soundD)
		stringD.play()
		
class PongApp(App):
	def build(self):
		game = PongGame()
		Clock.schedule_interval(game.update, 0.1)
		return game

if __name__ == '__main__':
	PongApp().run()
