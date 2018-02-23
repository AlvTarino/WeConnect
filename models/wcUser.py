import sys
class wcUser:
    def __init__(self):
        self.business = {}

    def create_business(self, name, *business_description):#creates business and allows users to add a description to the business
        business_description = list(business_description)
        if name not in self.business.keys():
            self.business[name] = [description for description in business_description]
        elif name in self.business.keys():
            return 'Business already exists!'
        return self.business

    def read_business(self, name):#Returns business_description from a specified business
        business_description = []
        if name in self.business.keys():
            business_description = [description for description in self.business[name]]
        return business_description

    def update_business(self, business_name, new_name):
        #creates business name
        if business_name in self.business.keys():
            self.business[new_name] = self.business.pop(business_name)
        else:
            return "Business name does not exist here"
        return self.business

    def update_business_description(self, business_name, description_heading, new_description):#creates new business-description
        if business_name in self.business.keys():
            for description in self.business[business_name]:
                if description == description_heading:
                    self.business[business_name].remove(description)
                    self.business[business_name].append(new_description)
                else:
                    return 'Business description unavailable'
        else:
            return "Business has not yet been created"
        return self.business

    def delete_business(self, business_name): #deletes a selected business
        if business_name in self.business.keys():
            del self.business[business_name]
        else:
            return 'Business not available'
        return self.business

    def add_business_description(self, business_name, *business_description):#adds on the already existing business_description
        business_description = list(business_description)
        if business_name in self.business.keys():
            for description in business_description:
                if description not in self.business[business_name]:
                    self.business[business_name].append(description)
        else:
            if business_name not in self.business:
                for description in business_description:
                    self.business[business_name] = [description for description in business_description]

    def delete_business_description(self, business_name, description):#deletes  the business description
        if description in self.business[business_name]:
            self.business[business_name].remove(description)
        else:
            return 'description not in business'
        return self.business

    def __repr__(self):
        return 'user businesss are: ' + ', '.join(name for name in self.business)
