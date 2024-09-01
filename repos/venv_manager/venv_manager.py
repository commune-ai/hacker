
import os
import subprocess
import venv
import shutil

class VenvManager:
    def __init__(self, base_path=os.path.expanduser("~/.venvs")):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def create_venv(self, name):
        venv_path = os.path.join(self.base_path, name)
        if os.path.exists(venv_path):
            print(f"Virtual environment '{name}' already exists.")
            return
        venv.create(venv_path, with_pip=True)
        print(f"Created virtual environment: {name}")

    def activate_venv(self, name):
        venv_path = os.path.join(self.base_path, name)
        if not os.path.exists(venv_path):
            print(f"Virtual environment '{name}' does not exist.")
            return
        activate_script = os.path.join(venv_path, "bin", "activate")
        print(f"To activate the virtual environment, run:")
        print(f"source {activate_script}")

    def deactivate_venv(self):
        if "VIRTUAL_ENV" in os.environ:
            print("To deactivate the current virtual environment, run:")
            print("deactivate")
        else:
            print("No active virtual environment detected.")

    def remove_venv(self, name):
        venv_path = os.path.join(self.base_path, name)
        if not os.path.exists(venv_path):
            print(f"Virtual environment '{name}' does not exist.")
            return
        shutil.rmtree(venv_path)
        print(f"Removed virtual environment: {name}")

    def list_venvs(self):
        venvs = [d for d in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, d))]
        if venvs:
            print("Available virtual environments:")
            for venv in venvs:
                print(f"- {venv}")
        else:
            print("No virtual environments found.")

if __name__ == "__main__":
    manager = VenvManager()
    
    # Example usage
    manager.create_venv("test_env")
    manager.list_venvs()
    manager.activate_venv("test_env")
    manager.deactivate_venv()
    manager.remove_venv("test_env")
    manager.list_venvs()
