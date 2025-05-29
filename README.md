[![Downloads](https://static.pepy.tech/badge/suby/month)](https://pepy.tech/project/suby)
[![Downloads](https://static.pepy.tech/badge/suby)](https://pepy.tech/project/suby)
[![Test-Package](https://github.com/pomponchik/suby/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/suby/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/suby.svg)](https://pypi.python.org/pypi/suby)
[![PyPI version](https://badge.fury.io/py/suby.svg)](https://badge.fury.io/py/suby)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


# oslex

`oslex` is an OS-independent wrapper for [`shlex`](https://docs.python.org/3/library/shlex.html) and [`mslex`](https://pypi.org/project/mslex/).

Its main purpose is to provide functions similar in functionality to `shlex.quote()`, `shlex.split()` and `shlex.join()` on both Windows and POSIX-compatible platforms.

This goal is achieved by simply forwarding the calls to either `shlex` (from the standard library) on POSIX-compatible systems, or the excellent `mslex` library (written by Lawrence D'Anna / @smoofra) on Windows.

In other words, `oslex` is to `shlex`/`mslex` what `os-path` is to `posixpath`/`ntpath`.

## Licensing

This library itself is licensed under the MIT license.

`oslex` uses the [`mslex`](https://pypi.org/project/mslex/) library, which is distributed under the Apache 2.0 license.
