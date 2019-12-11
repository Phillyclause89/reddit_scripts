"""https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

"""

import keyboard
import win32gui
import win32con
import time



class WindowNotFoundError(Exception):
    """Error to be raised if window name is not found"""
    pass


def focus_on_window(window_name):
    """Will bring all windows with a specific name to the top. The last one to be brought up will be in focus.

    Todo:
        * I feel like I could do more with this. Might make it its own module

    Examples:
        >>> focus_on_window("Untitled - Notepad")

    Args:
        window_name: (str) The name of the target window that you want to bring into focus

    Returns: None

    Raises:
        WindowNotFoundError(Exception) if window_name is not in the list

    """

    def window_dict_handler(hwnd, top_windows):
        """Adapted from: https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

        """

        if win32gui.IsWindowVisible(hwnd) and len(win32gui.GetWindowText(hwnd)) > 0:
            top_windows[hwnd] = win32gui.GetWindowText(hwnd)

    tw = {}
    win32gui.EnumWindows(window_dict_handler, tw)
    for handle in tw:
        if tw[handle] == window_name:
            win32gui.ShowWindow(handle, win32con.SW_NORMAL)
            win32gui.BringWindowToTop(handle)
            try:
                win32gui.SetForegroundWindow(handle)
            except Exception as e:
                if e.__str__() == "(0, 'SetForegroundWindow', 'No error message is available')":
                    pass
                else:
                    raise e

            return None
    raise WindowNotFoundError(f"WindowNotFoundError : The window name '{window_name}' does not appear to be an item in: {tw}")


if __name__ == "__main__":
    # Example require fresh window instances of Notepad and Command Prompt
    # Example call to program with the name "Untitled - Notepad" (windows default for new notepad instance) to top
    focus_on_window("Untitled - Notepad")
    # Safety sleep just in case our PC is slow to bring up the windowHello There!
    time.sleep(1)
    # Send our text into the window
    keyboard.write("Hello There!")
    # Example with CMD
    time.sleep(1)
    focus_on_window(r"Command Prompt")
    time.sleep(1)
    keyboard.write("python\nimport this\n")


