"""Run an extracted appendix listing with the Appendix A routines loaded.

The extracted listings are kept unchanged. This runner supplies the shared
namespace that the paper has implicitly across appendix code blocks.
"""

from pathlib import Path
import argparse


APPENDIX_A_FILES = (
    "appendix_a/01_core_dyck_sequence_routines.py",
    "appendix_a/02_make_strings.py",
)


def exec_file(path, namespace):
    source = path.read_text(encoding="ascii")
    exec(compile(source, str(path), "exec"), namespace)


def main():
    parser = argparse.ArgumentParser(description="Run an extracted appendix listing.")
    parser.add_argument("listing", help="path to the listing, relative to code/")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    namespace = {"__name__": "__main__"}
    for relative_path in APPENDIX_A_FILES:
        exec_file(here / relative_path, namespace)
    exec_file(here / args.listing, namespace)


if __name__ == "__main__":
    main()
