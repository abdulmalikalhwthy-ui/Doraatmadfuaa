from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SimpleTestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text="مرحباً! هذا اختبار لبناء التطبيق.", font_size=20))
        layout.add_widget(Button(text="زر تجريبي", size_hint=(1, 0.2)))
        return layout

if __name__ == '__main__':
    SimpleTestApp().run()
