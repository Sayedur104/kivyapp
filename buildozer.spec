[app]
# (str) Title of your application
title = RGB/Hex Converter

# (str) Package name
package.name = rgb_hex_converter

# (str) Package domain (used for android/ios package domain)
package.domain = com.satd.apk

# (str) Source code name
source.include_exts = py,png,jpg,kv,atlas,gif

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma-separated list of requirements
# e.g. requirements = sqlite3,kivy
requirements = python3,kivy,string,random

# (list) List of inclusions using pattern matching
# e.g. source.include_patterns = assets/*,images/*
source.include_patterns = images/*,icons/*,images/*.png,icons/*.png

# (list) List of exclusions using pattern matching
# e.g. source.exclude_patterns = license,images/exclude/*
source.exclude_patterns = tests/*,docs/*

# (str) Application entry point, default is 'main.py'
# e.g. entrypoint = main.py
entrypoint = main.py

# (str) Full path to a custom kivy configuration file (default: None)
# e.g. kivy_config = /path/to/config.ini
kivy_config =

# (str) Custom build directory
# e.g. build_dir = /path/to/build/dir
build_dir = .buildozer

# (str) Path to a custom splash screen (optional)
# e.g. splash = path/to/splash.png
presplash.filename = loading.gif

# (str) Path to a custom icon (optional)
# e.g. icon.filename = path/to/icon.png
icon.filename = icon.png

# (list) List of additional libraries to include
# e.g. lib.include_libs = lib/*,anotherlib/*
lib.include_libs =

# (list) List of extra packages to include in the build
# e.g. extra_packages = package1,package2
extra_packages =

[buildozer]
# (str) Path to the directory where the build will be created
# e.g. build_dir = /path/to/build
build_dir = .buildozer

# (str) Path to the directory where the Android SDK is located
# e.g. android.sdk_path = /path/to/android-sdk
android.sdk_path =

# (str) Path to the directory where the Android NDK is located
# e.g. android.ndk_path = /path/to/android-ndk
android.ndk_path =

# (str) Path to the directory where the Android NDK is located
# e.g. android.ndk_path = /path/to/android-ndk
android.ndk_path =

# (str) Path to the directory where the Java JDK is located
# e.g. android.jdk_path = /path/to/java-jdk
android.jdk_path =

# (list) List of extra Android permissions (for example: INTERNET)
# e.g. android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.permissions = INTERNET

# (str) Application orientation (one of: portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the app should be compiled in debug mode (default: True)
debug = True

# (bool) Indicate if the app should be compiled in release mode (default: False)
release = False

# (str) The name of the resulting APK file (default: "MyKivyApp")
# e.g. apk.filename = MyKivyApp
apk.filename = RGB_Hex_Converter

# (list) List of additional Android libraries to include
# e.g. android.add_libs = lib/*,anotherlib/*
android.add_libs =

# (str) The name of the resulting APK file (default: "MyKivyApp")
# e.g. apk.filename = MyKivyApp
apk.filename = RGB_Hex_Converter

# (str) Path to the Android NDK (default: None)
# e.g. android.ndk_path = /path/to/android-ndk
android.ndk_path =

# (str) Path to the Java JDK (default: None)
# e.g. android.jdk_path = /path/to/java-jdk
android.jdk_path =

# (str) Path to the Android SDK (default: None)
# e.g. android.sdk_path = /path/to/android-sdk
android.sdk_path =

# (list) List of extra permissions to request
# e.g. android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.permissions = INTERNET

# (bool) Whether to add extra flags for the build (default: False)
# e.g. android.extra_flags = --debug
android.extra_flags =