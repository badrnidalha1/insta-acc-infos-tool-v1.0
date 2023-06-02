import instaloader

ig=instaloader.Instaloader()


def printcolored(param):
    pass


print("""

$$$$$$\ $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\        $$$$$$$\   $$$$$$\ $$$$$$$$\ 
\_$$  _|$$$\  $$ |$$  __$$\\__$$  __|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\       $$  __$$\ $$  __$$\\__$$  __|
  $$ |  $$$$\ $$ |$$ /  \__|  $$ |   $$ /  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |      $$ |  $$ |$$ /  $$ |  $$ |   
  $$ |  $$ $$\$$ |\$$$$$$\    $$ |   $$$$$$$$ |        $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |      $$$$$$$\ |$$ |  $$ |  $$ |   
  $$ |  $$ \$$$$ | \____$$\   $$ |   $$  __$$ |        $$ |  $$ \$$$$ |$$  __|   $$ |  $$ |      $$  __$$\ $$ |  $$ |  $$ |   
  $$ |  $$ |\$$$ |$$\   $$ |  $$ |   $$ |  $$ |        $$ |  $$ |\$$$ |$$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |   
$$$$$$\ $$ | \$$ |\$$$$$$  |  $$ |   $$ |  $$ |      $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |      $$$$$$$  | $$$$$$  |  $$ |   
\______|\__|  \__| \______/   \__|   \__|  \__|      \______|\__|  \__|\__|       \______/       \_______/  \______/   \__|    V 1
                                                                                                                              
                                BY @badr.n1d        2021 - 2023 , All rights reserved.                                                                                      
                                                                                                                              
""")

# GET INSTAGRAM ACCOUNT INFORMATIONS .
usrname=input("Enter username: ")

profile=instaloader.Profile.from_username(ig.context, usrname)

print("Username: ", profile.username)
print("Number of Posts: ", profile.mediacount)
print(profile.username+ "  is having  "  +    str(profile.followers)+  ' followers. ')
print(profile.username+ "  is following  "  +   str(profile.followees)+  ' peoples. ')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)


# END