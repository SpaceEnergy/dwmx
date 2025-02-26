import os, sys
import platform  # Import platform module

def IsCornerPreferenceCompatible():
    
    if sys.platform != "win32":
        return False  # Not a Windows OS
    
    # Check if the system is Windows 11. 
    # This is necessary because the DWMWA_WINDOW_CORNER_PREFERENCE attribute is only available on Windows 11 and later.
    if platform.system() == "Windows" and int(platform.version().split('.')[2]) >= 22000:
        return True
    
    return False


def IsBlurBehindCompatible():
    
    if sys.platform != "win32":
        return False  # Not a Windows OS
    
    # Check if the system is Windows 10 version 1803 or higher.
    if platform.system() == "Windows" and int(platform.version().split('.')[2]) >= 17134:
        return True
    
    return False

IS_CORNER_PREFERENCE_COMPATIBLE = IsCornerPreferenceCompatible()
IS_BLUR_BEHIND_COMPATIBLE       = IsBlurBehindCompatible()
