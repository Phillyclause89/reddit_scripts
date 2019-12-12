# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/target_specific_window/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/target_specific_window/requirements.txt?style=plastic) | requirements.txt for this adventure.
window_refocus.py| ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/target_specific_window/window_refocus.py?style=plastic) | code for this adventure.
  
## Source Link:
  * [ r/learnpython/.../target_specific_window ]( https://www.reddit.com/r/learnpython/comments/e8u1b6/target_specific_window/ )
  
## Post Title:
  > Target specific window
  
## Post Body:
  > I would like to target a specific window to send keystrokes, I know how to send keystrokes with the keyboard module but I have no idea how to target only that window. Many thanks!

### My Comment(s):
  > Long story short, I believe you'll need to have the window be in focus before you send your key input. You can do this in a few ways.
  > 1) Manually switch the window context from wherever you are when you start the script (CMD/IDE) to the widow that you want to send keystrokes into. This can be tricky as depending on how your script is coded, it might want to start sending keys before you have the opportunity to switch windows. One solution is to do a little countdown at the start of your script to give you enough time to switch: [https://youtu.be/tWqbl9IUdCg?t=30](https://youtu.be/tWqbl9IUdCg?t=30)
  > 2) `pip install pywin32` (if on windows) and run something like this script to ensure the focus is switched to the widow you want. For this to work you'll need to know the name of the window of the window you want and not have any other windows open with the same name. Here is an example scrip that will switch the window context to the notepad program assuming there is a notepad window open named "Untitled - Notepad" (the default new notepad window name).
  > ```python
  > """https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
  > 
  > """
  > 
  > import keyboard
  > import win32gui
  > import win32con
  > import time
  > 
  > 
  > class WindowNotFoundError(Exception):
  >     """Error to be raised if window name is not found"""
  >     pass
  > 
  > 
  > def bring_window_to_top(window_name):
  >     """Will bring all windows with a specific name to the top. The last one to be brought up will be in focus.
  > 
  >     Todo:
  >         * I feel like I could do more with this. Might make it its own module
  > 
  >     Examples:
  >         >>> bring_window_to_top("Untitled - Notepad")
  >         # Will show all windows with the name "Untitled - Notepad"
  > 
  >     Args:
  >         window_name: (str) The name of the target window that you want to bring into focus
  > 
  >     Returns: None
  > 
  >     """
  > 
  >     def window_dict_handler(hwnd, top_windows):
  >         """Adapted from: https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
  > 
  >         """
  >         top_windows[hwnd] = win32gui.GetWindowText(hwnd)
  > 
  >     tw, expt = {}, True
  >     win32gui.EnumWindows(window_dict_handler, tw)
  >     for handle in tw:
  >         if tw[handle] == window_name:
  >             win32gui.ShowWindow(handle, win32con.SW_NORMAL)
  >             win32gui.BringWindowToTop(handle)
  >             win32gui.SetForegroundWindow(handle)
  >             expt = False
  >     if expt:
  >         raise WindowNotFoundError(f"'{window_name}' does not appear to be a window.")
  > 
  > 
  > if __name__ == "__main__":
  >     # Example call to program with the name "Untitled - Notepad" (windows default for new notepad instance) to top
  >     bring_window_to_top("Untitled - Notepad")
  >     # Safety sleep just in case our PC is slow to bring up the window
  >     time.sleep(1)
  >     # Send our text into the window
  >     keyboard.write("Hello There!")
  > ```
