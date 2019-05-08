import requests, lxml.html, sys, time

def ff_url(session):
    '''
    Returns a link to the Firefox English (US) download for windows
    '''
    link = []
    platform = ""
    r = session.get("https://www.mozilla.org/en-US/firefox/all/")
    body = lxml.html.fromstring(r.content)
    if sys.platform == "win32":
        platform = "win64"
    elif sys.platform == "linux2":
        platform = "linux64"
    elif sys.platform == "darwin":
        platform = "osx"
    xpath_ls = body.xpath(f"//a[@href='https://download.mozilla.org/?product=firefox-latest-ssl&os={platform}&lang=en-US'][contains(.,'Download')]")
    for element in xpath_ls:
        full_tag = lxml.html.tostring(element, encoding="unicode")
        attr = full_tag.split(" ")
        href = attr[1].replace("href=", "")
        text = href.replace('\"', "")
        link.append(text)
    return link


if __name__ == '__main__':
    with requests.Session() as s:
        ff_url(s)