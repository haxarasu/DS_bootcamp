import os
import subprocess
import sys


def check_env(expected_venv_name="salvados"):
    venv = os.getenv('VIRTUAL_ENV')
    if venv:
        venv_name = os.path.basename(venv)
        return venv_name == expected_venv_name
    return False


def install_package(requirements_file="libs_names.txt"):
    try:
        if check_env() == True:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        else:
            raise ValueError("The virtual environment is not active or does not match the expected one.")
    except Exception as e:
        raise RuntimeError(f"Error while installing packages: {e}")


def save_installed_packages():
    result = subprocess.run([sys.executable, "-m", "pip", "list"], capture_output=True, text=True)
    if result.returncode == 0:
        with open("requirements.txt", "w") as file:
            file.write(result.stdout)
    else:
        print("Failed to retrieve installed packages")

if __name__ == "__main__":
    install_package()
    save_installed_packages()
