import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'logs'))

import logs.logger
import threading, webview
import time
from utils.config import FRONTEND
from core.api import API
from core.stopwatch import Stopwatch
from core.controller import Controller
from core.monitor import MouseIdleMonitor, WindowMonitor  

controller_state = {
    "is_window_allowed": True,
    "is_idle": False
}

def main_loop():
    while True:
        if not controller_state["is_window_allowed"] or controller_state["is_idle"]:
            stopwatch.pause()

        else:
            stopwatch.resume()

stopwatch = Stopwatch()

window_monitor = WindowMonitor(stopwatch, controller_state)
mouse_monitor = MouseIdleMonitor(stopwatch, controller_state)

controller = Controller(stopwatch, mouse_monitor)

thread_window = threading.Thread(target=window_monitor.run)
thread_mouse = threading.Thread(target=mouse_monitor.run)
thread_main = threading.Thread(target=main_loop)

thread_window.start()
thread_mouse.start()
thread_main.start()

api = API(stopwatch, controller, mouse_monitor)

html_file = FRONTEND / "home.html"
webview.create_window("Focus Timer", str(html_file), js_api=api, confirm_close=True, width=500, height=690)
webview.start(private_mode=True)