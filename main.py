from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, WipeTransition, RiseInTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from recyclerview import ListViewer
from kivy.uix.screenmanager import ScreenManager
import datetime


lista = [{"text":"ABC123","evjarat":"1955","tipus":"Ford","ar": "500000"},{"text":"P00001","evjarat":"2020","tipus":"Ford 200","ar": "123456789"},{"text":"XYZ000","evjarat":"2000","tipus":"Renault Clio 1.5","ar": "1500000"},{"text":"CICA01","evjarat":"2015","tipus":"Honda","ar": "5500000"}]

class ListaScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.padding = 20
        layout.spacing = 20

        recyclerView = ListViewer()
        self.lv = recyclerView
        self.lv.width=Window.width
        self.lv.data = lista
        layout.add_widget(recyclerView)


        button=Button (text="Vissza",size_hint=(1.0,0.2))
        button.pos_hint={"center_x": 0.5, 'y': 0.0}
        button.color=(1.0, 1.0, 1.0, 1)
        button.background_color=(1.5, 1.5, 1.5, 1)
        button.bind(on_press=self.backToForm)
        layout.add_widget(button)

        self.add_widget(layout)
        self.bind(on_pre_enter=self.refreshData)

    def backToForm(self,instance):
        sm.current="Form"

    def refreshData(self,instance):
        self.lv.data=lista


class InfoScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.padding = 20
        layout.spacing = 20

        label=Label()
        self.lbl=label
        self.lbl.width = Window.width
        self.lbl.font_size=30
        layout.add_widget(label)

        button=Button (text="Vissza",size_hint=(1.0,0.2))
        button.background_color = (1.5, 1.5, 1.5, 1)
        button.pos_hint={"center_x":0.5,'y':0.0}
        button.bind(on_press=self.backToForm)
        layout.add_widget(button)

        self.add_widget(layout)

    def backToForm(self,instance):
        sm.current="Lista"

class FormScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout()
        layout.orientation = "vertical"
        layout.opacity = 1.0
        layout.padding = 20
        layout.spacing = 20
        grid = GridLayout()
        grid.spacing = 10
        grid.cols = 2

#RENDSZAM
        rendszamgomb = Button(text="Rendszám:", size_hint=(1.0, 0.1))
        rendszamgomb.pos_hint = {"center_x": 0.5, 'y': 0.0}
        rendszamgomb.color = (1.0, 1.0, 1.0, 1)
        rendszamgomb.bind(on_press=self.clearRendszammezo)
        grid.add_widget(rendszamgomb)

        rendszammezo = TextInput(multiline=False, write_tab=False)
        rendszammezo.foreground_color = (0.0, 0.0, 0.0, 5)
        rendszammezo.background_color =(1.0, 1.0, 1.0, 5)
        rendszammezo.font_size = 30
        rendszammezo.font_name = "Roboto-Bold"
        layout.rendszammezo=rendszammezo
        grid.add_widget(rendszammezo)

#ÉVJÁRAT
        evjaratgomb = Button(text="Évjárat:", size_hint=(1.0, 0.1))
        evjaratgomb.pos_hint = {"center_x": 0.5, 'y': 0.0}
        evjaratgomb.color = (1.0, 1.0, 1.0, 1)
        evjaratgomb.bind(on_press=self.clearEvjaratmezo)
        grid.add_widget(evjaratgomb)

        evjaratmezo = TextInput(multiline=False,write_tab=False)
        evjaratmezo.foreground_color = (0.0, 0.0, 0.0, 5)
        evjaratmezo.background_color = (1.0, 1.0, 1.0, 5)
        evjaratmezo.font_size = 30
        evjaratmezo.font_name = "Roboto-Bold"
        layout.evjaratmezo = evjaratmezo
        grid.add_widget(evjaratmezo)

#Tipus
        tipusgomb = Button(text="Típus:", size_hint=(1.0, 0.1))
        tipusgomb.pos_hint = {"center_x": 0.5, 'y': 0.0}
        tipusgomb.bind(on_press=self.clearTipusmezo)
        grid.add_widget(tipusgomb)

        tipusmezo = TextInput(multiline=False,write_tab=False)
        tipusmezo.foreground_color = (0.0, 0.0, 0.0, 5)
        tipusmezo.background_color = (1.0, 1.0, 1.0, 5)
        tipusmezo.font_size = 30
        tipusmezo.font_name = "Roboto-Bold"
        layout.tipusmezo = tipusmezo
        grid.add_widget(tipusmezo)

#ÁR
        argomb = Button(text="Ár:", size_hint=(1.0, 0.1))
        argomb.pos_hint = {"center_x": 0.5, 'y': 0.0}
        argomb.bind(on_press=self.clearArmezo)
        grid.add_widget(argomb)

        armezo = TextInput(multiline=False,write_tab=False)
        armezo.foreground_color = (0.0, 0.0, 0.0, 5)
        armezo.background_color = (1.0, 1.0, 1.0, 5)
        armezo.font_size = 30
        armezo.font_name = "Roboto-Bold"
        layout.armezo = armezo
        grid.add_widget(armezo)

        layout.add_widget(grid)

