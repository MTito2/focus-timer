import win32process, win32gui, psutil, mouse
from stopwatch import Stopwatch
from datetime import timedelta

class WindowMonitor:
    def __init__ (self, stopwatch, controler):
        self.study_apps = ["Code.exe", "firefox.exe", "pythonw.exe"]
        self.stopwatch = stopwatch
        self.last_process = None
        self.running = None
        self.controler = controler
    
    def get_active_process(self):
        handle = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(handle)[1]

        try:
            process = psutil.Process(pid)
            process_name = process.name()
            return process_name
        
        except:
            return None
        
        
    def run(self):
        self.running = True

        while self.running:
            current_process = self.get_active_process()

            if current_process != self.last_process:
                if current_process in self.study_apps:
                    
                    if self.stopwatch.is_paused(): 
                       self.controler["is_window_allowed"] = True

                else:
                    self.controler["is_window_allowed"] = False
            
            self.last_process = current_process
 
class MouseIdleMonitor:
    def __init__(self, stopwatch, controler):
        self.stopwatch = stopwatch
        self.idle_limit = 300
        self.controler = controler
        self.idle_stopwatch = Stopwatch()
        self.last_mouse_position = mouse.get_position()
        self.idle_pause_count = 0
        self.already_counted = False

    def is_idle(self):
        if self.stopwatch.is_started():
            total_time_idle = self.idle_stopwatch.elapsed()

            if total_time_idle.seconds >= self.idle_limit:
                return True

            return False
    
    def get_idle_pause_count(self):
        return self.idle_pause_count
    
    @property
    def get_idle_limit(self):
        return self.idle_limit
    
    @get_idle_limit.setter
    def setter_idle_limit(self, idle_limit):
        self.idle_limit = idle_limit * 60
    
    def run(self):

        while True:
            current_mouse_position = mouse.get_position()

            if current_mouse_position == self.last_mouse_position:

                if self.idle_stopwatch.is_started() is False:
                    self.idle_stopwatch.start()
                
                if self.is_idle():
                    self.idle_stopwatch.stop()

                    if self.stopwatch.is_paused() is False:
                        self.controler["is_idle"] = True

                    if self.stopwatch.is_started() and self.already_counted is False:
                        self.idle_pause_count += 1
                        self.already_counted = True

            else:
                if self.idle_stopwatch.is_started():
                    self.idle_stopwatch.stop()

                if self.stopwatch.is_paused():
                    self.controler["is_idle"] = False
                
                self.already_counted = False

            self.last_mouse_position = current_mouse_position

            if self.stopwatch.is_finished:
                self.idle_pause_count = 0
