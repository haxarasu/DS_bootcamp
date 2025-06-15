import os

def get_venv_name():
    venv_path = os.getenv('VIRTUAL_ENV')

    if venv_path:
        print(f'Your current virtual env is {venv_path}')
    else:
        print('No virtual env is active')
    

if __name__ == '__main__':
    get_venv_name()