import os, ctypes

# Load libraries from system32 directly to avoid DLL hijacking
user32 = ctypes.WinDLL(os.path.join(os.environ["WINDIR"], "System32", "user32.dll"))


# SetWinEventHook function prototype
SetWinEventHook          = user32.SetWinEventHook
WinEventProcType         = ctypes.WINFUNCTYPE(None, ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD, ctypes.wintypes.HWND, ctypes.wintypes.LONG, ctypes.wintypes.LONG, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD)
SetWinEventHook.argtypes = [ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.HMODULE, WinEventProcType, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
SetWinEventHook.restype  = ctypes.wintypes.HANDLE

# UnhookWinEvent function prototype
UnhookWinEvent          = user32.UnhookWinEvent
UnhookWinEvent.argtypes = [ctypes.wintypes.HANDLE]
UnhookWinEvent.restype  = ctypes.wintypes.BOOL
