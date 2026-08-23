import sys
import time


def lirik():
    lirik = [
        ("Oh thinkin' about our younger years", 0.1),
        ("There was only you and me ", 0.1),
        ("We were young and wild and free", 0.1),

        ("Now nothin' can take you away from me", 0.1),
        ("We've been down that road before - but that's over now", 0.1),
        ("You keep me comin' back for more", 0.1)

        ("Baby you're all that I want - when you're lyin' here in my arms", 0.1),
        ("i'm findin it hard to believe - we're in heaven", 0.1),
        ("And love is all that I need and I found it there in your heart", 0.1),
        ("It isn't to hard to see - we're in heaven", 0.1),
    ]

    delay = [2, 3, 2.5, 0.1, 0.1, 1, 2, 3, 2.5, 0.1, 0.1, 1, 2, 3, 2.5, 0.1, 0.1]

    print("\nHeaven - Bryan Adams\n")
    time.sleep(2)

    for i, (line, delay_karakter) in enumerate(lirik):
        for karakter in line:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print("")

    print("\nCode by: ningss")

lirik()
