from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class TortillasScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class TacoApp(App):
    pass


if __name__ == '__main__':
    TacoApp().run()