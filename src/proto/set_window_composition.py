import os, ctypes
from ctypes import wintypes
from enum   import Enum, auto

WCA_ACCENT_POLICY              = 19

class ACCENT_FLAG(Enum):
    ACCENT_FLAG_ENABLE_BLURBEHIND        = 0x20
    ACCENT_FLAG_ENABLE_ACRYLICBLURBEHIND = 0x80
    ACCENT_FLAG_ENABLE_HOSTBACKDROP      = 0x100
    ACCENT_FLAG_INVALID_STATE            = 0x200


class ACCENT_STATE(Enum):
    ACCENT_DISABLED                   = 0
    ACCENT_ENABLE_GRADIENT            = auto()
    ACCENT_ENABLE_TRANSPARENTGRADIENT = auto()
    ACCENT_ENABLE_BLURBEHIND          = auto()
    ACCENT_ENABLE_ACRYLICBLURBEHIND   = auto()
    ACCENT_ENABLE_HOSTBACKDROP        = auto()
    ACCENT_INVALID_STATE              = auto()


class ACCENTPOLICY(ctypes.Structure): _fields_ = [
    ( "nAccentState", ctypes.c_int  ), 
    ( "nFlags",       ctypes.c_int  ), 
    ( "nColor",       ctypes.c_uint ), 
    ( "nAnimationId", ctypes.c_int  )
]


class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure): _fields_ = [
    ( "nAttribute", ctypes.c_uint   ), 
    ( "pData",      ctypes.c_void_p ), 
    ( "ulDataSize", ctypes.c_size_t )
]
    

# Load libraries from system32 directly to avoid DLL hijacking
user32 = ctypes.WinDLL(os.path.join(os.environ["WINDIR"], "System32", "user32.dll"))

# SetWindowCompositionAttribute function prototype
SetWindowCompositionAttribute = user32.SetWindowCompositionAttribute
SetWindowCompositionAttribute.argtypes = [wintypes.HWND, ctypes.POINTER(WINDOWCOMPOSITIONATTRIBDATA)]
SetWindowCompositionAttribute.restype = wintypes.BOOL