[app]
title = Test App
package.name = testapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 👇 تبسيط المتطلبات لأقصى حد
requirements = python3,kivy==2.3.1

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
