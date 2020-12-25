
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, WipeTransition, RiseInTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from recyclerview import EmberViewer
from kivy.uix.screenmanager import ScreenManager

lista = [{"text":"Karcsi","kor":35},{"text":"Béla","kor":52}]

class DetailsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = FloatLayout(size=Window.size)
        recyclerView = EmberViewer()
        self.rv = recyclerView
        self.rv.width=Window.width
        self.rv.data = lista
        layout.add_widget(recyclerView)
        layout.add_widget(Label(text="Helló"))
        button=Button (text="Back",size_hint=(0.6,0.2))
        button.pos_hint={"center_x":0.5,'y':0.1}
        button.bind(on_press=self.backToForm)
        layout.add_widget(button)
        self.add_widget(layout)
        self.bind(on_pre_enter=self.refreshData)

    def backToForm(self,instance):
        sm.transition.direction = "right"
        sm.current="Plus"
    def refreshData(self,instance):
        self.rv.data=lista


class PlusScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = FloatLayout(size=Window.size)
        self.lbl=Label(text= "One Plus")
        layout.add_widget(self.lbl)
        #layout.add_widget(Label(text="Plus One"))
        button=Button (text="Back",size_hint=(0.6,0.2))
        button.pos_hint={"center_x":0.5,'y':0.1}
        button.bind(on_press=self.backToForm)
        layout.add_widget(button)
        self.add_widget(layout)

    def backToForm(self,instance):
        sm.transition.direction = "right"
        sm.current="Form"

class FormScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.opacity = 0.4
        layout.padding = 20
        layout.spacing = 20
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
        layout.nevmezo=nevmezo
        grid.add_widget(nevmezo)
        kor = Label(text="Kor")
        kor.bind(pos=self.redrawKor, size=self.redrawKor)
        with kor.canvas.before:
            Color(0.4, 0.4, 0.4, 1)
            self.bg_rec_Kor = Rectangle(size=kor.size, pos=kor.pos)
        grid.add_widget(kor)
        layout.add_widget(grid)
        kormezo = TextInput(multiline=False)  # password=True,
        kormezo.foreground_color = (0.0, 0.0, 0.0, 1)
        kormezo.background_normal = "index.jpg"
        kormezo.background_active = "index.jpg"
        kormezo.font_size = 20
        kormezo.font_name = "Roboto-Bold"
        layout.kormezo=kormezo
        grid.add_widget(kormezo)
        button = Button(text="Ellenőrzés")
        button.bind(on_press=self.checkFieldsAndPrintData)
        button.bind(on_touch_down =self.clearInputs)
        button.background_normal = "index.jpg"
        button.background_down = "cica.jpg"
        layout.add_widget(button)

        nextbutton = Button(text="Következő")
        nextbutton.bind(on_press=self.showDetails)
        layout.add_widget(nextbutton)


        float = FloatLayout(size=(300, 300))
        layout.add_widget(float)
        btn = Button(text="én is", size_hint=(0.5, 0.2))  # x tengely, ytengely
        btn.bind(on_touch_down=self.removeIfDoubleTap)
        btn.pos_hint = {'center_x': 0.5, 'y': 0.5}
        btn2 = Button(text="én is2", size_hint=(0.5, 0.2))  # x tengely, ytengely
        btn2.bind(on_touch_down=self.removeIfDoubleTap)
        btn2.pos_hint = {'center_x': 0.2, 'y': 0.5}
        float.add_widget(btn)
        float.add_widget(btn2)
        self.layout=layout
        self.add_widget(layout)
        self.bind(on_leave=self.clearOnLeave)

    def showDetails(self,instance):
        #pass
        sm.transition.direction="left"
        sm.current="Details"
        #sm.current=sm.next()

    def clearOnLeave(self,instance):
        self.layout.kormezo.text = ""
        self.layout.nevmezo.text = ""

    def clearInputs(self,instance,touch):
        if touch.is_double_tap:
            self.layout.kormezo.text=""
            self.layout.nevmezo.text=""
            #popup
            layout = BoxLayout()
            layout.add_widget(Label(text="Kitörölve"))
            closeButton = Button(text="Bezárni")
            layout.add_widget(closeButton)
            popup = Popup(title="Demo",content=layout)
            popup.open()
            closeButton.bind(on_press = popup.dismiss)
        #else:
          #  self.checkFieldsAndPrintData(instance)

    def removeIfDoubleTap(self, instance, touch):
        if touch.is_double_tap:
            parent =instance.parent
            parent.remove_widget(instance)


    def redraw(self, instance, value):
            self.bg_rec.size = instance.size
            self.bg_rec.pos = instance.pos
    def redrawKor(self, instance, value):
            self.bg_rec_Kor.size = instance.size
            self.bg_rec_Kor.pos = instance.pos
    def checkFieldsAndPrintData(self, instance):
        nevmezo=self.layout.nevmezo
        kormezo=self.layout.kormezo
        if len(nevmezo.text) <=0 or len(kormezo.text) <=0:
            if not hasattr(self,"errorMessage"):
             self.layout.errorMessage=Label(text="nem lehet üres")
             self.add_widget(self.layout.errorMessage,len(self.layout.children)-4)
        elif not kormezo.text.isdigit():
            if not hasattr(self, "errorMessage"):
                self.layout.errorMessage = Label(text="a kor egy szám legyen")
                self.add_widget(self.layout.errorMessage, len(self.layout.children) - 4)
            else:
                self.layout.errorMessage.text="a kor egy szám legyen"
        else:
            if hasattr(self, "errorMessage"):
                self.remove_widget(self.layout.errorMessage)
            lista.append({"text":nevmezo.text, "kor":kormezo.text})
            print("A "+nevmezo.text+" nevű kolléga "+kormezo.text+" éves")
            print (len(lista))

sm=ScreenManager()

class Hello(App):
    def build(self):
        formScreen = FormScreen(name="Form")
        sm.add_widget(formScreen)
        detailsScreen = DetailsScreen(name="Details")
        sm.add_widget(detailsScreen)
        plusScreen = PlusScreen(name="Plus")
        sm.add_widget(plusScreen)
        #sm.transition=WipeTransition()
        sm.transition=RiseInTransition() #ilyenkor a tööbi beállitás nem működök

        sm.current ="Form"
        return sm

helloapp = Hello()
helloapp.run()