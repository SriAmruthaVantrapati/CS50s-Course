from twttr import shorten
def main():
    test_twttr()
def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") =="HLL"
    assert shorten("hello, WORLD")=="hll, WRLD"
    assert shorten("23")=="23"
    assert shorten("cs50")=="cs50"
    assert shorten("hello, WORLD")=="hll, WRLD"
    assert shorten(",._-")==",._-"
if __name__ =="__main__":
    main()
