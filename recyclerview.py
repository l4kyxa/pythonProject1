from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView


class EmberViewer(RecycleView):
    def __init__(self):
        super(EmberViewer, self).__init__()


class RVItem(Button):
    def get_data_index(self):
        return self.parent.get_view_index_at(self.center)

    def on_press(self):
        screen = self.parent.parent.parent.parent.manager.get_screen("Plus")
        screen.lbl.text= str(self.parent.parent.data[self.get_data_index()])
        self.parent.parent.parent.parent.manager.current="Plus"
        #print(self.parent.parent.data[self.get_data_index()])
        #print(self.get_data_index())


Builder.load_string('''
<EmberViewer>:
    viewclass: 'RVItem'
    id:rv
    orientation:'vertical'
    space_x: self.size[0]/3
    RecycleBoxLayout:
        color:(0.4, 0.4, 0.4, 1)
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y:None
        height: self.minimum_height
        orientation: 'vertical'
''')