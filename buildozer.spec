[app]
title = DripClient
package.name = dripclient
package.domain = org.drip
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# ВАЖНО: Настройки для Flet
requirements = python3, flet, flet-core, flet-runtime, hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
