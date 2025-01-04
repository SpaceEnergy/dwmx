

# Load libraries from system32 directly to avoid DLL hijacking
import os, ctypes


ole32 = ctypes.WinDLL(os.path.join(os.environ["WINDIR"], "System32", "ole32.dll"))

CoInitialize          = ole32.CoInitialize
CoInitialize.argtypes = [ctypes.c_void_p]
CoInitialize.restype  = ctypes.c_long

CoUninitialize          = ole32.CoUninitialize
CoUninitialize.argtypes = []
CoUninitialize.restype  = None