#-*-coding:utf-8 -*-
import configparser
import signal

PROJECTS_CONFIG = "projects.ini"


class Parser():
    def __init__(self):
        pass

    @staticmethod
    def load():

        config = configparser.ConfigParser()
        config.read(PROJECTS_CONFIG)
        for section in config.sections():
            value = config.get(section, 'name')  # -> "Python is fun!"
            Projects.add_projects({section: value})


class Projects():

    PROJECTS = {
        # "001": "维权",
    }
    project_id_next = 1

    def __init__(self):
        pass

    def get_project_id(self):
        ret = self.project_id_next
        self.project_id_next += 1
        return ret

    @classmethod
    def add_projects(cls, project):
        cls.PROJECTS.update(project)

# 捕捉异常信号
class ExceptSignalHandle():
    SIGUSR1 = 30
    signal_handlers = None
    @classmethod
    def collect_handlers(cls):
        cls.signal_handlers = [
            {
                "signal": cls.SIGUSR1, 
                "handler": cls.handle_reload_project
            },
            # {
            #     "signal": SIGUSR1, 
            #     "handler": handle_reload_project
            # },
        ]    
    @classmethod
    def handle_reload_project(cls, sig, frame):
        Parser.load()
        print("{0} {1}".format(sig, frame))
        signal.signal(cls.SIGUSR1, cls.handle_reload_project)

    @classmethod
    def handle_signal(cls):
        cls.collect_handlers()
        for except_handle in cls.signal_handlers:
            except_handle["handler"](except_handle["signal"], None)

ExceptSignalHandle.handle_signal()

if __name__ == "__main__":
    import time
    while True:
        time.sleep()