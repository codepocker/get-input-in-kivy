from cProfile import label
from cgitb import text
from mimetypes import init
from tkinter import VERTICAL, Button, Grid, Label, Widget
import kivy
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App




class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        #Add widgets
        self.add_widget(Label(text="Name"))
        #Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        #Add widgets
        self.add_widget(Label(text="Email"))
        #Add Input Box
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        #Add Button
        """btn = Button(text="Submit")
        self.add_widget(btn)"""
        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)




    def press(self, instance):
        name = self.name.text
        email = self.email.text

        #following statement is to print the output in the terminal
        #print(f'Hello {name} your Email is {email}')

        #print the output label in APP
        self.add_widget(Label(text=f'Hello {name}! Your Email is {email}'))






class TheLabApp(App):
    def build(self):
        return MyGridLayout()

TheLabApp().run()