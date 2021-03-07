'''instaloader_chrome_cookie.py
Works only on Linux and Darwin.

If not using Chromium, specify cookie file using the -c option.
For example for Brave Browser do this:
python instaloader_chrome_cookie.py -c ~/.config/BraveSoftware/Brave-Browser/Default/Cookies

Optionally specify the instaloader session file using the -f option.
'''

from argparse import ArgumentParser
from pycookiecheat import chrome_cookies
from instaloader import Instaloader

url = 'https://instagram.com'

def import_session(cookiefile, sessionfile):
    if cookiefile:
        cookie_data = chrome_cookies(url, cookie_file=cookiefile)
    else:
        cookie_data = chrome_cookies(url)
    # print(cookie_data)

    instaloader = Instaloader(max_connection_attempts=1)
    instaloader.context._session.cookies.update(cookie_data)

    username = instaloader.test_login()
    if not username:
        raise SystemExit("Not logged in. Are you logged in successfully?")

    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(sessionfile)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-c", "--cookiefile")
    p.add_argument("-f", "--sessionfile")
    args = p.parse_args()
    try:
        import_session(args.cookiefile, args.sessionfile)
    except Exception as e:
        raise SystemExit("Cookie import failed: {}".format(e))
