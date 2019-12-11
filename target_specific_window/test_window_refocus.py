from unittest import TestCase
import window_refocus
import os
import time

class Test(TestCase):
    def test_bring_window_to_top(self):
        with self.assertRaises(window_refocus.WindowNotFoundError) as e:
            window_refocus.bring_window_to_top("TEST FAILED!!!!!!!!!!!")

        os.startfile(r"C:\WINDOWS\system32\notepad.exe")
        time.sleep(2)
        os.startfile(r"C:\Users\Philip\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt")
        time.sleep(2)
        window_refocus.bring_window_to_top("Untitled - Notepad")
        time.sleep(2)
        window_refocus.bring_window_to_top("Command Prompt")
        print("pass")

