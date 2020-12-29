from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView


class ListViewer(RecycleView):
    def __init__(self):
        super(ListViewer, self).__init__()


class RVItem(Button):
    def get_data_index(self):
        return self.parent.get_view_index_at(self.center)



    def on_press(self):
        screen = self.parent.parent.parent.parent.manager.get_screen("Info")
        X=str (self.parent.parent.data[self.get_data_index()])
        b = X.split(",")
        screen.lbl.text = str("RENDSZÁM: "+(b[0][10:(len(b[0]) - 1)])+"\n\nÉVJÁRAT: "+(b[1][13:(len(b[1]) - 1)])+"\n\nTÍPUS: "+(b[2][11:(len(b[2])-1)])+"\n\nÁR: "+(b[3][8:(len(b[3]) - 2)]))
        self.parent.parent.parent.parent.manager.current="Info"



Builder.load_string('''
<ListViewer>:
    viewclass: 'RVItem'
    id:lv
    orientation:'vertical'
    space_x: self.size[0]/10
    RecycleBoxLayout:
        color:(0.5, 0.5, 0.5, 1)
        default_size: None, dp(150)
        default_size_hint: 1, None
        size_hint_y:None
        height: self.minimum_height
        orientation: 'vertical'
        
''')