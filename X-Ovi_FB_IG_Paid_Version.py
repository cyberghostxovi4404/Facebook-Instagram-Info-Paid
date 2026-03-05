import os
import sys
import instaloader
from instaloader import Instaloader
import getpass

# Check for facebook-scraper
try:
    from facebook_scraper import get_profile, get_posts
    FACEBOOK_AVAILABLE = True
except ImportError:
    FACEBOOK_AVAILABLE = False

def check_facebook_scraper():
    if not FACEBOOK_AVAILABLE:
        print("\033[1;31m[!] facebook-scraper not installed. Install it with: pip install facebook-scraper\033[0m")
        sys.exit(1)

def banner():
    print("\033[1;31m")
    print("""
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
        ::::::::::::::::::::::::""")
    print("\033[1;36m  +===============================================+")
    print("\033[1;97m     __   __           ____  _      _ _ ")
    print("\033[1;97m     \\ \\ / /          / __ \\| |    | | |")
    print("\033[1;31m      \\ V /  ______  | |  | \\ \\  / /| |")
    print("\033[1;31m       > <  |______| | |  | |\\ \\/ / | |")
    print("\033[1;36m      / . \\          | |__| | \\  /  | |")
    print("\033[1;36m     /_/ \\_\\          \\____/   \\/   |_|")
    print("\033[1;36m  +===============================================+")
    print("\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mCEO    \033[1;31m: \033[1;91mOVI (CYBER GHOST X)")
    print("\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mTEAM   \033[1;31m: \033[1;97mCYBER GHOST X OVI")
    print("\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mTOOL   \033[1;31m: \033[1;92mFacebook Instagram Info Paid Version")
    print("\033[1;37m     [ \033[1;31m• \033[1;37m] \033[1;36mSTATUS \033[1;31m: \033[1;93mPAID ACCESS GRANTED")
    print("\033[1;36m  +===============================================+\033[0m")

def instagram_profile_info(username):
    try:
        print("\033[33mInstagram Profile Informations...\033[0m\n")
        x = Instaloader()
        f = instaloader.Profile.from_username(x.context, username)

        print("\033[32mUsername\033[0m :", f.username)
        print("\033[32mID\033[0m :", f.userid)
        print("\033[32mFull Name\033[0m :", f.full_name)
        print("\033[32mBiography\033[0m :", f.biography)
        print("\033[32mBusiness Category Name\033[0m :", f.business_category_name)
        print("\033[32mExternal URL\033[0m :", f.external_url)
        print("\033[32mFollowed By Viewer\033[0m :", f.followed_by_viewer)
        print("\033[32mFollowees\033[0m :", f.followees)
        print("\033[32mFollowers\033[0m :", f.followers)
        print("\033[32mFollows Viewer\033[0m :", f.follows_viewer)
        print("\033[32mBlocked By Viewer\033[0m :", f.blocked_by_viewer)
        print("\033[32mHas Blocked Viewer\033[0m :", f.has_blocked_viewer)
        print("\033[32mHas Highlight Reels\033[0m :", f.has_highlight_reels)
        print("\033[32mHas Public Story\033[0m :", f.has_public_story)
        print("\033[32mHas Requested Viewer\033[0m :", f.has_requested_viewer)
        print("\033[32mRequested By Viewer\033[0m :", f.requested_by_viewer)
        print("\033[32mHas Viewable Story\033[0m :", f.has_viewable_story)
        print("\033[32mIGTV\033[0m :", f.igtvcount)
        print("\033[32mIs Business Account\033[0m :", f.is_business_account)
        print("\033[32mIs Private\033[0m :", f.is_private)
        print("\033[32mIs Verified\033[0m :", f.is_verified)
        print("\033[32mMedia Count\033[0m :", f.mediacount)
        print("\033[32mProfile Picture URL\033[0m :", f.profile_pic_url)

    except KeyboardInterrupt:
        print("\033[33mI understand!")
    except EOFError:
        print("\033[33mWhy?")
    except Exception as e:
        print("\033[31mError:\033[0m", e)

