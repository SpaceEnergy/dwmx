import os, ctypes

# Load libraries from system32 directly to avoid DLL hijacking
user32 = ctypes.WinDLL(os.path.join(os.environ["WINDIR"], "System32", "user32.dll"))

PeekMessageW          = user32.PeekMessageW
PeekMessageW.argtypes = [ctypes.POINTER(ctypes.wintypes.MSG), ctypes.wintypes.HWND, ctypes.wintypes.UINT, ctypes.wintypes.UINT, ctypes.wintypes.UINT]
PeekMessageW.restype  = ctypes.wintypes.BOOL

TranslateMessageW          = user32.TranslateMessage
TranslateMessageW.argtypes = [ctypes.POINTER(ctypes.wintypes.MSG)]
TranslateMessageW.restype  = ctypes.wintypes.BOOL

DispatchMessageW          = user32.DispatchMessageW
DispatchMessageW.argtypes = [ctypes.POINTER(ctypes.wintypes.MSG)]
DispatchMessageW.restype  = ctypes.c_long