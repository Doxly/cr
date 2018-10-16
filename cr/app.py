#!/usr/bin/env python
# -- encoding:utf-8 --

''' Template for new application'''

from pva_tools.pva_application import PvaApplication


class MyApplication(PvaApplication):
    """docstring for MyApplication"""

    # dictionary for defaults values
    defaults = {
    }

    def __init__(self):
        super(MyApplication, self).__init__()

    def get_args(self, parameters=None, add_to_config=False):
        ''' Write some code for additional command-line parameters'''
        parser = self.get_argparser()
        parser.description = 'Some description visible when -h is set'
        # . . .
        self.args = parser.parse_args(parameters)
        if add_to_config:
            self.arg_to_config()

    def process(self):
        '''Make some activity acording to given commands'''
        # call parent methon for show_config and save_config parameters
        PvaApplication.process(self)
        # You code ...

def main():
    '''Main function of application. Executed if called from command line.'''
    app = MyApplication()
    app.get_args(add_to_config=True)
    app.process()
    print('done!')

if __name__ == '__main__':
    main()
