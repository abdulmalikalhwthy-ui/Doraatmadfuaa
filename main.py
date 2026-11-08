name: Build APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

    - name: Install Buildozer and Cython
      run: |
        pip3 install --user --upgrade buildozer
        pip3 install --user --upgrade cython virtualenv

    # 👇 الحل: إجبار Buildozer على استخدام مرايا Huawei Cloud لتحميل SDK و NDK
    - name: Build with Buildozer
      run: |
        export PATH=$PATH:~/.local/bin
        # توجيه Buildozer لاستخدام مرايا سريعة
        export BUILDOZER_ANDROID_SDK_URL="https://repo.huaweicloud.com/android/repository/"
        export BUILDOZER_ANDROID_NDK_URL="https://repo.huaweicloud.com/android/repository/"
        echo y | buildozer -v android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk
