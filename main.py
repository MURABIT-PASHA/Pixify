from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivymd.app import MDApp
from view.home_page import HomePage
from view.canvas import DrawCanvas


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = DictProperty()
        self.screen = Builder.load_file('view/home_page.kv')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.data = {
            'Python': [
                'language-python',
                "on_press", lambda x: print("pressed PHP"),
                "on_release", lambda x: self.callback
            ],
            'PHP': [
                'language-php',
                "on_press", lambda x: print("pressed PHP"),
                "on_release", lambda x: self.callback
            ],
            'C++': [
                'language-cpp',
                "on_press", lambda x: print("pressed C++"),
                "on_release", lambda x: self.callback
            ],
        }
        return Factory.HomePage()

    def callback(self, **args):
        print(args)


if __name__ == "__main__":
    MainApp().run()
