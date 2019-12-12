from unittest import TestCase
import window_refocus
import os
import time

class Test(TestCase):
    def test_bring_window_to_top(self):
        with self.assertRaises(window_refocus.WindowNotFoundError) as e:
            window_refocus.focus_on_window("TEST FAILED!!!!!!!!!!!")

        os.startfile(r"C:\WINDOWS\system32\notepad.exe")
        time.sleep(2)
        os.startfile(r"C:\WINDOWS\system32\cmd")
        time.sleep(2)
        window_refocus.focus_on_window("Untitled - Notepad")
        time.sleep(2)
        window_refocus.focus_on_window("C:\WINDOWS\system32\cmd.exe")

