"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward, first version: 11/07/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR = (1, 0, 0, 1)
names = ["Coleson", "Megan", "Jevan", "Nick", "Script"]


class DynamicLabelsApp(App):

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()