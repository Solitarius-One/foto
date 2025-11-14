# download_bing.py
#install bing_image_downloader
from bing_image_downloader import downloader
import sys

if len(sys.argv) < 2:
    print("Usage: python download_bing.py \"keyword\" [limit]")
    sys.exit(1)

keyword = sys.argv[1]
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20  # default 20 gambar

downloader.download(keyword, limit=limit, output_dir='hasil', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
print(f"✅ Selesai. Cek folder ./hasil/{keyword.replace(' ', '_')}/")
#python3 what.py "kucing lucu" 10
