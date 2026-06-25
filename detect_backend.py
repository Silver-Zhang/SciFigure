import platform

system = platform.system().lower()

if system == "windows":
    print("windows_ppt_com")
elif system == "darwin":
    print("macos_ppt_script")
elif system == "linux":
    print("python_pptx")
else:
    print("python_pptx_fallback")
