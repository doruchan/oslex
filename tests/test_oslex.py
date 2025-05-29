from oslex import split, quote

pretty_examples = [
    (r"c:\Program Files\FooBar", r'"c:\Program Files\FooBar"'),
    (r"c:\Program Files (x86)\FooBar", r'"c:\Program Files (x86)\FooBar"'),
    ("^", "^^"),
    (" ^", '" ^"'),
    ("&", "^&"),
    ("!", "^!"),
    (r"%foo%", r"^%foo^%"),
    ("!foo!", "^!foo^!"),
    ("foo bar!", '"foo bar"^!'),
    ("!foo bar!", '^!"foo bar"^!'),
    ("foo\\bar\\baz\\", "foo\\bar\\baz\\"),
    ("foo bar\\baz\\", '"foo bar\\baz\\\\"'),
    ("foo () bar\\baz\\", '"foo () bar\\baz\\\\"'),
    ("foo () bar\\baz\\\\", '"foo () bar\\baz\\\\\\\\"'),
    ("foo () bar\\baz\\\\\\", '"foo () bar\\baz\\\\\\\\\\\\"'),
    ("foo () bar\\baz\\\\\\\\", '"foo () bar\\baz\\\\\\\\\\\\\\\\"'),
    (r"foo\bar! baz", r'foo\bar^!" baz"'),
    (r"x\!", r"x\^!"),
    ("foo\\", "foo\\"),
    ("\\", "\\"),
]


def test_pretty_examples():
    for s, ans in pretty_examples:
        assert quote(s) == ans
        assert split(ans) == [s]
        assert split(ans + " " + ans + " foo bar") == [s, s, "foo", "bar"]
