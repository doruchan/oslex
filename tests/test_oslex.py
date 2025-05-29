import pytest
import oslex


split_cases = [
    # input_str, expected_posix, expected windows
    r'"c:\Program Files\FooBar"',
    r'"c:\Program Files (x86)\FooBar"',
    "^^",
    '" ^"',
    "^&",
    "^!",
    r"^%foo^%",
    "^!foo^!",
    "foo bar^!",
    "^!foo bar^!",
    "foo\\bar\\baz\\",
    "foo bar\\baz\\\\",
    '"foo () bar\\baz\\\\"',
    '"foo () bar\\baz\\\\\\"',
     r"foo\bar^! baz",
]

quote_cases = (
    "^",
    " ^",
    "&",
    "!",
    r"%",
    "!foo!",
    "'",
    '"',
    "?",
    "word with spaces",
    r"x\!", "'x\\!'", 'x\\^!'
)



@pytest.mark.parametrize("input_str", quote_cases)
def test_quote(input_str):
    assert oslex.quote(input_str) == oslex.underlying.quote(input_str)


@pytest.mark.parametrize("input_str", quote_cases)
@pytest.mark.parametrize("for_cmd", [True, False])
def test_quote_kwargs_win(input_str, for_cmd):
    if not oslex.is_windows():
        return
    kwargs = {"for_cmd": for_cmd}
    assert oslex.quote(input_str, **kwargs) == oslex.underlying.quote(input_str, **kwargs)


@pytest.mark.parametrize("input_str", split_cases)
def test_split(input_str):
    assert oslex.split(input_str) == oslex.underlying.split(input_str)


@pytest.mark.parametrize("input_str", split_cases)
@pytest.mark.parametrize("like_cmd", [True, False])
@pytest.mark.parametrize("check", [True, False])
@pytest.mark.parametrize("ucrt", [True, False])
def test_split_kwargs_win(input_str, like_cmd, check, ucrt):
    if not oslex.is_windows():
        return
    kwargs = {
        "like_cmd": like_cmd,
        "check": check,
        "ucrt": ucrt,
    }
    assert oslex.split(input_str, **kwargs) == oslex.underlying.split(input_str, **kwargs)

@pytest.mark.parametrize("input_str", split_cases)
@pytest.mark.parametrize("comments", [True, False])
@pytest.mark.parametrize("posix", [True, False])
def test_split_kwargs_posix(input_str, comments, posix):
    if not oslex.is_posix():
        return
    kwargs = {
        "comments": comments,
        "posix": posix,
    }
    assert oslex.split(input_str, **kwargs) == oslex.underlying.split(input_str, **kwargs)


@pytest.mark.parametrize("input_str", split_cases)
def test_join(input_str):
    assert oslex.join(input_str) == oslex.underlying.join(input_str)


@pytest.mark.parametrize("input_str", split_cases)
@pytest.mark.parametrize("for_cmd", [True, False])
def test_join_kwargs_win(input_str, for_cmd):
    if not oslex.is_windows():
        return
    kwargs = {"for_cmd": for_cmd}
    assert oslex.join(input_str, **kwargs) == oslex.underlying.join(input_str, **kwargs)
