from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import builder


class FirstScreen(Screen):
    def search_image(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
