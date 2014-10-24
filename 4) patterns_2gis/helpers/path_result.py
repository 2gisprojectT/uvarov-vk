__author__ = 'admin'

from helpers.base_component import BaseComponent


class PathResult(BaseComponent):

    selectors = {
        'self': 'module-1-9-1',
        'route_steps': '.routeResults__steps',
    }

    #@property
    def isFound(self):
        if self.driver.find_elements_by_css_selector(self.selectors['route_steps']):
            return True
        else:
            return False

    def foundSteps(self):
        return self.driver.find_elements_by_css_selector(self.selectors['route_steps'])