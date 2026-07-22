import time


def fake_transfer(dvd_path, captions):
    print("Starting transfer...")
    print(f"DVD: {dvd_path}")
    print(f"Captions: {len(captions)} items")

    for i, c in enumerate(captions):
        print(f"Sending frame {c['frame']} → {c['text']}")
        time.sleep(0.2)

    print("Transfer complete!")
