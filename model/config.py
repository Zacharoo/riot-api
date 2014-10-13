import sys

def get_mode():
    mode = sys.environ['MODE']
    if mode == 'DEV' or mode == 'INTEGRATION' or mode == 'PRODUCTION':
        return mode
    return 'TEST'
