#import kivy
#kivy.require('1.1.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.popup import Popup

class SetNamePopup(Popup):
    pass

class MainLayout(BoxLayout):
    fullName = StringProperty('No Name')
    def setName(self,*args):
        setNamePopup().open()

class popUpApp(App):
    def build(self):
        self.title="Popups Example"
        return MainLayout()

if __name__=="__main__":
    popUpApp().run()