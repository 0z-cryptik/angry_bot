import random

emojis = {
    "red_angry_face": "\uE416",
    "middle_finger": "\U0001F595",
    "unamused_face": "\uE40E",
    "slightly_smiling_face": "\U0001F642",
    "unamused_and_slightly_angry": "\uE402",
    "folded_hands": "\uE41D",
    "face_with_hand_over_mouth": "\U0001F92D",
}


def curses_func(name: str, message: str) -> str:
    curses_list = [
        f"Hi {name}, kindly f*ck off {emojis['slightly_smiling_face']}",
        f"Oh shut your stupid ass up, talking bout {message} {emojis['unamused_face']}",
        f"Shut your goofy ass up b*tch and go get a job",
        f"Shut the f*ck up",
        f"Shut the f*ck up {name}",
        f"Ain't you got something better to do? {emojis['unamused_and_slightly_angry']}",
        f"F*ck you {name}",
        f"F*ck off {name}",
        f"Mirror mirror on the wall, you're the stupidest of them all"
        f"blah blah blah... I don't remember asking your dumb ass for a damn thing",
        f"Do you have a mental condition? or are you just this f*cking stupid naturally?",
        f"Please shut up before I make you cry",
        f"You sound just as dumb as I expected",
        f"Somewhere out there there is a tree that's giving you oxygen. You need to go find that tree and apologise",
        f"You asked your mom what her biggest mistake is, she asked you to go look in the mirror",
        f"The person that said nobody is ugly must not have met you",
        f"You have a face that would make onions cry",
        f"I am jealous of all the people that have never met you",
        f"You know {name} I was thinking of you today, and it reminded me to take out the trash",
        f'"{message}"\n\n Were you born this dumb, or did you have to take lessons??',
        f"You know {name} everyone is allowed to act stupid once in a while, but you're really abusing the privilege {emojis['face_with_hand_over_mouth']}",
        f"You must have been born on a highway, because that's where most accidents happen",
        f"{name} you're not the dumbest person on the planet, but you sure better hope they don't die {emojis['folded_hands']}",
    ]

    random_reply: str = random.choice(curses_list)

    return random_reply
