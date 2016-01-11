'''
Created on Apr 1,2015
@author: dgrewal
'''

import os

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    remove a file or a list of files
    '''
    def __init__(self, component_name='remove_files', component_parent_dir=None, seed_dir=None):
       self.version = "1.0.0"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        if not self.args.run_component:
            cmd = 'exit 0'
            cmd_args = []
            return cmd, cmd_args

        if type(self.args.input) is list:
            self.args.input = [val+self.args.postfix for val in self.args.input]
            cmd = 'rm -rf '+ ' '.join(self.args.input)
        else:
            cmd = 'rm -rf '+ self.args.input+self.args.postfix

        cmd_args = []

        return cmd, cmd_args

# to run as stand alone
def _main():
    '''main function'''
    remove_files = Component()
    remove_files.args = component_ui.args
    remove_files.run()

if __name__ == '__main__':

    import component_ui

    _main()
