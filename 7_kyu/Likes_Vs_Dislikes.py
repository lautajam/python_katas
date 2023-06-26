"""YouTube had a like and a dislike button, which allowed users to express their opinions about particular 
content. It was set up in such a way that you cannot like and dislike a video at the same time. 
There are two other interesting rules to be noted about the interface: Pressing a button, which 
is already active, will undo your press. If you press the like button after pressing the dislike 
button, the like button overwrites the previous "Dislike" state. The same is true for the other way round.

Task
Create a function that takes in a list of button inputs and returns the final state.

Examples
likeOrDislike([Dislike]) => Dislike
likeOrDislike([Like,Like]) => Nothing
likeOrDislike([Dislike,Like]) => Like
likeOrDislike([Like,Dislike,Dislike]) => Nothing

Notes
If no button is currently active, return Nothing.
If the list is empty, return Nothing."""

list_like_dislike = ["Dislike", "Like", "Like", "Disike", "Disike"]

# Take a list of likes/dislikes and check the button state
def like_or_dislike(list_like_dislike):
    ant_btn, result = list_like_dislike[0], ""
    for button in list_like_dislike:
        if button.lower() == "like": # The result is none when the reactions are repeats
            if ant_btn == button: result = None
            else: 
                result = button
                ant_btn = button
        elif button.lower() == "dislike":
            if ant_btn == button: result = None
            else: 
                result = button
                ant_btn = button
        else: 
            continue
    return result

# MAIN

reaction = like_or_dislike(list_like_dislike)

print(reaction)

    