from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

# 👇 استيراد الشاشات فقط (وليس التطبيقات كاملة)
# هذا يمنع تشغيل التطبيقات القديمة في نفس الوقت
from student import LoginScreen as StudentLoginScreen, CoursesScreen as StudentCoursesScreen
from coordinator import CoordinatorScreen

# ألوان الهوية البصرية
COLOR_PRIMARY_DARK = get_color_from_hex("#003B2D") 
COLOR_ACCENT = get_color_from_hex("#FFD700") 
COLOR_WHITE = [1, 1, 1, 1]

class RoleSelectionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "role_selection"
        
        layout = MDBoxLayout(orientation='vertical', md_bg_color=COLOR_PRIMARY_DARK, padding=dp(30), spacing=dp(20))
        
        layout.add_widget(MDLabel(
            text="مرحباً بك في معهد التنمية",
            halign="center", font_style="Headline", role="medium",
            theme_text_color="Custom", text_color=COLOR_ACCENT,
            size_hint_y=None, height=dp(60)
        ))
        
        layout.add_widget(MDLabel(
            text="الرجاء اختيار نوع الحساب للدخول",
            halign="center", font_style="Subtitle", role="medium",
            theme_text_color="Custom", text_color=COLOR_WHITE,
            size_hint_y=None, height=dp(40)
        ))

        layout.add_widget(MDBoxLayout(size_hint_y=0.1))

        # زر الطالب
        student_btn = MDCard(
            size_hint_y=None, height=dp(100), radius=[dp(20)], elevation=8, 
            md_bg_color=COLOR_WHITE, ripple_behavior=True, on_release=self.go_to_student
        )
        student_box = MDBoxLayout(orientation='horizontal', padding=dp(20), spacing=dp(15))
        student_box.add_widget(MDLabel(text="🎓", font_style="Display", role="large", size_hint_x=None, width=dp(60)))
        student_box.add_widget(MDLabel(text="دخول الطالب\n(عرض الدورات والتسجيل)", font_style="Title", role="medium", theme_text_color="Custom", text_color=COLOR_PRIMARY_DARK))
        student_btn.add_widget(student_box)
        
        # زر المنسق
        coord_btn = MDCard(
            size_hint_y=None, height=dp(100), radius=[dp(20)], elevation=8, 
            md_bg_color=COLOR_ACCENT, ripple_behavior=True, on_release=self.go_to_coordinator
        )
        coord_box = MDBoxLayout(orientation='horizontal', padding=dp(20), spacing=dp(15))
        coord_box.add_widget(MDLabel(text="💼", font_style="Display", role="large", size_hint_x=None, width=dp(60)))
        coord_box.add_widget(MDLabel(text="دخول المنسق\n(إدارة الطلبات والمقاصصة)", font_style="Title", role="medium", theme_text_color="Custom", text_color=(0,0,0,1)))
        coord_btn.add_widget(coord_box)

        layout.add_widget(student_btn)
        layout.add_widget(coord_btn)
        
        layout.add_widget(MDBoxLayout(size_hint_y=0.2))
        layout.add_widget(MDLabel(
            text="إعداد وتطوير: السيد عبد الملك علي الحوثي\nالإصدار 1.0.0",
            halign="center", font_style="Caption",
            theme_text_color="Custom", text_color=(0.8, 0.8, 0.8, 1),
            size_hint_y=None, height=dp(50)
        ))

        self.add_widget(layout)

    def go_to_student(self, instance):
        # الانتقال إلى شاشة تسجيل دخول الطالب
        self.manager.current = "student_login"

    def go_to_coordinator(self, instance):
        # الانتقال إلى شاشة المنسق
        self.manager.current = "coordinator_main"

class UnifiedApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        
        # مدير الشاشات الموحد
        sm = MDScreenManager()
        
        # 1. شاشة اختيار نوع الحساب
        sm.add_widget(RoleSelectionScreen())
        
        # 2. شاشات تطبيق الطالب (تم استيرادها من student.py)
        sm.add_widget(StudentLoginScreen())
        sm.add_widget(StudentCoursesScreen())
        
        # 3. شاشات تطبيق المنسق (تم استيرادها من coordinator.py)
        sm.add_widget(CoordinatorScreen())
        
        return sm

if __name__ == '__main__':
    UnifiedApp().run()