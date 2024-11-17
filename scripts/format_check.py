import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.dirname(current_dir)

if __name__ == "__main__":
    all_params = sys.argv[1:]

    path: str = f"{base_dir}/project/"
    if all_params:
        path: str = all_params[0]

    os.system(f"pylint {path}")
