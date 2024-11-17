import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.dirname(current_dir)

if __name__ == "__main__":
    all_params = sys.argv[1:]

    # If a path is given, run isort and black on that path only
    path: str = base_dir
    if all_params:
        path = all_params[0]

    print("path is: ", path)
    os.system(f"isort {path} --multi-line=3 --profile=black --skip env")
    os.system(f"black {path} --exclude '/env/'")
