from pytube import YouTube
import numpy as np
import pandas as pd
from os.path import join, abspath, dirname

# filepaths
ROOT = dirname(dirname(abspath(__file__)))
META_PATH = join(ROOT, 'data', 'metadata.csv')
VID_DIR = join(ROOT, 'data', 'videos')
meta = pd.read_csv(META_PATH, index_col=['creative', 'uid']).sort_index() 

for i, (creative, uid) in enumerate(meta.index): 
    end = '\r' if i < len(meta.index)-1 else '\n'
    print('Processing video %d of %d...' %(i+1, len(meta.index)), end=end, flush=True)
    video_url = "https://www.youtube.com/watch?v=" + uid
    # download highest quality mp4 video to data/videos under the filename {uid}.mp4
    YouTube(video_url).streams.filter(file_extension='mp4').first().download(output_path = VID_DIR, filename = uid + ".mp4")