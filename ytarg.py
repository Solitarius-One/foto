import argparse
from yt_dlp import YoutubeDL

# -------------------------
# Argparse
# -------------------------
parser = argparse.ArgumentParser(description="Download MP3 from YouTube")
parser.add_argument("--keyword", type=str, help="Keyword pencarian YouTube")
parser.add_argument("--url", type=str, help="URL YouTube langsung")

args = parser.parse_args()

# -------------------------
# Tentukan mode input
# -------------------------
if args.url:
    target = args.url
elif args.keyword:
    target = f"ytsearch:{args.keyword}"
else:
    raise ValueError("Harus pakai --keyword atau --url")

# -------------------------
# Opsi download MP3
# -------------------------
opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "outtmpl": "%(title).200s.%(ext)s"
}

# -------------------------
# Eksekusi yt-dlp
# -------------------------
with YoutubeDL(opts) as ydl:
    ydl.download([target])
