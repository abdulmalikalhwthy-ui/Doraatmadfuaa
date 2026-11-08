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

SERVER_URL = "http://127.0.0.1:5000"

translations = {
    'ar': {'institute_name': 'معهد المستقبل', 'login': 'تسجيل الدخول', 'username': 'اسم المستخدم', 'password': 'كلمة المرور', 'dashboard': 'لوحة التحكم', 'available_courses': 'الدورات المتاحة', 'courses': 'الدورات', 'no_courses': 'لا توجد دورات مضافة حالياً.', 'error_conn': 'تعذر الاتصال بالسيرفر', 'teacher': 'المدرب', 'price': 'السعر', 'change_lang': 'English'},
    'en': {'institute_name': 'Future Institute', 'login': 'Login', 'username': 'Username', 'password': 'Password', 'dashboard': 'Dashboard', 'available_courses': 'Available Courses', 'courses': 'Courses', 'no_courses': 'No courses available currently.', 'error_conn': 'Connection failed', 'teacher': 'Teacher', 'price': 'Price', 'change_lang': 'فارسی'},
    'fa': {'institute_name': 'موسسه آینده', 'login': 'ورود', 'username': 'نام کاربری', 'password': 'رمز عبور', 'dashboard': 'داشبورد', 'available_courses': 'دوره‌های موجود', 'courses': 'دوره‌ها', 'no_courses': 'در حال حاضر هیچ دوره‌ای وجود ندارد.', 'error_conn': 'عدم اتصال به سرور', 'teacher': 'استاد', 'price': 'قیمت', 'change_lang': 'العربية'}
}

current_lang = 'ar'

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "login"
        self.layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
        
        self.lang_btn = MDButton(MDButtonText(text=translations[current_lang]['change_lang']), style="text", pos_hint={"right": 1}, on_release=self.change_language)
        self.layout.add_widget(self.lang_btn)
        
        header_card = MDCard(size_hint_y=0.4, radius=[20,], elevation=15, md_bg_color=(0.1, 0.2, 0.4, 1))
        header_box = MDBoxLayout(orientation='vertical', padding=dp(10))
        
        self.title_label = MDLabel(text=translations[current_lang]['institute_name'], halign="center", font_style="Headline", role="medium", theme_text_color="Custom", text_color=(1,1,1,1))
        
        header_box.add_widget(self.title_label)
        header_card.add_widget(header_box)
        
        self.layout.add_widget(header_card)
        
        # التعديل هنا: تغيير rectangle إلى filled
        self.username = MDTextField(hint_text=translations[current_lang]['username'], mode="filled")
        self.password = MDTextField(hint_text=translations[current_lang]['password'], password=True, mode="filled")
        
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.password)
        
        self.login_btn = MDButton(MDButtonText(text=translations[current_lang]['login']), style="filled", size_hint_x=1, on_release=self.login)
        self.layout.add_widget(self.login_btn)
        self.add_widget(self.layout)

    def change_language(self, instance):
        global current_lang
        if current_lang == 'ar': current_lang = 'en'
        elif current_lang == 'en': current_lang = 'fa'
        else: current_lang = 'ar'
        
        self.title_label.text = translations[current_lang]['institute_name']
        self.username.hint_text = translations[current_lang]['username']
        self.password.hint_text = translations[current_lang]['password']
        self.login_btn.children[0].text = translations[current_lang]['login']
        self.lang_btn.children[0].text = translations[current_lang]['change_lang']

    def login(self, instance):
        if self.username.text == "student" and self.password.text == "123":
            self.manager.current = "home"

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "home"
        layout = MDBoxLayout(orientation='vertical')
        
        self.toolbar = MDTopAppBar(
            MDTopAppBarTitle(text=translations[current_lang]['dashboard']),
            type="small"
        )
        layout.add_widget(self.toolbar)
        
        self.btn_courses = MDButton(MDButtonText(text=translations[current_lang]['available_courses']), style="filled", size_hint=(1, 0.2), on_release=self.go_courses)
        layout.add_widget(self.btn_courses)
        self.add_widget(layout)

    def on_enter(self):
        self.toolbar.children[0].text = translations[current_lang]['dashboard']
        self.btn_courses.children[0].text = translations[current_lang]['available_courses']

    def go_courses(self, instance):
        self.manager.current = "courses"

class CoursesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "courses"
        layout = MDBoxLayout(orientation='vertical')
        
        self.toolbar = MDTopAppBar(
            MDTopAppBarTitle(text=translations[current_lang]['courses']),
            type="small"
        )
        layout.add_widget(self.toolbar)
        
        self.scroll = MDScrollView()
        self.courses_list = MDList()
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
                    self.courses_list.add_widget(MDLabel(text=translations[current_lang]['no_courses'], halign="center"))
                for c in courses:
                    text = f"{translations[current_lang]['teacher']}: {c['teacher']} | {translations[current_lang]['price']}: {c['price']}"
                    
                    item = MDListItem(
                        MDListItemLeadingIcon(icon="book"),
                        MDListItemHeadlineText(text=c['title']),
                        MDListItemSupportingText(text=text),
                    )
                    self.courses_list.add_widget(item)
        except Exception:
            self.courses_list.add_widget(MDLabel(text=translations[current_lang]['error_conn'], halign="center"))

class StudentApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm = MDScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(CoursesScreen())
        return sm

if __name__ == '__main__':
    StudentApp().run()