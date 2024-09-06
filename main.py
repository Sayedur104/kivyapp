from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class ConverterApp(App):
    def build(self):
        # ব্যাকগ্রাউন্ড সেটআপ
        self.root = BoxLayout(orientation='vertical')
        with self.root.canvas.before:
            self.rect = Rectangle(source='bg_image.png', pos=self.root.pos, size=self.root.size)
            self.root.bind(size=self._update_rect, pos=self._update_rect)
        
        # টাইটেল লেবেল
        title_label = Label(text="RGB/Hex Converter", font_size='24sp', size_hint=(1, 0.2))
        
        # ইনপুট বক্স এবং বাটন
        self.input_box = TextInput(hint_text="Enter RGB or Hex", size_hint=(1, 0.2), multiline=False)
        convert_button = Button(text="Convert", on_press=self.convert, size_hint=(1, 0.2))
        
        # আউটপুট লেবেল
        self.output_label = Label(text="", size_hint=(1, 0.2))
        
        # লেআউটে যুক্ত করুন
        self.root.add_widget(title_label)
        self.root.add_widget(self.input_box)
        self.root.add_widget(convert_button)
        self.root.add_widget(self.output_label)
        
        return self.root
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def convert(self, instance):
        input_text = self.input_box.text.strip()
        
        if input_text.startswith('#'):
            try:
                r, g, b = tuple(int(input_text[i:i+2], 16) for i in (1, 3, 5))
                self.output_label.text = f"RGB: {r}, {g}, {b}"
            except ValueError:
                self.show_error("Invalid Hex value!")
        else:
            try:
                r, g, b = map(int, input_text.split(','))
                self.output_label.text = f"Hex: #{r:02x}{g:02x}{b:02x}"
            except ValueError:
                self.show_error("Invalid RGB value!")
    
    def show_error(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    ConverterApp().run()