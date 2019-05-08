import requests, lxml.html, sys, time


def platform_manager():
    platform = []
    if sys.platform == "win32":
        platform.append("win64")
        platform.append(".exe")
    elif sys.platform == "linux2":
        platform.append("linux64")
        platform.append(".tar.gz")
    elif sys.platform == "darwin":
        platform.append("osx")
        platform.append(".dmg")
    return platform


def ff_url(session, platform):
    '''
    Returns a link to the Firefox English (US) download
    '''

    link = ""

    r = session.get("https://www.mozilla.org/en-US/firefox/all/")
    body = lxml.html.fromstring(r.content)
    
    xpath_ls = body.xpath(f"//a[@href='https://download.mozilla.org/?product=firefox-latest-ssl&os={str(platform[0])}&lang=en-US'][contains(.,'Download')]")
    for element in xpath_ls:
        full_tag = lxml.html.tostring(element, encoding="unicode")
        attr = full_tag.split(" ")
        href = attr[1].replace("href=", "")
        link = href.replace('\"', "")
    return link


def ff_download(session, link, platform):
    '''
    Download the latest file for the platform
    '''
    r = s.get(link, stream=True)
    with open(f"latest_firefox{str(platform[1])}", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    

if __name__ == '__main__':
    start_time = time.time()
    with requests.Session() as s:
        ff_download(s, ff_url(s, platform_manager()), platform_manager())
    end_time = time.time() - start_time
    print(f"Total time: {end_time}")
    