import *
#class wc_business(object):
class wc_business:
    def __init__(self, name, business_description):
        self.name = name
        self.about_business = ''
        self.business_description = []

    def __repr__(self):
        return 'Businesses: ' + name + ', '.join(description for description in self.business_description)
