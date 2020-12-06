#!/bin/python
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.image import Image
#ok here I understand everything

#new class called CharacterList inherits from StackLayout class
class CharacterList(StackLayout):
    def __init__(self, characters_dict_list, **kwargs):
        super(CharacterList, self).__init__(**kwargs)        
        self.characters_dict_list = characters_dict_list
        self.list_widget = self.dict_to_label_list()    
        self.add_widget(self.list_widget)     
    
    def dict_to_label_list(self):
        list_widget = StackLayout() 
        for i in self.characters_dict_list:
            list_widget.add_widget(Label(text=i['name'], size_hint=[1.0,0.10]))
            list_widget.add_widget(Image(source=i['img'], size_hint=[1.0,0.10]))
        return list_widget


class MyRootApp(RelativeLayout):
    def __init__(self, **kwargs):
        super(MyRootApp, self).__init__(**kwargs)
    
        self.character_list = CharacterList([ { 'name': 'Fred', 'img': './assets/fred.png' },
                       { 'name': 'Ned', 'img': './assets/ned.png' },
                       { 'name': 'CPU', 'img': './assets/CPU.png' },
                       { 'name': 'CPU2', 'img': './assets/CPU.png' },
                       { 'name': 'CPU3', 'img': './assets/CPU.png' },
                       { 'name': 'CPU4', 'img': './assets/CPU.png' },
                       { 'name': 'CPU5', 'img': './assets/CPU.png' },
                       { 'name': 'CPU6', 'img': './assets/CPU.png' },
                       { 'name': 'CPU7', 'img': './assets/CPU.png' },
                       { 'name': 'CPU9', 'img': './assets/CPU.png' }, ] )
                                   
        self.add_widget(self.character_list) 

class KivyApp(App):

    def build(self):
        return MyRootApp()

if __name__ == '__main__':
    KivyApp().run()