def instagram_post_info(username):
    print("\n\033[33mInstagram Post Informations...\033[0m\n")
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()

        post_info = []

        for i, post in enumerate(posts, start=1):
            if i > 10:  # Limit to 10 posts to avoid too much output
                break
            caption = post.caption
            if caption is None:
                caption = "No caption provided"
            post_date = post.date.strftime("%Y-%m-%d")
            post_time = post.date.strftime("%I:%M %p")
            post_info.append((f"\033[41mPOST {i}\033[0m", post_date, post_time, caption, post.url))

        if post_info:
            for info in post_info:
                print(f"{info[0]}")
                print(f"Posted Date: {info[1]}")
                print(f"Posted Time: {info[2]}")
                print(f"Caption: {info[3]}")
                print(f"Post URL: \033[32m{info[4]}\033[0m")
                print("-" * 50)
                print()
        else:
            print("No posts found.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def instagram_download_posts(username, download_path):
    print("\n\033[33mDownloading all Instagram posts...\033[0m\n")
    os.chdir('/sdcard')
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        for i, post in enumerate(posts, start=1):
            L.download_post(post, target=download_path)
            print(f"\033[41mPOST {i}\033[0m downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def facebook_profile_info(username):
    check_facebook_scraper()
    print("\n\033[33mFacebook Profile Informations...\033[0m\n")
    try:
        # Get profile info
        profile = get_profile(username)
        # Print available fields
        print("\033[32mName\033[0m :", profile.get('Name', 'N/A'))
        print("\033[32mUsername\033[0m :", profile.get('Username', username))
        print("\033[32mID\033[0m :", profile.get('id', 'N/A'))
        print("\033[32mFollowers\033[0m :", profile.get('Followers', 'N/A'))
        print("\033[32mFollowing\033[0m :", profile.get('Following', 'N/A'))
        print("\033[32mAbout\033[0m :", profile.get('About', 'N/A'))
        print("\033[32mProfile Picture\033[0m :", profile.get('Profile Picture', 'N/A'))
        print("\033[32mCover Photo\033[0m :", profile.get('Cover Photo', 'N/A'))
        print("\033[32mWork\033[0m :", profile.get('Work', 'N/A'))
        print("\033[32mEducation\033[0m :", profile.get('Education', 'N/A'))
        print("\033[32mPlaces Lived\033[0m :", profile.get('Places Lived', 'N/A'))
        print("\033[32mContact Info\033[0m :", profile.get('Contact Info', 'N/A'))
        print("\033[32mRelationship\033[0m :", profile.get('Relationship', 'N/A'))
        print("\033[32mBirthday\033[0m :", profile.get('Birthday', 'N/A'))
    except Exception as e:
        print("\033[31mError fetching Facebook profile:\033[0m", e)

def facebook_post_info(username):
    check_facebook_scraper()
    print("\n\033[33mFacebook Post Informations (last 10 posts)...\033[0m\n")
    try:
        posts = get_posts(username, pages=2)  # Fetch a few posts
        for i, post in enumerate(posts, start=1):
            if i > 10:
                break
            print(f"\033[41mPOST {i}\033[0m")
            print(f"Posted Time: {post.get('time', 'N/A')}")
            print(f"Text: {post.get('text', 'N/A')}")
            print(f"Post URL: \033[32m{post.get('post_url', 'N/A')}\033[0m")
            print(f"Image: {post.get('image', 'N/A')}")
            print(f"Likes: {post.get('likes', 'N/A')}")
            print(f"Comments: {post.get('comments', 'N/A')}")
            print("-" * 50)
            print()
    except Exception as e:
        print("\033[31mError fetching Facebook posts:\033[0m", e)

def open_help():
    os.system("termux-open-url https://www.facebook.com/cyberghostxovihackeroffpower")

def options_menu(username):
    print("\033[36mCurrent Instagram username: \033[0m \033[37m{}\033[0m \n".format(username))
    print("\033[1;34mOptions:\033[0m")
    print("\033[1;33m[1]\033[0m \033[1;32mInstagram Profile Information\033[0m")
    print("\033[1;33m[2]\033[0m \033[1;32mInstagram Post Information\033[0m")
    print("\033[1;33m[3]\033[0m \033[1;32mDownload all Instagram posts\033[0m")
    print("\033[1;33m[4]\033[0m \033[1;32mFacebook Profile Information\033[0m")
    print("\033[1;33m[5]\033[0m \033[1;32mFacebook Post Information\033[0m")
    print("\033[1;33m[6]\033[0m \033[1;32mChange Instagram Username\033[0m")
    print("\033[1;33m[7]\033[0m \033[1;32mGet Help\033[0m")
    print("\033[1;33m[8]\033[0m \033[1;32mExit\033[0m")
    choice = input("\n\033[36mEnter your choice: \033[0m")

    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        instagram_profile_info(username)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        instagram_post_info(username)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        download_path = "X-Ovi-Instagram"
        instagram_download_posts(username, download_path)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        fb_username = input("\n\033[36mEnter Facebook username (or profile ID): \033[0m")
        facebook_profile_info(fb_username)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        fb_username = input("\n\033[36mEnter Facebook username (or profile ID): \033[0m")
        facebook_post_info(fb_username)
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        username = input("\n\033[36mEnter new Instagram username: \033[0m")
        input("\n\033[36mUsername changed successfully. Press Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        open_help()
        input("\n\033[36mPress Enter to go back to the menu...\033[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        options_menu(username)
    elif choice == "8":
        print("\033[1;31mExiting...\033[0m")
        sys.exit()
    else:
        print("Invalid choice.")

def main():
    # Password protection
    correct_password = "cyberghostxovi"
    attempts = 3
    print("\033[1;33m[!] This tool is protected. Please enter the password to continue.\033[0m")
    while attempts > 0:
        password = getpass.getpass("\033[36mPassword: \033[0m")
        if password == correct_password:
            print("\033[1;32m[✓] Access Granted! Loading tool...\033[0m")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\033[1;31m[✗] Wrong password! {attempts} attempt(s) left.\033[0m")
            else:
                print("\033[1;31m[✗] Too many failed attempts. Exiting...\033[0m")
                sys.exit(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    username = input("\n\033[36mEnter Instagram username: \033[0m")
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    options_menu(username)

if __name__ == "__main__":
    main()
