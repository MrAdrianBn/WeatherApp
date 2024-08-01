from kivy.app import App
from kivy.uix.button import Button
from Logic.CityFormatter import CityFormatter
from Logic.TimeFormatter import TimeFormatter
from Logic.WeatherFormatter import WeatherFormatter


class MainApp(App):
    def build(self):
        button = Button(text='Check weather',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        city = CityFormatter("paryz", 3)
        info = city.show_available_cities()
        weather = WeatherFormatter()
        print(weather.extract_weather_information(info[0][1], info[0][2]))
        timer = TimeFormatter()
        timer.set_local_time(weather.get_weather_information()[len(weather.weather_information) - 1])
        print(timer.get_local_time())


if __name__ == '__main__':
    app = MainApp()
    app.run()
