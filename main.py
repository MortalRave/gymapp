from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass

class TrainingWindow(Screen):
    pass

class PlanEditorWindow(Screen):
    pass

class StopperWindow(Screen):
    pass

class TimerWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("gym.kv")

class GymApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    GymApp().run()