
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertToKmApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_value(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_calculate(self):
        KM_CONVERSION = 1.60934
        value = self.get_value()
        result = value * KM_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.get_value() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()


ConvertToKmApp().run()