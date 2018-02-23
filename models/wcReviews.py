import sys
class review:
    def __init__(self, name):
        self.name = name
        self.status = False
        self.business_description = []

    def __repr__(self):
        return 'Your reviews: ' + ', ' .join(description for description in self.business_description)
