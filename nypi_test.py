from nypi import get_pkg


def test_nypi():
    p = get_pkg("pytest")
    assert p.latest.spec == "pytest==6.2.5"
