'''
This is a utils library
'''

class utils:
    def __init__(self):
        pass


    def find_max(self, list):
        '''
        This is to return the largest number of a given list
        '''
        list_max = list[0]
        for item in list:
            if list_max < item:
                list_max = item

        return list_max

