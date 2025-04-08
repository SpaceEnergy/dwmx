import Millennium, PluginUtils # type: ignore 
import psutil, threading, win32process, win32con, ctypes, ctypes.wintypes

from patcher.patch_window_ctx    import*
from proto.set_window_event_hook import*
from proto.window_com_proto      import*
from proto.com_initialize        import*
from proto.win_event_proc_type   import*
from xplatform.platform_check    import*

WINEVENT_OUTOFCONTEXT = 0x0000

class Plugin:

    def _front_end_loaded(self):
        if self.WINDOWS_VERSION_NOT_SUPPORTED:
            print("Frontend loaded, with error")
            Millennium.call_frontend_method("ShowAlertMessage", params=["Aw snap...", "It seems your windows version is incompatible with this plugin. You must be running Windows 11 or newer."])


    def GetProcessName(self, processId):
        try:
            return psutil.Process(processId).name()
        except psutil.NoSuchProcess:
            return None


    def WindowEventCallback(self, hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):

        # Skip EVENT_OBJECT_SHOW events
        if event == 32770:
            return
        

        threadId, processId = win32process.GetWindowThreadProcessId(hwnd)
        targetProcessName = self.GetProcessName(processId)

        if targetProcessName == "steamwebhelper.exe":
            PatchWindowContext(hwnd)


    def StartWindowHook(self):

        WinEventProc = WinEventProcType(self.WindowEventCallback)
 
        # Hook all window events
        self.WindowHook = SetWinEventHook(
            win32con.EVENT_MIN, 
            win32con.EVENT_MAX, 
            0, 
            WinEventProc, 
            0, 
            0, 
            WINEVENT_OUTOFCONTEXT
        )

        if not self.WindowHook:
            PROCESS_LOGGER.log("Failed to hook window events")
            return
        
        PROCESS_LOGGER.log("Hooked window events")
        msg = ctypes.wintypes.MSG()

        while self.bIsListening:
            while user32.PeekMessageW(ctypes.byref(msg), 0, 0, 0, win32con.PM_REMOVE):
                user32.TranslateMessageW(msg)
                user32.DispatchMessageW(msg)

        PROCESS_LOGGER.log("Closed message listener...")
        

    def _load(self):    
        self.WINDOWS_VERSION_NOT_SUPPORTED = not IS_CORNER_PREFERENCE_COMPATIBLE or not IS_BLUR_BEHIND_COMPATIBLE

        CoInitialize(0) 
        PROCESS_LOGGER.log("Starting DWMX backend...")
        
        self.bIsListening = True
        self.mainThread   = threading.Thread(target=self.StartWindowHook)

        self.mainThread.start()
        Millennium.ready()


    def _unload(self):
        PROCESS_LOGGER.log("unloading dwmx...")
        self.bIsListening = False
        self.mainThread.join()

        # Unhook the window event
        UnhookWinEvent(self.WindowHook)
        CoUninitialize()
