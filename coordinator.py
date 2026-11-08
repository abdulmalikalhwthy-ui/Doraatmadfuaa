from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivy.metrics import dp

translations = {
    'ar': {'coordinator_panel': 'لوحة المنسق العام', 'welcome': 'مرحباً بك أيها المنسق', 'new_requests': 'طلبات التسجيل الجديدة', 'payments': 'مراجعة المقاصصة المالية', 'cards': 'إدخال كروت الدفع (داخلي/خارجي)'},
    'en': {'coordinator_panel': 'Coordinator Panel', 'welcome': 'Welcome Coordinator', 'new_requests': 'New Registration Requests', 'payments': 'Review Payments / Reconciliation', 'cards': 'Manage Payment Cards'},
    'fa': {'coordinator_panel': 'پنل هماهنگ‌کننده', 'welcome': 'خوش آمدید هماهنگ‌کننده', 'new_requests': 'درخواست‌های ثبت‌نام جدید', 'payments': 'بررسی تسویه حساب', 'cards': 'مدیریت کارت‌های پرداخت'}
}

current_lang = 'ar'

class CoordinatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical')
        
        self.toolbar = MDTopAppBar(
            MDTopAppBarTitle(text=translations[current_lang]['coordinator_panel']),
            type="small"
        )
        self.layout.add_widget(self.toolbar)
        
        self.welcome_lbl = MDLabel(text=translations[current_lang]['welcome'], halign="center", font_style="H5", size_hint_y=0.2)
        self.layout.add_widget(self.welcome_lbl)
        
        self.btn_requests = MDButton(MDButtonText(text=translations[current_lang]['new_requests'] + " (0)"), style="filled", size_hint=(1, 0.2), md_bg_color=(0.8, 0.4, 0.1, 1))
        self.btn_payments = MDButton(MDButtonText(text=translations[current_lang]['payments']), style="filled", size_hint=(1, 0.2), md_bg_color=(0.1, 0.6, 0.3, 1))
        self.btn_cards = MDButton(MDButtonText(text=translations[current_lang]['cards']), style="filled", size_hint=(1, 0.2))
        
        self.layout.add_widget(self.btn_requests)
        self.layout.add_widget(self.btn_payments)
        self.layout.add_widget(self.btn_cards)
        
        self.add_widget(self.layout)

    def change_language(self):
        global current_lang
        if current_lang == 'ar': current_lang = 'en'
        elif current_lang == 'en': current_lang = 'fa'
        else: current_lang = 'ar'
        
        self.toolbar.children[0].text = translations[current_lang]['coordinator_panel']
        self.welcome_lbl.text = translations[current_lang]['welcome']
        self.btn_requests.children[0].text = translations[current_lang]['new_requests'] + " (0)"
        self.btn_payments.children[0].text = translations[current_lang]['payments']
        self.btn_cards.children[0].text = translations[current_lang]['cards']

class CoordinatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        sm = MDScreenManager()
        sm.add_widget(CoordinatorScreen())
        return sm

if __name__ == '__main__':
    CoordinatorApp().run()