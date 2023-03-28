from pathlib import Path

from easy import easy
from hard import hard
from medium import medium

output_dirs = [
    Path('artifacts/')
]

if __name__ == '__main__':
    for dir in output_dirs:
        dir.mkdir(exist_ok=True, parents=True)

    easy()
    medium()
    hard()