import win32process, win32gui, psutil, mouse


class WindowMonitor:
    def __init__ (self):
        self.study_apps = ["Code.exe", "firefox.exe", "pythonw.exe"]
        self.last_process = None
        self.running = None
    
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
            print(current_process)
            
 
monitor = WindowMonitor()

monitor.run()