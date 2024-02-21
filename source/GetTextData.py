
import GetSource

def test(url):
    r = GetSource.get_source_text(url)
    print(r[0], r[1])
    return r