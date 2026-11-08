import requests
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.appbar import MDTopAppBar, MDTopAppBarTitle
from kivymd.uix.list import MDList, MDListItem, MDListItemHeadlineText, MDListItemSupportingText, MDListItemLeadingIcon
from kivymd.uix.scrollview import MDScrollView
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

# 👇 تم تحديث عنوان IP الخاص بك هنا
SERVER_URL = "http://192.168.0.106:5000"

# ألوان مستوحاة من تصميمك السابق
COLOR_PRIMARY_DARK = get_color_from_hex("#003B2D") # الأخضر الداكن
COLOR_ACCENT = get_color_from_hex("#FFD700") # الذهبي
COLOR_BG = get_color_from_hex("#F5F5F5") # رمادي فاتح للخلفية
COLOR_WHITE = [1, 1, 1, 1]
COLOR_TEXT_GRAY = get_color_from_hex("#777777")

translations = {
    'ar': {'institute_name': 'معهد التنمية بجامعة آل البيت العالمية', 'subtitle': 'نظام إدارة وتنسيق الدورات', 'dev_by': 'إعداد وتطوير', 'dev_name': 'السيد عبد الملك علي الحوثي', 'phone': '+967 777 008 785', 'version': 'الإصدار 1.0.0', 'password': 'أدخل كلمة المرور', 'login': '← دخول', 'courses': 'الدورات المتاحة', 'no_courses': 'لا توجد دورات مضافة حالياً.', 'error_conn': 'تعذر الاتصال بالسيرفر', 'teacher': 'المدرب', 'price': 'السعر'},
    'en': {'institute_name': 'Al-Bayt Development Institute', 'subtitle': 'Course Management System', 'dev_by': 'Developed by', 'dev_name': 'Mr. Abdulmalik Al-Houthi', 'phone': '+967 777 008 785', 'version': 'Version 1.0.0', 'password': 'Enter Password', 'login': '← Login', 'courses': 'Available Courses', 'no_courses': 'No courses available currently.', 'error_conn': 'Connection failed', 'teacher': 'Teacher', 'price': 'Price'},
    'fa': {'institute_name': 'موسسه توسعه دانشگاه آل بیت', 'subtitle': 'سیستم مدیریت دوره‌ها', 'dev_by': 'توسعه دهنده', 'dev_name': 'سید عبدالملک الحوثی', 'phone': '+967 777 008 785', 'version': 'نسخه 1.0.0', 'password': 'رمز عبور را وارد کنید', 'login': 'ورود →', 'courses': 'دوره‌های موجود', 'no_courses': 'در حال حاضر هیچ دوره‌ای وجود ندارد.', 'error_conn': 'عدم اتصال به سرور', 'teacher': 'استاد', 'price': 'قیمت'}
}

current_lang = 'ar'

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"
        
        # خلفية داكنة
        main_layout = MDBoxLayout(orientation='vertical', md_bg_color=COLOR_PRIMARY_DARK)
        
        # زر تغيير اللغة في الأعلى
        top_bar = MDBoxLayout(size_hint_y=None, height=dp(50), padding=[dp(10), dp(10), dp(10), 0])
        self.lang_btn = MDButton(MDButtonText(text='English', theme_text_color="Custom", text_color=COLOR_ACCENT), style="text", pos_hint={"right": 1}, on_release=self.change_language)
        top_bar.add_widget(self.lang_btn)
        main_layout.add_widget(top_bar)

        # المساحة الرئيسية (الشعار والبيانات)
        center_layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15), pos_hint={"center_y": 0.6})
        
        # محاكاة الشعار (يمكنك استبداله بصورة لاحقاً)
        logo_label = MDLabel(text="❖", halign="center", font_style="Display", role="large", theme_text_color="Custom", text_color=COLOR_ACCENT, size_hint_y=None, height=dp(80))
        center_layout.add_widget(logo_label)
        
        self.title_label = MDLabel(text=translations[current_lang]['institute_name'], halign="center", font_style="Title", role="large", theme_text_color="Custom", text_color=COLOR_ACCENT)
        center_layout.add_widget(self.title_label)
        
        self.subtitle_label = MDLabel(text=translations[current_lang]['subtitle'], halign="center", font_style="Subtitle", role="medium", theme_text_color="Custom", text_color=COLOR_WHITE)
        center_layout.add_widget(self.subtitle_label)

        # بطاقة المطور
        dev_card = MDCard(size_hint_y=None, height=dp(140), radius=[dp(15)], elevation=5, md_bg_color=COLOR_PRIMARY_DARK, line_color=COLOR_ACCENT, style="outlined")
        dev_box = MDBoxLayout(orientation='vertical', padding=dp(10))
        self.dev_by = MDLabel(text=translations[current_lang]['dev_by'], halign="center", theme_text_color="Custom", text_color=COLOR_WHITE, font_style="Caption")
        self.dev_name = MDLabel(text=translations[current_lang]['dev_name'], halign="center", theme_text_color="Custom", text_color=COLOR_ACCENT, font_style="Title", role="medium")
        self.phone = MDLabel(text=translations[current_lang]['phone'], halign="center", theme_text_color="Custom", text_color=COLOR_WHITE, font_style="Body")
        self.version = MDLabel(text=translations[current_lang]['version'], halign="center", theme_text_color="Custom", text_color=COLOR_TEXT_GRAY, font_style="Caption")
        
        dev_box.add_widget(self.dev_by)
        dev_box.add_widget(self.dev_name)
        dev_box.add_widget(self.phone)
        dev_box.add_widget(self.version)
        dev_card.add_widget(dev_box)
        
        center_layout.add_widget(dev_card)
        main_layout.add_widget(center_layout)

        # منطقة الإدخال (أسفل الشاشة)
        bottom_layout = MDBoxLayout(orientation='vertical', padding=[dp(20), dp(20), dp(20), dp(40)], spacing=dp(15), size_hint_y=None, height=dp(200), pos_hint={"center_y": 0.2})
        
        self.password = MDTextField(hint_text=translations[current_lang]['password'], password=True, mode="filled", md_bg_color=COLOR_WHITE, text_color=(0,0,0,1))
        bottom_layout.add_widget(self.password)
        
        self.login_btn = MDButton(MDButtonText(text=translations[current_lang]['login'], theme_text_color="Custom", text_color=(0,0,0,1), font_style="Title"), style="filled", size_hint_x=1, height=dp(55), md_bg_color=COLOR_ACCENT, on_release=self.login)
        bottom_layout.add_widget(self.login_btn)
        
        copyright_lbl = MDLabel(text="© 2026 - جميع الحقوق محفوظة", halign="center", theme_text_color="Custom", text_color=COLOR_TEXT_GRAY, font_style="Caption")
        bottom_layout.add_widget(copyright_lbl)

        main_layout.add_widget(bottom_layout)
        self.add_widget(main_layout)

    def change_language(self, instance):
        global current_lang
        if current_lang == 'ar': current_lang = 'en'
        elif current_lang == 'en': current_lang = 'fa'
        else: current_lang = 'ar'
        
        self.title_label.text = translations[current_lang]['institute_name']
        self.subtitle_label.text = translations[current_lang]['subtitle']
        self.dev_by.text = translations[current_lang]['dev_by']
        self.dev_name.text = translations[current_lang]['dev_name']
        self.phone.text = translations[current_lang]['phone']
        self.version.text = translations[current_lang]['version']
        self.password.hint_text = translations[current_lang]['password']
        self.login_btn.children[0].text = translations[current_lang]['login']
        
        if current_lang == 'ar': instance.children[0].text = 'English'
        elif current_lang == 'en': instance.children[0].text = 'فارسی'
        else: instance.children[0].text = 'العربية'

    def login(self, instance):
        # كلمة المرور الافتراضية 1234
        if self.password.text == "1234" or self.password.text == "admin":
            self.manager.current = "courses"
            self.password.text = ""

class CoursesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "courses"
        layout = MDBoxLayout(orientation='vertical', md_bg_color=COLOR_BG)
        
        # شريط علوي مطابق للتصميم
        self.toolbar = MDTopAppBar(
            MDTopAppBarTitle(text=translations[current_lang]['courses'], theme_text_color="Custom", text_color=COLOR_ACCENT),
            type="small",
            md_bg_color=COLOR_PRIMARY_DARK,
            left_action_items=[["arrow-right", lambda x: setattr(self.manager, 'current', 'login')]]
        )
        layout.add_widget(self.toolbar)
        
        self.scroll = MDScrollView(padding=dp(10))
        self.courses_list = MDList(md_bg_color=COLOR_BG)
        self.scroll.add_widget(self.courses_list)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def on_enter(self):
        self.toolbar.children[0].text = translations[current_lang]['courses']
        self.courses_list.clear_widgets()
        try:
            response = requests.get(f"{SERVER_URL}/get_courses", timeout=5)
            if response.status_code == 200:
                courses = response.json()
                if not courses:
                    self.courses_list.add_widget(MDLabel(text=translations[current_lang]['no_courses'], halign="center", padding=dp(20)))
                for c in courses:
                    text = f"{translations[current_lang]['teacher']}: {c['teacher']} | {translations[current_lang]['price']}: {c['price']}"
                    
                    # تصميم البطاقة مطابق لتصميمك السابق
                    card = MDCard(size_hint_y=None, height=dp(80), radius=[dp(15)], elevation=2, md_bg_color=COLOR_WHITE, padding=dp(10))
                    item = MDListItem(
                        MDListItemLeadingIcon(icon="book", theme_icon_color="Custom", icon_color=COLOR_PRIMARY_DARK),
                        MDListItemHeadlineText(text=c['title'], theme_text_color="Custom", text_color=COLOR_PRIMARY_DARK, font_style="Title", role="medium"),
                        MDListItemSupportingText(text=text, theme_text_color="Custom", text_color=COLOR_TEXT_GRAY, font_style="Body", role="small"),
                        md_bg_color=COLOR_WHITE
                    )
                    card.add_widget(item)
                    # إضافة مسافة بين البطاقات
                    wrapper = MDBoxLayout(size_hint_y=None, height=dp(90), padding=[0, dp(5), 0, dp(5)])
                    wrapper.add_widget(card)
                    self.courses_list.add_widget(wrapper)
        except Exception as e:
            self.courses_list.add_widget(MDLabel(text=translations[current_lang]['error_conn'], halign="center", theme_text_color="Custom", text_color=(1,0,0,1)))

class StudentApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green" # ليتوافق مع أيقونات النظام
        self.theme_cls.theme_style = "Light" # التطبيق يعتمد على الخلفيات المخصصة
        
        sm = MDScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(CoursesScreen())
        return sm

if __name__ == '__main__':
    StudentApp().run()
