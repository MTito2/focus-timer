class API:
    def __init__(self, stopwatch, controller):
        self.stopwatch = stopwatch
        self.controller = controller

    def start(self):
        self.stopwatch.start()
    
    def pause(self):
        self.stopwatch.pause()

    def elapsed(self):
        return str(self.stopwatch.elapsed())
    
    def stop(self):
        self.stopwatch.stop()

    def is_started(self):
        return self.stopwatch.is_started()

    def is_running(self):
        return self.stopwatch.is_running()
    
    def is_paused(self):
        return self.stopwatch.is_paused()
    
    def receive_study_title(self, title):
        return self.stopwatch.receive_study_title(title)
    
    def calculate_final_time(self):
        self.controller.calculate_final_time()

    def export_report(self):
        self.controller.export_report()