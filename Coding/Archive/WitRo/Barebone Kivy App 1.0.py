import kivy
kivy.require('1.0.6')
from kivy.app import App
from kivy.uix.label import Label

def bonjour():
    a = "bonjour mon soleil"
    print(a)

bonjour()

class MyApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()





















#a=5+5
#print("hello world")
#print(a)