from datetime import timedelta

from utils.functions import export_json, read_json, timestamp
from core.firebase.registers import add_register
from utils.config import DATA_PATH

class Controller:
    def __init__(self, stopwatch, mouse_monitor):
        self.stopwatch = stopwatch
        self.mouse_monitor = mouse_monitor
        self.result = None
        self.idle_time = timedelta(seconds=0)
        self.raw_time = timedelta(seconds=0)

    def calculate_final_time(self):
        idle_limit = timedelta(seconds=self.mouse_monitor.get_idle_limit)
        idle_pause_count = self.mouse_monitor.get_idle_pause_count()

        if idle_pause_count > 0:
            self.raw_time = self.stopwatch.stop()
            self.idle_time = idle_limit * idle_pause_count
            self.result = self.raw_time - self.idle_time
        
        else:
            self.raw_time = self.stopwatch.stop()
            self.result = self.stopwatch.stop()
        
        return self.result
    
    def save_in_db(self):
        print("is_finished:", self.stopwatch.is_finished)

        if self.stopwatch.is_finished:

            duration = self.result
            idle_time = self.idle_time
            raw_time = self.raw_time

            content = {
                "date": str(timestamp()),
                "description": self.stopwatch.get_study_title(),
                "raw_time": str(raw_time),
                "idle_time": str(idle_time),
                "actual_duration": str(duration),
            }

            add_register(content)

            self.stopwatch.is_finished = False
        
        else: 
            return "ok" 
