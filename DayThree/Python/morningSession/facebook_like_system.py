def facebook_likes(likes):
    if len(likes) == 0:
        display == f"no one likes this"
    elif len(likes) == 1:
        display == f"likes[0] likes this"
    elif len(likes) == 2:
        display == f"likes[0] and Likes[1] likes this"
    elif len(likes) == 3:
        display == f"likes[0], likes[1] and likes[2] likes this"
    elif len(likes) == 4:
        display == f"likes[0], likes[1] and 2 others likes this"
        
    return display
