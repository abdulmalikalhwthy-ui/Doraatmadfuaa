[app]
title = Remote Courses
package.name = remotecourses
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 👇 نستخدم KivyMD لاحقاً، لكن الآن للاختبار سنبني Kivy فقط
requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 25b

# 👇 إعدادات القبول التلقائي للتراخيص (ستتولاها الأداة)
android.accept_sdk_license = True
android.private_storage = True
android.archs = armeabi-v7a
android.enable_androidx = True
