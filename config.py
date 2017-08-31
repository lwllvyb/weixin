#-*-coding:utf-8 -*-
import configparser
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

Parser.load()