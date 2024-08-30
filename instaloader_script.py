import instaloader

def download_instagram_data(username, password, profile_name):
    L = instaloader.Instaloader()

    try:
        # Log in to Instagram
        L.login(username, password)
        print("Login successful.")
    except instaloader.exceptions.ConnectionException as e:
        print(f"Login failed: {e}")
        return

    try:
        print(f"Attempting to download profile: {profile_name}")
        # Download profile data
        L.download_profile(profile_name, profile_pic=True)
        print(f"Profile {profile_name} downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("The profile does not exist or the URL is incorrect.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    insta_username = "******"  # Replace with your Instagram username
    insta_password = "******"  # Replace with your Instagram password
    target_profile = "ayush_mayekar_"       # Replace with the profile to download

    download_instagram_data(insta_username, insta_password, target_profile)
