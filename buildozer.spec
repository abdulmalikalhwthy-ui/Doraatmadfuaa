[app]
title = Remote Courses
package.name = remotecourses
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 👇 هذا هو التعديل الحاسم: استخدام الإصدار المستقر وتجنب materialshapes و pycairo
requirements = python3,kivy==2.3.1,kivymd==2.0.0,requests,flask,materialyoucolor==3.0.3,pillow,exceptiongroup,asyncgui,asynckivy,android

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
