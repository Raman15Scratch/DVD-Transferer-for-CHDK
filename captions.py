import re


def load_captions(file_path):
    captions = []

    pattern = r"\((\d{2}):(\d{2}):(\d{2}):(\d{2})\)\s*(.*)"

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                h, m, s, fms, text = match.groups()

                total_frames = (
                    int(h) * 3600 * 30 +
                    int(m) * 60 * 30 +
                    int(s) * 30 +
                    int(fms)
                )

                captions.append({
                    "frame": total_frames,
                    "text": text
                })

    return captions
