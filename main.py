import requests
import wikipedia
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("Frontend.kv")


class FirstScreen(Screen):
    def search_image(self):
        image_name = self.manager.current_screen.ids.image_name.text
        print(image_name)
        page = wikipedia.page(image_name)
        image_link = page.images[0]
        print(image_link)
        req = requests.get(image_link)
        image_path = 'files/img2.jpg'
        with open(image_path, 'wb') as f:
            f.write(req.content)
        self.manager.current_screen.ids.img.source = image_path


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
