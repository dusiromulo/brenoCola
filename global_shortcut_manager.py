__author__ = 'Roland'


class GlobalShortcutManager():

    def __init__(self, os_type):
        self.os_type = os_type
        self.global_service = None

    def set_service_on(self):
        if self.os_type == 'windows':
            import os
            import sys
            import ctypes
            from ctypes import wintypes
            import win32con
            self.global_service = WindowsGlobalShortcut()
        elif self.os_type == 'linux':
            import gtk
            import keybinder
            self.global_service = LinuxGlobalShortcut()
        else:
            self.global_service = MacGlobalShortcut()


class WindowsGlobalShortcut():

    def __init__(self):
        self.byref = ctypes.byref
        self.user32 = ctypes.windll.user32

        self.HOTKEYS = {
            1: (win32con.VK_F3, win32con.MOD_WIN),
            2: (win32con.VK_F4, win32con.MOD_WIN)
        }
        self.start_service()

    def handle_win_f3(self):
        os.startfile(os.environ['TEMP'])

    def handle_win_f4(self):
        self.user32.PostQuitMessage(0)

    def start_service(self):

        HOTKEY_ACTIONS = {
            1: self.handle_win_f3,
            2: self.handle_win_f4
        }
        #
        # RegisterHotKey takes:
        #  Window handle for WM_HOTKEY messages (None = this thread)
        #  arbitrary id unique within the thread
        #  modifiers (MOD_SHIFT, MOD_ALT, MOD_CONTROL, MOD_WIN)
        #  VK code (either ord ('x') or one of win32con.VK_*)
        #
        for id, (vk, modifiers) in self.HOTKEYS.items():
            print("Registering id", id, "for key", vk)
            if not self.user32.RegisterHotKey(None, id, modifiers, vk):
                print("Unable to register id", id)

        #
        # Home-grown Windows message loop: does
        #  just enough to handle the WM_HOTKEY
        #  messages and pass everything else along.
        #
        try:
            msg = wintypes.MSG()
            while self.user32.GetMessageA(self.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    action_to_take = HOTKEY_ACTIONS.get(msg.wParam)
                    if action_to_take:
                        action_to_take()

                self.user32.TranslateMessage(self.byref(msg))
                self.user32.DispatchMessageA(self.byref(msg))

        finally:
            for id in self.HOTKEYS.keys():
                self.user32.UnregisterHotKey (None, id)


class LinuxGlobalShortcut():

    def __init__(self):
        keystr = "<Ctrl>1"
        keybinder.bind(keystr, self.keybinder_callback)
        gtk.main()

    def keybinder_callback():
        gtk.main_quit()

    def _clipboard_changed(clipboard, event):
        cbText = clipboard.wait_for_text()

        gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY).connect("owner-change", _clipboard_changed)


class MacGlobalShortcut():

    pass