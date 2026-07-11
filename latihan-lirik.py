import sys
import time


def lirik():
    lirik = [
        ("I text a postcard sent to you...", 0.1),
        ("Did it go through?", 0.1),
        ("Sendin' all my love to you", 0.2),
        ("You are the moonlight of my life", 0.1),
        ("Every night", 0.2),
        ("Givin' all my love to you", 0.1),
    ]

    delay = [0.7, 2, 3.3, 0.8, 1.2, 0.8]

    print("\nLast Night on Earth - Greenday")
    time.sleep(2)

    for i, (line, delay_karakter) in enumerate(lirik):
        for karakter in line:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print("")

    print("\nCode by: nama maba_nim")


lirik()
