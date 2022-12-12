import argparse
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        with open(filename, "rb") as f:
            for line in f.readlines():
                if line.contains("getLogger()"):
                    print(
                        f"{filename}: getLogger() called without name, call getLogger(__name__) instead"
                    )
                    retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
