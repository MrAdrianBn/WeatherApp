from kivy.app import App
from kivy.uix.button import Button
from Query import QueryCreator
import json
import ast


class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):  # tutaj tylko metody beda wywolane a cale konwersje itd w oddzielnych klasach
        query = QueryCreator("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=2&appid"
                             "=c614ed968bb3ba231528a9e4546a27f1")
        json_data = query.make_query()
        print(json_data)
        if json_data:
            first_result = json_data[0]
            lon = first_result.get('lon')
            print(f"Longitude: {lon}")
        else:
            print("No data found")


if __name__ == '__main__':
    app = MainApp()
    app.run()
