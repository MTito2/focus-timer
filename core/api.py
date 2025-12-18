from firebase.registers import get_registers_by_period, IndicadorManager

class API:
    def __init__(self, stopwatch, controller, idle_monitor):
        self.stopwatch = stopwatch
        self.controller = controller
        self.idle_monitor = idle_monitor
        self.indicators = IndicadorManager()
        self.period = None
        self.registers = None

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
        return True

    def save_in_db(self):
        return self.controller.save_in_db()

    def setter_idle_limit(self, idle_limit):
        self.idle_monitor.setter_idle_limit = idle_limit
    
    def set_period(self, period):
        self.period = period

    def get_registers(self):
        self.registers = get_registers_by_period(self.period)
        return self.registers
    
    def get_total_hours(self):
        return self.indicators.get_total_time(self.registers)
    
    def get_biggest_session(self):
        return self.indicators.get_biggest_session(self.registers)

    def get_average_time(self):
        return self.indicators.get_average_time(self.registers)
    
    def get_proportion_focus(self):
         return self.indicators.get_proportion_focus(self.registers)