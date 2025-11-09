[app]

# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.1,kivymd,pillow

# (str) Presplash of the application
# NOTE: Uncomment if the file exists in the repo at assets/calculatorsplash.png
# presplash.filename = %(source.dir)s/assets/calculatorsplash.png

# (str) Icon of the application
# NOTE: Uncomment if the file exists in the repo at assets/calculator.png
# icon.filename = %(source.dir)s/assets/calculator.png

# (list) Supported orientations
orientation = portrait

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
# Make android.sdk consistent with android.api to avoid mismatches in tool selection
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
