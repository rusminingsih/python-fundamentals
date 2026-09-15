import sys
import time

def lirik():
    lirik = [
        ("If you ever leave me, baby", 0.1),
        ("Leave some morphine at my door", 0.1),
        ("'Cause it would take a whole lot of medication", 0.1),
        ("To realize what we used to have", 0.1),
        ("We don't have it anymore", 0.1),

        ("There's no religion that could save me", 0.1),
        ("No matter how long my knees are on the floor", 0.1),
        ("So keep in mind all the sacrifices I'm making", 0.1),
        ("To keep you by my side", 0.1),
        ("To keep you from walking out the door", 0.1),

        ("'Cause there'll be no sunlight", 0.1),
        ("If I lose you, baby", 0.1),
        ("There'll be no clear skies", 0.1),
        ("If I lose you, baby", 0.1),
        ("Just like the clouds, my eyes will do the same", 0.1),
        ("If you walk away, every day it will rain, rain, rain", 0.1)
    ]

    delay = [2, 3, 2.5, 0.1, 0.1, 1, 2, 3, 2.5, 0.1, 0.1, 1, 2, 3, 2.5, 0.1, 0.1]

    print("\nBruno Mars - It Will Rain\n")
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
