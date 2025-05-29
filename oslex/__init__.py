"""
oslex module
"""
import sys
from typing import List, Optional


def is_posix() -> bool:
    """
    Returns whether the system running Python is POSIX compatible.
    This is the condition for oslex.underlying being shlex.
    This is also the condition for os.path being posixpath.
    """
    return 'posix' in sys.builtin_module_names


def is_windows() -> bool:
    """
    Returns whether the system running Python is Windows based.
    This is the condition for oslex.underlying being mslex.
    This is also the condition for os.path being ntpath.
    """

    if is_posix():
        # This early return is likely redundant, but we want to be 100% 
        # equivalent to the if-elseif structure found in os.py
        # See https://github.com/python/cpython/blob/3.7/Lib/os.py
        return False

    return 'nt' in sys.builtin_module_names


# Import OS-specific module

if is_posix():
    import shlex as underlying
elif is_windows():
    # mypy does not understand conditional importing, so it thinks 
    # we are redefining the name "underlying" -> we have to ignore the "no-redef" error
    import mslex as underlying  # type: ignore[no-redef]
else:
    raise ImportError('no os specific module found')

# Define functions


def quote(s: str,
          # windows arguments
          for_cmd: Optional[bool] = None) -> str:
    """
    Return a shell-escaped version of the string s.
    The returned value is a string that can safely be used
    as one token in a shell command line, for cases where you cannot use a list.
    This function is safe to use both for POSIX-compatible shells and for Windows's cmd.
    """
    if is_windows():
        kwargs = dict(for_cmd=for_cmd)
    else:
        kwargs = {}
    return underlying.quote(s, **kwargs)


def split(s: str,
          # posix arguments
          comments: Optional[bool] = None, posix : Optional[bool] = None,
          # windows arguments
          like_cmd: Optional[bool] = None, check: Optional[bool] = None,
          ucrt: Optional[bool] = None) -> List[str]:
    """
    Split the string s using shell-like syntax.
    This function is safe to use both for POSIX-compatible shells 
    and for Windows's cmd.
    """
    if is_windows():
        kwargs = dict(
            like_cmd=like_cmd,
            check=check,
            ucrt=ucrt,
        )
    else:
        kwargs = dict(
            comments=comments,
            posix=posix,
        )
    return underlying.split(s, **kwargs)


def join(split_command: List[str],
         # windows arguments
         for_cmd: Optional[bool] = None) -> str:
    """
    Concatenate the tokens of the list split_command and return a string. 
    This function is the inverse of split().
    The returned value is shell-escaped to protect against injection 
    vulnerabilities (see quote()).
    This function is safe to use both for POSIX-compatible shells and 
    for Windows's cmd.
    """
    if is_windows():
        kwargs = dict(for_cmd=for_cmd)
    else:
        kwargs = {}
    return underlying.join(split_command, **kwargs)
