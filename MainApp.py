from kivy.app import App
from kivy.uix.button import Button
from CityFormatter import CityFormatter


class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        city = CityFormatter("london", 3)
        info = city.show_available_cities()



if __name__ == '__main__':
    app = MainApp()
    app.run()
