
from os_identifier import OsIdentifier
from global_shortcut_manager import GlobalShortcutManager

GlobalShortcutManager(OsIdentifier().get_os_type()).set_service_on()
