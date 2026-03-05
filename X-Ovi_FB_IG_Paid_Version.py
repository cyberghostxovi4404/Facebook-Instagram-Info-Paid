#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import getpass
import requests
from bs4 import BeautifulSoup

# Instagram
try:
    import instaloader
    INSTAGRAM_AVAILABLE = True
except ImportError:
    INSTAGRAM_AVAILABLE = False

# Facebook (scraper)
try:
    from facebook_scraper import get_profile, get_posts
    FACEBOOK_SCRAPER_AVAILABLE = True
except ImportError:
    FACEBOOK_SCRAPER_AVAILABLE = False

PASSWORD = "cyberghostxovi"
MAX_ATTEMPTS = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code="0", end="\n"):
    print(f"\033[{color_code}m{text}\033[0m", end=end)

def banner():
    clear_screen()
    print("""
\033[1;31m
                ........
              .::::::::::.
             .::'      '::.
             ::          ::
             ::          ::
             ::   .  .   ::
             '::.  ..  .::'
              '::::::::::'
            .::::::::::::::.
          .::::::::::::::::::.
         ::::::::::::::::::::::
        ::::::::::::::::::::::::
\033[1;36m  +===============================================+
\033[1;97m     __   __           ____  _      _ _ 
\033[1;97m     \\ \\ / /          / __ \\| |    | | |
\033[1;31m      \\ V /  ______  | |  | \\ \\  / /| |
\033[1;31m       > <  |______| | |  | |\\ \\/ / | |
\033[1;36m      / . \\          | |__| | \\  /  | |
\033[1;36m     /_/ \\_\\          \\____/   \\/   |_|
\033[1;36m  +===============================================+
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mCEO    \033[1;31m: \033[1;91mOVI (CYBER GHOST X)
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mTEAM   \033[1;31m: \033[1;97mCYBER GHOST X OVI
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mTOOL   \033[1;31m: \033[1;92mFacebook Instagram Info (Login Fixed)
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mSTATUS \033[1;31m: \033[1;93mPAID ACCESS GRANTED
\033[1;36m  +===============================================+\033[0m
""")

def authenticate():
    print_colored("[!] This tool is protected. Enter password:", "1;33")
    for attempt in range(MAX_ATTEMPTS, 0, -1):
        pwd = getpass.getpass("\033[36mPassword: \033[0m")
        if pwd == PASSWORD:
            print_colored("[✓] Access Granted!", "1;32")
            time.sleep(1)
            return True
        else:
            print_colored(f"[✗] Wrong password! {attempt-1} attempts left." if attempt>1 else "[✗] Too many failures. Exiting.", "1;31")
            if attempt == 1:
                sys.exit(1)
    return False

# ----------------- Instagram Functions -----------------
def instagram_profile_info(username):
    print_colored("\n[ Instagram Profile Information ]\n", "1;33")
    if not INSTAGRAM_AVAILABLE:
        print_colored("Instaloader not installed. Install: pip install instaloader", "1;31")
        return

    L = instaloader.Instaloader()
    # Optional login to avoid rate limits
    login_choice = input("Login to Instagram? (y/n, default n): ").strip().lower()
    if login_choice == 'y':
        ig_user = input("Instagram username: ").strip()
        ig_pass = getpass.getpass("Instagram password: ")
        try:
            L.login(ig_user, ig_pass)
            print_colored("Login successful! Rate limits reduced.", "1;32")
        except Exception as e:
            print_colored(f"Login failed: {e}. Continuing anonymously.", "1;33")

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        print_colored(f"Username: {profile.username}", "1;32")
        print_colored(f"Full Name: {profile.full_name}", "1;32")
        print_colored(f"ID: {profile.userid}", "1;32")
        print_colored(f"Bio: {profile.biography}", "1;32")
        print_colored(f"Followers: {profile.followers}", "1;32")
        print_colored(f"Following: {profile.followees}", "1;32")
        print_colored(f"Posts: {profile.mediacount}", "1;32")
        print_colored(f"Private: {profile.is_private}", "1;32")
        print_colored(f"Verified: {profile.is_verified}", "1;32")
        print_colored(f"Profile Pic: {profile.profile_pic_url}", "1;32")
    except instaloader.exceptions.ProfileNotExistsException:
        print_colored("Profile does not exist.", "1;31")
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

def instagram_post_info(username, limit=10):
    print_colored(f"\n[ Last {limit} Instagram Posts ]\n", "1;33")
    if not INSTAGRAM_AVAILABLE:
        print_colored("Instaloader not installed.", "1;31")
        return

    L = instaloader.Instaloader()
    login_choice = input("Login to Instagram? (y/n, default n): ").strip().lower()
    if login_choice == 'y':
        ig_user = input("Instagram username: ").strip()
        ig_pass = getpass.getpass("Instagram password: ")
        try:
            L.login(ig_user, ig_pass)
            print_colored("Login successful!", "1;32")
        except Exception as e:
            print_colored(f"Login failed: {e}. Continuing anonymously.", "1;33")

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        for i, post in enumerate(posts, 1):
            if i > limit:
                break
            print_colored(f"POST {i}", "1;41")
            print(f"Date: {post.date.strftime('%Y-%m-%d %I:%M %p')}")
            print(f"Caption: {post.caption if post.caption else 'No caption'}")
            print(f"URL: \033[32m{post.url}\033[0m")
            print("-"*50)
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

