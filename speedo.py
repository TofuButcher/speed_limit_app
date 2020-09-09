import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import time

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='First Name: '))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text='Last Name: '))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text='Cats or Dogs?: '))
        self.cord = TextInput(multiline=False)
        self.inside.add_widget(self.cord)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.firstname.text
        last = self.lastname.text
        email = self.email.text
        cord = self.cord.text
        if name:
            print('Name: ', name)
        if last:
            print('Last Name: ', last)
        if email:
            print('Email:' , email)
        if cord:
            print('Email:' , cord)

        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""
        self.cord.text = ""

class Main(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    app = Main()
    app.run()

'''name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        self.name.text = ""
        self.email.text = ""'''

#        label = Label(text='Hello from Kivy',
#                      size_hint=(.5, .5),
#                        pos_hint={'center_x': .5, 'center_y': .5})