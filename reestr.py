import winreg

KEY_PATH = r"Software\MyApp"

def set_seen(path_to_file: str) -> None:
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, KEY_PATH) as key:
        winreg.SetValueEx(key, "ArgPath", 0, winreg.REG_SZ, path_to_file)

def get_seen() -> str | None:
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEY_PATH) as key:
            value, _ = winreg.QueryValueEx(key, "ArgPath")
            return value
    except FileNotFoundError:
        return None