def instagram_download_posts(username):
    print_colored("\n[ Downloading Instagram Posts ]\n", "1;33")
    if not INSTAGRAM_AVAILABLE:
        print_colored("Instaloader not installed.", "1;31")
        return

    L = instaloader.Instaloader()
    login_choice = input("Login to Instagram? (y/n, default n): ").strip().lower()
    if login_choice == 'y':
        ig_user = input("Instagram username: ").strip()
        ig_pass = getpass.getpass("Instagram password: ")
        try:
            L.login(ig_user, ig_pass)
            print_colored("Login successful!", "1;32")
        except Exception as e:
            print_colored(f"Login failed: {e}. Continuing anonymously.", "1;33")

    download_path = os.path.join("/sdcard", f"IG_{username}")
    os.makedirs(download_path, exist_ok=True)

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        count = 0
        for post in posts:
            L.download_post(post, target=download_path)
            count += 1
            print_colored(f"Downloaded post {count}", "1;32")
        print_colored(f"\n✅ Downloaded {count} posts to {download_path}", "1;32")
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

# ----------------- Facebook Functions -----------------
def facebook_simple_info(profile_id):
    """Fallback: fetch name and profile pic using requests."""
    url = f"https://www.facebook.com/{profile_id}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code != 200:
            return None, f"HTTP {r.status_code}"
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.find("title")
        name = title.text.replace("Facebook", "").strip() if title else "N/A"
        og_image = soup.find("meta", property="og:image")
        pic = og_image["content"] if og_image else "N/A"
        return {"name": name, "profile_pic": pic}, None
    except Exception as e:
        return None, str(e)

def facebook_profile_info(identifier):
    print_colored("\n[ Facebook Profile Information ]\n", "1;33")

    # Try using facebook-scraper if available
    if FACEBOOK_SCRAPER_AVAILABLE:
        try:
            profile = get_profile(identifier)
            if profile:
                for key in ["Name", "Username", "id", "Followers", "About"]:
                    val = profile.get(key, "N/A")
                    if val:
                        print_colored(f"{key}: {val}", "1;32")
                return
            else:
                print_colored("facebook-scraper returned empty.", "1;33")
        except Exception as e:
            print_colored(f"facebook-scraper error: {e}", "1;33")
            print_colored("Trying fallback method...", "1;33")
    else:
        print_colored("facebook-scraper not installed. Using fallback.", "1;33")

    # Fallback: simple name & picture
    info, err = facebook_simple_info(identifier)
    if info:
        print_colored(f"Name: {info['name']}", "1;32")
        print_colored(f"Profile Picture URL: {info['profile_pic']}", "1;32")
        print_colored("\n[!] Only basic info available via fallback.", "1;33")
    else:
        print_colored(f"Fallback also failed: {err}", "1;31")

def facebook_post_info(identifier, limit=10):
    print_colored(f"\n[ Last {limit} Facebook Posts (if available) ]\n", "1;33")
    if not FACEBOOK_SCRAPER_AVAILABLE:
        print_colored("facebook-scraper not installed. Cannot fetch posts.", "1;31")
        return
    try:
        posts = get_posts(identifier, pages=2)
        for i, post in enumerate(posts, 1):
            if i > limit: break
            print_colored(f"POST {i}", "1;41")
            print(f"Time: {post.get('time', 'N/A')}")
            print(f"Text: {post.get('text', 'N/A')[:200]}...")
            print(f"URL: \033[32m{post.get('post_url', 'N/A')}\033[0m")
            print("-"*50)
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

def open_help():
    os.system("termux-open-url https://www.facebook.com/cyberghostxovihackeroffpower")
    print_colored("Help page opened.", "1;32")

# ----------------- Menu -----------------
def options_menu(ig_username):
    while True:
        clear_screen()
        banner()
        print_colored(f"\nCurrent Instagram username: \033[37m{ig_username}\033[0m\n", "1;36")
        print("  \033[1;33m[1]\033[0m \033[1;32mInstagram Profile Information\033[0m")
        print("  \033[1;33m[2]\033[0m \033[1;32mInstagram Post Information (last 10)\033[0m")
        print("  \033[1;33m[3]\033[0m \033[1;32mDownload all Instagram posts\033[0m")
        print("  \033[1;33m[4]\033[0m \033[1;32mFacebook Profile Information\033[0m")
        print("  \033[1;33m[5]\033[0m \033[1;32mFacebook Post Information\033[0m")
        print("  \033[1;33m[6]\033[0m \033[1;32mChange Instagram Username\033[0m")
        print("  \033[1;33m[7]\033[0m \033[1;32mGet Help\033[0m")
        print("  \033[1;33m[8]\033[0m \033[1;32mExit\033[0m")
        choice = input("\n\033[36mEnter your choice: \033[0m").strip()

        if choice == "1":
            instagram_profile_info(ig_username)
        elif choice == "2":
            instagram_post_info(ig_username)
        elif choice == "3":
            instagram_download_posts(ig_username)
        elif choice == "4":
            fb_id = input("Enter Facebook username or profile ID: ").strip()
            facebook_profile_info(fb_id)
        elif choice == "5":
            fb_id = input("Enter Facebook username or profile ID: ").strip()
            facebook_post_info(fb_id)
        elif choice == "6":
            new_ig = input("Enter new Instagram username: ").strip()
            if new_ig:
                ig_username = new_ig
                print_colored("Username changed.", "1;32")
        elif choice == "7":
            open_help()
        elif choice == "8":
            print_colored("Exiting...", "1;31")
            sys.exit()
        else:
            print_colored("Invalid choice!", "1;31")

        input("\n\033[36mPress Enter to continue...\033[0m")

def main():
    clear_screen()
    if not INSTAGRAM_AVAILABLE:
        print_colored("[!] Instaloader not installed. Install: pip install instaloader", "1;31")
        sys.exit(1)

    authenticate()
    clear_screen()
    banner()
    ig_user = input("\nEnter Instagram username: ").strip()
    if not ig_user:
        print_colored("No username entered.", "1;31")
        sys.exit(1)
    options_menu(ig_user)

if __name__ == "__main__":
    main()
