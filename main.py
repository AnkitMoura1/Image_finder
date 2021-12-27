from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("Frontend.kv")


class FirstScreen(Screen):
    def search_image(self):
        self.manager.current_screen.ids.img.source = "img.png"


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
