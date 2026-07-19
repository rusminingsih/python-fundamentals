import os
import sys
import time
import random
import shutil

# ================= KONFIGURASI =================
FPS = 5 / 20                      # kecepatan animasi (detik per frame)
SNOW_CHARS = ["*", ".", "+", "❄", "✦", "·"]

LYRICS = [
    ("So, what if I call", 3),
    ("And I use this holiday to make my way to your ghost", 4),
    ("And you pick up the phone?", 3),
    ("Oh, what if you're lonely", 3),
    ("And I get the chance to stay", 3),
]

INTRO_LINES = [
    "*.  .:*  Merry Christmas  *:.  .*",
    "",
    "I Miss You",
    "Ghost",
    "*.  .:*        *:.  .*",
]

CLOSING_LINES = ["i loved u"]


# ================= UTIL TERMINAL =================
def get_size():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines - 1  # -1 biar gak ada auto-scroll


def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def clear():
    sys.stdout.write("\033[2J")
    sys.stdout.flush()


# ================= SALJU =================
class Snowflake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset(random_y=True)

    def reset(self, random_y=False):
        self.x = random.randint(0, max(self.width - 1, 0))
        self.y = random.randint(0, max(self.height - 1, 0)) if random_y else 0
        self.char = random.choice(SNOW_CHARS)
        self.speed = random.choice([1, 1, 2])

    def fall(self):
        self.y += self.speed
        if self.y >= self.height:
            self.reset()


def make_snow(width, height, density=0.02):
    count = max(int(width * height * density), 10)
    return [Snowflake(width, height) for _ in range(count)]


# ================= RENDER =================
def render_frame(snow, width, height, text_lines=None):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    for flake in snow:
        if 0 <= flake.y < height and 0 <= flake.x < width:
            grid[flake.y][flake.x] = flake.char

    if text_lines:
        start_row = height // 2 - len(text_lines) // 2
        for i, line in enumerate(text_lines):
            row = start_row + i
            if 0 <= row < height:
                col = max((width - len(line)) // 2, 0)
                for j, ch in enumerate(line):
                    c = col + j
                    if 0 <= c < width:
                        grid[row][c] = ch

    return "\n".join("".join(row) for row in grid)


def render_simple_text(lines):
    width, height = get_size()
    return render_frame([], width, height, text_lines=lines)


def play_scene(snow, text_lines, duration):
    """Tampilkan satu baris/lirik selama `duration` detik sambil salju tetap jatuh."""
    deadline = time.time() + duration
    while time.time() < deadline:
        width, height = get_size()
        pad = "\n" * 0
        for f in snow:
            f.fall()
        frame = render_frame(snow, width, height, text_lines=text_lines)
        sys.stdout.write("\033[H" + pad + frame)
        sys.stdout.flush()
        time.sleep(FPS)


# ================= MAIN =================
def main():
    clear()
    hide_cursor()

    width, height = get_size()
    snow = make_snow(width, height)

    try:
        # intro
        play_scene(snow, INTRO_LINES, duration=3)

        # lirik satu per satu, sinkron durasi
        for lyric, duration in LYRICS:
            play_scene(snow, [lyric], duration)

        # penutup
        clear()
        closing_output = render_simple_text(CLOSING_LINES)
        sys.stdout.write("\033[H" + "\n" * 0 + closing_output)
        sys.stdout.flush()
        time.sleep(3.5)

    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear()


if __name__ == "__main__":
    main()