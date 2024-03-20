import instaloader

def download_reels(username):
    L = instaloader.Instaloader()

    try:
        # Load the profile of the specified username
        profile = instaloader.Profile.from_username(L.context, username)

        # Download all reels
        for post in profile.get_posts():
            if post.is_video and post.typename == 'GraphVideo':
                L.download_post(post, target=profile.username)

        print("Downloaded all reels from the Instagram account:", username)

    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: The specified Instagram account does not exist.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Replace 'your_username' with the Instagram username from which you want to download reels
    username = 'therealnaturelove'
    download_reels(username)
