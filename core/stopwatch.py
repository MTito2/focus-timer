
import os, sys
from datetime import datetime, timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'config'))

from utils.functions import timestamp
    
class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._is_running = False
        self._is_paused = False
        self._accumulated_time = timedelta(0)
        self._total = ""
        self._current_study_title = ""
        self._is_finished = None

    def start(self):
        if self._is_running is False:
            self._start_time = timestamp()
            self._is_running = True

    def pause(self):
        if self._is_running:
            self._is_paused = True
            self._is_running = False
            self._accumulated_time += timestamp() - self._start_time
        
    def resume(self):
        if self._is_paused and self._is_running is False:
            self._start_time = timestamp()
            self._is_paused = False
            self._is_running = True

    def elapsed(self):
        if self._is_running:
            return self._accumulated_time + (timestamp() - self._start_time)
        
        else:
            return self._accumulated_time
        
    def stop(self):
        if self._start_time is None:
            return self._total

        if self._is_running:
            self._total = (self._accumulated_time + (timestamp() - self._start_time))
        
        elif self._is_paused:
            self._total = self._accumulated_time
        
        self._is_finished = True
        self._start_time = None
        self._accumulated_time = timedelta(0)
        self._is_paused = False
        self._is_running = False
        
        return self._total
    
    def is_started(self):
        if self._start_time is not None:
            return True
        
        return False

    def is_running(self):
        return self._is_running
    
    def is_paused(self):
        return self._is_paused
    
    @property
    def is_finished(self):
        return self._is_finished
    
    @is_finished.setter
    def is_finished(self, value):
        self._is_finished = value

    def receive_study_title(self, title):
        self._current_study_title = title
        return self._current_study_title
    
    def get_study_title(self):
        return self._current_study_title

        