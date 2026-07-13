#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import contextlib
import io

with atheris.instrument_imports():
    import astpretty
    import ast

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = io.StringIO()
    yield
    sys.stdout = save_stdout

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with nostdout():
            astpretty.pprint(ast.parse(fdp.ConsumeRemainingString()))
            astpretty.pformat(ast.parse(fdp.ConsumeRemainingString()))
    except (IndentationError, ValueError, SyntaxError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
