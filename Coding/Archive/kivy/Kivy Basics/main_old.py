import kivy
kivy.require('1.10.1')
from kivy.deps import sdl2, glew
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory 

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

    var = ObjectProperty(None)
    var = "bonjour"

    def btn(self):
        print('hi')
        #Factory is the constructor method for popups, MyPopup() is the name of targeted popup testlabel1 is the python id referenced in the .kv file text is the attribute of the element
        print(str(Factory.MyPopup().testlabel.text))
        self.var = "test"
        print(Factory.MySecondPopup().label2.text)
        #{}'.format(FloatLayout.testlabel)

    #    var1 = self.var1.text
    #    var2 = self.var2.text
    #    var3 = self.var3.text
    #    MyPopup.open()
        pass       

if __name__ == "__main__":
    MyApp().run()