
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class FormScreen(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = "vertical"
        self.opacity = 0.4
        self.padding = 20
        self.spacing = 20
        grid = GridLayout()
        grid.spacing = 10
        grid.cols = 2
        nev = Label(text="Név")
        nev.bind(pos=self.redraw, size=self.redraw)
        with nev.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.bg_rec = Rectangle(size=nev.size, pos=nev.pos)
        grid.add_widget(nev)
        nevmezo = TextInput(multiline=False)  # password=True,
        nevmezo.foreground_color = (0.0, 0.0, 0.0, 1)
        nevmezo.background_normal = "index.jpg"
        nevmezo.background_active = "index.jpg"
        nevmezo.font_size = 20
        nevmezo.font_name = "Roboto-Bold"
        grid.add_widget(nevmezo)
        kor = Label(text="Kor")
        kor.bind(pos=self.redrawKor, size=self.redrawKor)
        with kor.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.bg_rec_Kor = Rectangle(size=kor.size, pos=kor.pos)
        grid.add_widget(kor)
        self.add_widget(grid)
        kormezo = TextInput(multiline=False)  # password=True,
        kormezo.foreground_color = (0.0, 0.0, 0.0, 1)
        # kormezo.background_color=(0.5,0.5,0.5,1)
        kormezo.background_normal = "index.jpg"
        kormezo.background_active = "index.jpg"
        kormezo.font_size = 20
        kormezo.font_name = "Roboto-Bold"
        grid.add_widget(kormezo)
        button = Button(text="Ellenőrzés")
       # button.bind(on_press=self.checkFieldsAndPrintData)
        button.background_normal = "index.jpg"
        button.background_down = "cica.jpg"
        self.add_widget(button)
        float = FloatLayout(size=(300, 300))
        self.add_widget(float)
        btn = Button(text="én is", size_hint=(0.5, 0.2))  # x tengely, ytengely
        btn.pos_hint = {'center_x': 0.5, 'y': 0.5}
        btn2 = Button(text="én is", size_hint=(0.5, 0.2))  # x tengely, ytengely
        btn2.pos_hint = {'center_x': 0.2, 'y': 0.5}
        float.add_widget(btn)
        float.add_widget(btn2)

    def redraw(self, instance, value):
            self.bg_rec.size = instance.size
            self.bg_rec.pos = instance.pos
    def redrawKor(self, instance, value):
            self.bg_rec_Kor.size = instance.size
            self.bg_rec_Kor.pos = instance.pos
    def checkFieldAndprintData(self, instance):
            self


class Hello(App):
    def build(self):
        formScreen = FormScreen()
        return formScreen

helloapp = Hello()
helloapp.run()