#Gomb
        button1 = Button(text="Hozzáadás",size_hint=(1.0,0.3))
        button1.background_color=(1.5, 1.5, 1.5, 1)
        button1.bind(on_press=self.checkFieldsAndPrintData)
        layout.add_widget(button1)

        button2 = Button(text="Lista",size_hint=(1.0,0.3))
        button2.background_color = (1.5, 1.5, 1.5, 1)
        button2.bind(on_press=self.showDetails)
        layout.add_widget(button2)

        self.layout=layout
        self.add_widget(layout)
        self.bind(on_leave=self.clearOnLeave)

    def showDetails(self,instance):

        sm.transition.direction="left"
        sm.current="Lista"

    def clearOnLeave(self,instance):
        self.layout.evjaratmezo.text = ""
        self.layout.rendszammezo.text = ""
        self.layout.tipusmezo.text = ""
        self.layout.armezo.text = ""

    def clearRendszammezo(self, instance):
        self.layout.rendszammezo.text = ""
    def clearEvjaratmezo(self, instance):
        self.layout.evjaratmezo.text = ""
    def clearTipusmezo(self, instance):
        self.layout.tipusmezo.text = ""
    def clearArmezo(self, instance):
        self.layout.armezo.text = ""

    def checkFieldsAndPrintData(self, instance):
        date = datetime.datetime.now()
        x =(date.year)
        rendszammezo=self.layout.rendszammezo
        evjaratmezo=self.layout.evjaratmezo
        tipusmezo=self.layout.tipusmezo
        armezo=self.layout.armezo

        if len(rendszammezo.text) <=0 or len(evjaratmezo.text) <=0 or len(tipusmezo.text) <=0 or len(armezo.text)<=0:
            layout = BoxLayout()
            layout.orientation = "vertical"
            layout.add_widget(Label(text="Töltsön ki minden mezőt!", font_size=20))
            closeButton = Button(text="Vissza", size_hint=(1.0, 0.2))
            closeButton.background_color = (1.5, 1.5, 1.5, 1)
            layout.add_widget(closeButton)
            popup = Popup(title="Hiba", content=layout)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)

        elif not len(rendszammezo.text) ==6:
            layout = BoxLayout()
            layout.orientation = "vertical"
            layout.add_widget(Label(text="A rendszám nem megfelelő", font_size=20))
            closeButton = Button(text="Vissza", size_hint=(1.0, 0.2))
            closeButton.background_color = (1.5, 1.5, 1.5, 1)
            layout.add_widget(closeButton)
            popup = Popup(title="Hiba", content=layout)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)

        elif not evjaratmezo.text.isdigit() or not len(evjaratmezo.text)==4 or int(evjaratmezo.text) > x or int(evjaratmezo.text)<1000:
            layout = BoxLayout()
            layout.orientation = "vertical"
            layout.add_widget(Label(text="Az évjárat nem megfelelő", font_size=20))
            closeButton = Button(text="Vissza", size_hint=(1.0, 0.2))
            closeButton.background_color = (1.5, 1.5, 1.5, 1)
            layout.add_widget(closeButton)
            popup = Popup(title="Hiba", content=layout)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)

        elif not armezo.text.isdigit():
            layout = BoxLayout()
            layout.orientation = "vertical"
            layout.add_widget(Label(text="Az ár nem megfelelő", font_size=20))
            closeButton = Button(text="Vissza", size_hint=(1.0, 0.2))
            closeButton.background_color = (1.5, 1.5, 1.5, 1)
            layout.add_widget(closeButton)
            popup = Popup(title="Hiba", content=layout)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)

        else:
            layout = BoxLayout()
            layout.orientation = "vertical"
            layout.add_widget(Label(text="Rendszám: "+rendszammezo.text+"\n\nÉvjárat: "+evjaratmezo.text+"\n\nTípus: "+tipusmezo.text+"\n\nÁr: "+armezo.text, font_size=20))
            closeButton = Button(text="Rendben", size_hint=(1.0, 0.2))
            closeButton.background_color = (1.5, 1.5, 1.5, 1)
            layout.add_widget(closeButton)
            popup = Popup(title="Sikeres Mentés", content=layout)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)
            lista.append({"text": rendszammezo.text, "evjarat" : evjaratmezo.text, "tipus" : tipusmezo.text, "ar" : armezo.text})

            self.layout.rendszammezo.text = ""
            self.layout.evjaratmezo.text = ""
            self.layout.tipusmezo.text = ""
            self.layout.armezo.text = ""

sm=ScreenManager()

class Hello(App):
    def build(self):
        self.title = 'Gépjármű-nyilvántartás'
        formScreen = FormScreen(name="Form")
        sm.add_widget(formScreen)

        listaScreen = ListaScreen(name="Lista")
        sm.add_widget(listaScreen)

        infoScreen = InfoScreen(name="Info")
        sm.add_widget(infoScreen)

        sm.transition=RiseInTransition()
        sm.current ="Form"
        return sm

helloapp = Hello()
helloapp.run()