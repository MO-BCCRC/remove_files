'''
Created on Apr 1 2015

@author: dgrewal
'''

import argparse

__version__ = '1.0.0'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='remove_files',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This component removes the input files''')

# required arguments
parser.add_argument('--input',
                    nargs = '*',
                    help='input file. (will be delted by the component)')

parser.add_argument('--run_component',
                    default = False,
                    action= 'store_true',
                    help='flag to turn the component ON/OFF')

args, x = parser.parse_known_args()
