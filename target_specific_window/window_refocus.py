"""https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

"""

import keyboard
import win32gui
import win32con
import time


class WindowNotFoundError(Exception):
    """Error to be raised if window name is not found"""
    pass


class WindowNotSupportedError(Exception):
    """Error to be raised if window name is not found"""
    pass


def bring_window_to_top(window_name):
    """Will bring all windows with a specific name to the top. The last one to be brought up will be in focus.

    Todo:
        * I feel like I could do more with this. Might make it its own module

    Examples:
        >>> bring_window_to_top("Untitled - Notepad")

    Args:
        window_name: (str) The name of the target window that you want to bring into focus

    Returns: None

    Raises:
        WindowNotFoundError(Exception) if window_name is not in the list

        WindowNotSupportedError(Exception)

    """

    DEBUG = {}

    def window_dict_handler(hwnd, top_windows):
        """Adapted from: https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

        """
        # DEBUG
        top_windows[hwnd] = win32gui.GetWindowText(hwnd)

    tw = {}
    win32gui.EnumWindows(window_dict_handler, tw)
    tw = {i: str(x) for i, x in tw.items() if len(x) > 0}
    for handle in tw:
        if tw[handle] == window_name:
            win32gui.ShowWindow(handle, win32con.SW_NORMAL)
            win32gui.BringWindowToTop(handle)
            win32gui.SetForegroundWindow(handle)
            return None
    raise WindowNotFoundError(f"WindowNotFoundError : '{window_name}' does not appear to be a window name in: {tw}")


if __name__ == "__main__":
    # Example require fresh window instances of Notepad and Command Prompt
    # Example call to program with the name "Untitled - Notepad" (windows default for new notepad instance) to top
    bring_window_to_top("Untitled - Notepad")
    # Safety sleep just in case our PC is slow to bring up the windowHello There!
    time.sleep(1)
    # Send our text into the window
    keyboard.write("Hello There!")
    # Example with CMD
    time.sleep(1)
    bring_window_to_top(r"Command Prompt")
    time.sleep(1)
    keyboard.write("python\nimport this\n")


