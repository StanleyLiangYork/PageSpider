from utilities.url_utilities import load_urls_from_file

def test_load_file():
    """
    test the load_urls_from file() method and check if the read string is longer than one char
    """

    test_urls = load_urls_from_file("/Users/zhaohuiliang/PycharmProjects/PageSpider/input.txt")
    assert (len(test_urls) > 1)
