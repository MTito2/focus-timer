from datetime import timedelta

from utils.functions import export_json, read_json, timestamp
from utils.config import DATA_PATH

class Controller:
    def __init__(self, stopwatch, mouse_monitor):
        self.stopwatch = stopwatch
        self.mouse_monitor = mouse_monitor
        self.result = None
        self.idle_time = timedelta(seconds=0)
        self.raw_time = timedelta(seconds=0)

    def calculate_final_time(self):
        idle_limit = timedelta(seconds=self.mouse_monitor.get_idle_limit())
        idle_pause_count = self.mouse_monitor.get_idle_pause_count()

        if idle_pause_count > 0:
            self.raw_time = self.stopwatch.stop()
            self.idle_time = idle_limit * idle_pause_count
            self.result = self.raw_time - self.idle_time
        
        else:
            self.result = self.stopwatch.stop()

        
        return self.result
    
    def export_report(self):
        if self.stopwatch.is_finished:
            report = read_json(DATA_PATH, "report.json")

            duration = self.result
            idle_time = self.idle_time
            raw_time = self.raw_time

            content = [{
                "date": str(timestamp()),
                "description": self.stopwatch.get_study_title(),
                "raw_time": str(raw_time),
                "idle_time": str(idle_time),
                "actual_duration": str(duration),
                }]

            for item in content:
                report.append(item)

            export_json(report, DATA_PATH, "report.json")

            self.stopwatch.is_finished = False



