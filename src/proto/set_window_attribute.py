import ctypes
from ctypes import wintypes
from enum import Enum, auto
import os

DWMWA_WINDOW_CORNER_PREFERENCE = 33

class DWM_WINDOW_CORNER_PREFERENCE(Enum):
    DWMWCP_DEFAULT    = 0
    DWMWCP_DONOTROUND = auto()
    DWMWCP_ROUND      = auto()
    DWMWCP_ROUNDSMALL = auto()


# Get DWMAPI from system32 directly to avoid DLL hijacking
DWM_API = ctypes.WinDLL(os.path.join(os.environ["WINDIR"], "System32", "dwmapi.dll"))

# DwmSetWindowAttribute function prototype
DwmSetWindowAttribute          = DWM_API.DwmSetWindowAttribute
DwmSetWindowAttribute.argtypes = [wintypes.HWND, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD]
DwmSetWindowAttribute.restype  = ctypes.c_long