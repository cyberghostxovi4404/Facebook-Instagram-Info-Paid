#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facebook & Instagram Information Tool
Author: OVI (CYBER GHOST X)
Version: 2.0 (Fixed & Optimized)
"""

import os
import sys
import time
import getpass
from datetime import datetime

# Instagram
try:
    import instaloader
    from instaloader import Instaloader
    INSTAGRAM_AVAILABLE = True
except ImportError:
    INSTAGRAM_AVAILABLE = False

# Facebook
try:
    from facebook_scraper import get_profile, get_posts
    FACEBOOK_AVAILABLE = True
except ImportError:
    FACEBOOK_AVAILABLE = False

# ------------------------------------------------------------
# Configuration
PASSWORD = "cyberghostxovi"
MAX_ATTEMPTS = 3
# ------------------------------------------------------------

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code="0"):
    """Print colored text using ANSI codes."""
    print(f"\033[{color_code}m{text}\033[0m")

def banner():
    """Display tool banner."""
    clear_screen()
    banner_art = """
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
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mTOOL   \033[1;31m: \033[1;92mFacebook Instagram Info (Fixed Version)
\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mSTATUS \033[1;31m: \033[1;93mPAID ACCESS GRANTED
\033[1;36m  +===============================================+\033[0m
"""
    print(banner_art)

def check_dependencies():
    """Check if required libraries are installed."""
    if not INSTAGRAM_AVAILABLE:
        print_colored("[!] Instaloader not found. Install with: pip install instaloader", "1;31")
        sys.exit(1)
    if not FACEBOOK_AVAILABLE:
        print_colored("[!] facebook-scraper not found. Facebook functions will be disabled.", "1;33")
        print_colored("    Install with: pip install facebook-scraper", "1;33")
        time.sleep(2)

def authenticate():
    """Password protection."""
    print_colored("[!] This tool is protected. Please enter the password to continue.", "1;33")
    for attempt in range(MAX_ATTEMPTS, 0, -1):
        pwd = getpass.getpass("\033[36mPassword: \033[0m")
        if pwd == PASSWORD:
            print_colored("[✓] Access Granted! Loading tool...", "1;32")
            time.sleep(1)
            return True
        else:
            print_colored(f"[✗] Wrong password! {attempt-1} attempt(s) left." if attempt > 1 else "[✗] Too many failed attempts. Exiting...", "1;31")
            if attempt == 1:
                sys.exit(1)
    return False

# ------------------- Instagram Functions -------------------
def instagram_profile_info(username):
    """Fetch Instagram profile info."""
    print_colored("\n[ Instagram Profile Information ]\n", "1;33")
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)

        info = {
            "Username": profile.username,
            "ID": profile.userid,
            "Full Name": profile.full_name,
            "Biography": profile.biography,
            "Business Category": profile.business_category_name,
            "External URL": profile.external_url,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Is Private": profile.is_private,
            "Is Verified": profile.is_verified,
            "Media Count": profile.mediacount,
            "IGTV Count": profile.igtvcount,
            "Profile Picture": profile.profile_pic_url
        }

        for key, value in info.items():
            print_colored(f"{key}:", "1;32", end=" ")
            print(value)

    except instaloader.exceptions.ProfileNotExistsException:
        print_colored("Error: Profile does not exist.", "1;31")
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

def instagram_post_info(username, limit=10):
    """Show recent Instagram posts."""
    print_colored(f"\n[ Last {limit} Instagram Posts ]\n", "1;33")
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        for i, post in enumerate(posts, 1):
            if i > limit:
                break
            print_colored(f"POST {i}", "1;41")
            print(f"Date: {post.date.strftime('%Y-%m-%d %I:%M %p')}")
            print(f"Caption: {post.caption if post.caption else 'No caption'}")
            print(f"URL: \033[32m{post.url}\033[0m")
            print("-" * 50)
    except instaloader.exceptions.ProfileNotExistsException:
        print_colored("Profile does not exist.", "1;31")
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

def instagram_download_posts(username, download_path=None):
    """Download all posts of a user."""
    print_colored("\n[ Downloading Instagram Posts ]\n", "1;33")
    if download_path is None:
        download_path = os.path.join(os.path.expanduser("~"), "storage/downloads", f"IG_{username}")
    else:
        download_path = os.path.join("/sdcard", download_path)  # Default for Termux

    # Create directory if not exists
    os.makedirs(download_path, exist_ok=True)

    try:
        L = instaloader.Instaloader(dirname_pattern=download_path)
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        count = 0
        for post in posts:
            L.download_post(post, target=download_path)
            count += 1
            print_colored(f"Downloaded post {count}", "1;32")

        print_colored(f"\n✅ Downloaded {count} posts to: {download_path}", "1;32")
    except instaloader.exceptions.ProfileNotExistsException:
        print_colored("Profile does not exist.", "1;31")
    except Exception as e:
        print_colored(f"Error: {e}", "1;31")

# ------------------- Facebook Functions -------------------
def facebook_profile_info(identifier):
    """Fetch Facebook profile info (if library works)."""
    if not FACEBOOK_AVAILABLE:
        print_colored("[!] facebook-scraper not installed. Cannot fetch Facebook info.", "1;31")
        return

    print_colored("\n[ Facebook Profile Information ]\n", "1;33")
    try:
        profile = get_profile(identifier)
        fields = [
            ("Name", "Name"),
            ("Username", "Username"),
            ("ID", "id"),
            ("Followers", "Followers"),
            ("Following", "Following"),
            ("About", "About"),
            ("Profile Picture", "Profile Picture"),
            ("Cover Photo", "Cover Photo"),
            ("Work", "Work"),
            ("Education", "Education"),
            ("Places Lived", "Places Lived"),
            ("Contact Info", "Contact Info"),
            ("Relationship", "Relationship"),
            ("Birthday", "Birthday")
        ]
        for label, key in fields:
            value = profile.get(key, "N/A")
            if value:
                print_colored(f"{label}:", "1;32", end=" ")
                print(value)
            else:
                print_colored(f"{label}:", "1;32", end=" N/A\n")
    except Exception as e:
        print_colored(f"Error fetching Facebook profile: {e}", "1;31")

def facebook_post_info(identifier, limit=10):
    """Fetch recent Facebook posts."""
    if not FACEBOOK_AVAILABLE:
        print_colored("[!] facebook-scraper not installed. Cannot fetch Facebook posts.", "1;31")
        return

    print_colored(f"\n[ Last {limit} Facebook Posts ]\n", "1;33")
    try:
        posts = get_posts(identifier, pages=2)
        for i, post in enumerate(posts, 1):
            if i > limit:
                break
            print_colored(f"POST {i}", "1;41")
            print(f"Time: {post.get('time', 'N/A')}")
            print(f"Text: {post.get('text', 'N/A')}")
            print(f"Post URL: \033[32m{post.get('post_url', 'N/A')}\033[0m")
            print(f"Likes: {post.get('likes', 'N/A')} | Comments: {post.get('comments', 'N/A')}")
            print("-" * 50)
    except Exception as e:
        print_colored(f"Error fetching posts: {e}", "1;31")

def open_help():
    """Open help link."""
    os.system("termux-open-url https://www.facebook.com/cyberghostxovihackeroffpower")
    print_colored("Help page opened in browser.", "1;32")

# ------------------- Menu -------------------
def options_menu(ig_username):
    """Main menu loop."""
    while True:
        clear_screen()
        banner()
        print_colored(f"\nCurrent Instagram username: \033[37m{ig_username}\033[0m\n", "1;36")
        print_colored("Options:", "1;34")
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
            fb_id = input("\nEnter Facebook username or profile ID: ").strip()
            facebook_profile_info(fb_id)
        elif choice == "5":
            fb_id = input("\nEnter Facebook username or profile ID: ").strip()
            facebook_post_info(fb_id)
        elif choice == "6":
            new_ig = input("\nEnter new Instagram username: ").strip()
            if new_ig:
                ig_username = new_ig
                print_colored("Username changed successfully.", "1;32")
        elif choice == "7":
            open_help()
        elif choice == "8":
            print_colored("\nExiting...", "1;31")
            sys.exit(0)
        else:
            print_colored("Invalid choice!", "1;31")

        input("\n\033[36mPress Enter to continue...\033[0m")

def main():
    clear_screen()
    check_dependencies()
    authenticate()
    clear_screen()
    banner()
    ig_user = input("\n\033[36mEnter Instagram username: \033[0m").strip()
    if not ig_user:
        print_colored("No username entered. Exiting.", "1;31")
        sys.exit(1)
    options_menu(ig_user)

if __name__ == "__main__":
    main()
