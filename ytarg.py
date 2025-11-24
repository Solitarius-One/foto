from yt_dlp import YoutubeDL

keyword = "lagu lofi tidur"   # bisa diganti bebas
search_query = f"ytsearch:{keyword}"

opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "outtmpl": "%(title).200s.%(ext)s"
}

with YoutubeDL(opts) as ydl:
    ydl.download([search_query])
