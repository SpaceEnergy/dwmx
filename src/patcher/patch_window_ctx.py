import ctypes
from xplatform.platform_check     import*
from proto.set_window_attribute   import*
from proto.set_window_composition import*

def EnableBlurBehind(target):
    policy = ACCENTPOLICY()
    policy.nAccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value
    policy.nFlags = ACCENT_FLAG.ACCENT_FLAG_ENABLE_BLURBEHIND.value
    policy.nColor = 0x00000000
    policy.nAnimationId = 0

    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.nAttribute = WCA_ACCENT_POLICY
    data.pData = ctypes.cast(ctypes.pointer(policy), ctypes.c_void_p)
    data.ulDataSize = ctypes.sizeof(policy)

    return SetWindowCompositionAttribute(target, ctypes.byref(data))


def EnableRoundedCorners(target):
    value = ctypes.c_int(DWM_WINDOW_CORNER_PREFERENCE.DWMWCP_ROUND.value)
    DwmSetWindowAttribute(target, DWMWA_WINDOW_CORNER_PREFERENCE, ctypes.byref(value), ctypes.sizeof(value))

def PatchWindowContext(hwnd):
    if IS_CORNER_PREFERENCE_COMPATIBLE:
        EnableRoundedCorners(hwnd)

    if IS_BLUR_BEHIND_COMPATIBLE:
        EnableBlurBehind(hwnd)