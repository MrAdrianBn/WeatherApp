
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from Logic.CityFormatter import CityFormatter


class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)

        self.city = None
        self.rows = 3

        self.add_widget(Label(text="Enter City"))

        self.name = TextInput()
        self.add_widget(self.name)


        self.button = Button(text='Search')
        self.button.bind(on_press=self.call_city)

        self.add_widget(self.button)


    def call_city(self, instance):
        self.city = CityFormatter(self.name.text, 4)
        self.name.text = str(self.city.show_available_cities())

