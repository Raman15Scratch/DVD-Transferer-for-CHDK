import string
import os


def find_dvd():
    drives = [f"{d}:\\" for d in string.ascii_uppercase]

    for drive in drives:
        try:
            if os.path.exists(drive):
                # crude check: DVD usually has VIDEO_TS
                if os.path.exists(drive + "VIDEO_TS"):
                    return drive
        except:
            pass

    return None
