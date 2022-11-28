#!/usr/bin/env python3

'''instaloader_chrome_cookie.py
Works only on Linux and Darwin.

If not using Chromium, specify cookie file using the -c option.
If your browser is using GNOME Keyring or KWallet you will need to specify the password using the -p flag.

For example for Brave Browser do this:
./instaloader_chrome_cookie.py -c ~/.config/BraveSoftware/Brave-Browser/Default/Cookies -p [password]

Optionally specify the instaloader session file using the -f option.
'''

from argparse import ArgumentParser
from pycookiecheat import chrome_cookies
from instaloader import Instaloader

url = 'https://instagram.com'

def import_session(cookiefile, sessionfile, password):
    if cookiefile:
        if password:
            try:
                cookie_data = chrome_cookies(url, cookie_file=cookiefile, password=password)
            except:
                raise SystemError("The password you specified is probably wrong.")
        else:
            try:
                cookie_data = chrome_cookies(url, cookie_file=cookiefile)
            except:
                raise SystemError("Maybe you need to specify password.")
    else:
        if password:
            cookie_data = chrome_cookies(url, password=password)
        else:
            cookie_data = chrome_cookies(url) 

    instaloader = Instaloader(max_connection_attempts=1)
    instaloader.context._session.cookies.update(cookie_data)

    username = instaloader.test_login()
    if not username:
        raise SystemError("Not logged in. Are you logged in successfully?")

    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(sessionfile)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-c", "--cookiefile")
    p.add_argument("-f", "--sessionfile")
    p.add_argument("-p", "--password")
    args = p.parse_args()
    try:
        import_session(args.cookiefile, args.sessionfile, args.password)
    except Exception as e:
        raise SystemExit("Cookie import failed: {}".format(e))
