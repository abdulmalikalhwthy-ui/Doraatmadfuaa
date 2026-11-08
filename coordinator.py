from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivymd.uix.scrollview import MDScrollView
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

# نفس ألوان التطبيق السابق
COLOR_PRIMARY_DARK = get_color_from_hex("#003B2D") 
COLOR_ACCENT = get_color_from_hex("#FFD700") 
COLOR_BG = get_color_from_hex("#F5F5F5") 
COLOR_WHITE = [1, 1, 1, 1]
COLOR_TEXT_GRAY = get_color_from_hex("#777777")

translations = {
    'ar': {'panel': 'لوحة المنسق العام', 'welcome': 'مرحباً بك أيها المنسق', 'req': 'طلبات التسجيل', 'pay': 'المقاصصة المالية', 'cards': 'كروت الدفع'},
    'en': {'panel': 'Coordinator Panel', 'welcome': 'Welcome Coordinator', 'req': 'Registration Requests', 'pay': 'Financial Reconciliation', 'cards': 'Payment Cards'},
    'fa': {'panel': 'پنل هماهنگ‌کننده', 'welcome': 'خوش آمدید هماهنگ‌کننده', 'req': 'درخواست‌های ثبت‌نام', 'pay': 'تسویه حساب', 'cards': 'کارت‌های پرداخت'}
}
current_lang = 'ar'

class CoordinatorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "coordinator"
        
        layout = MDBoxLayout(orientation='vertical', md_bg_color=COLOR_BG)
        
        # شريط علوي فخم
        self.toolbar = MDTopAppBar(
            MDTopAppBarTitle(text=translations[current_lang]['panel'], theme_text_color="Custom", text_color=COLOR_ACCENT),
            type="small",
            md_bg_color=COLOR_PRIMARY_DARK,
            right_action_items=[["translate", lambda x: self.change_language()]]
        )
        layout.add_widget(self.toolbar)
        
        # منطقة المحتوى
        scroll = MDScrollView(padding=dp(15))
        content = MDBoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        welcome = MDLabel(text=translations[current_lang]['welcome'], halign="center", font_style="Title", role="medium", theme_text_color="Custom", text_color=COLOR_PRIMARY_DARK, size_hint_y=None, height=dp(50))
        content.add_widget(welcome)
        
        # الأزرار (البطاقات)
        self.btn_req = self.create_card(translations[current_lang]['req'], "account-clock", COLOR_PRIMARY_DARK)
        self.btn_pay = self.create_card(translations[current_lang]['pay'], "cash-check", "#4CAF50")
        self.btn_cards = self.create_card(translations[current_lang]['cards'], "credit-card", "#2196F3")
        
        content.add_widget(self.btn_req)
        content.add_widget(self.btn_pay)
        content.add_widget(self.btn_cards)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def create_card(self, text, icon, color):
        card = MDCard(size_hint_y=None, height=dp(100), radius=[dp(15)], elevation=4, md_bg_color=COLOR_WHITE, padding=dp(15), ripple_behavior=True)
        box = MDBoxLayout(orientation='horizontal', spacing=dp(15))
        
        # الأيقونة
        from kivymd.uix.button import MDIconButton
        box.add_widget(MDIconButton(icon=icon, theme_icon_color="Custom", icon_color=color, icon_size=dp(40)))
        
        # النص
        box.add_widget(MDLabel(text=text, halign="right", font_style="Title", role="medium", theme_text_color="Custom", text_color=COLOR_PRIMARY_DARK))
        
        card.add_widget(box)
        return card

    def change_language(self):
        global current_lang
        if current_lang == 'ar': current_lang = 'en'
        elif current_lang == 'en': current_lang = 'fa'
        else: current_lang = 'ar'
        
        self.toolbar.children[0].text = translations[current_lang]['panel']
        self.btn_req.children[0].children[0].text = translations[current_lang]['req']
        self.btn_pay.children[0].children[0].text = translations[current_lang]['pay']
        self.btn_cards.children[0].children[0].text = translations[current_lang]['cards']

class CoordinatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        sm = MDScreenManager()
        sm.add_widget(CoordinatorScreen())
        return sm

if __name__ == '__main__':
    CoordinatorApp().run()
