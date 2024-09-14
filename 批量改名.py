import os
import re

path = r'Y:\电视剧\康熙微服私访记\Season 1'

suffix = '.mp4'
suffix1 = '.nfo'
suffix2 = '.jpg'

for file in os.listdir(path):
    if file[-len(suffix):] == suffix:
        fff = re.findall('第(\d+)集', file)
        old_file = os.path.join(path, file)

        new_file = os.path.join(path, '康熙微服私访记 S01E' + fff[0] + '.mp4')

        os.rename(old_file, new_file)

    if file[-len(suffix1):] == suffix1:
        os.remove(os.path.join(path, file))

    if file[-len(suffix2):] == suffix2:
        os.remove(os.path.join(path, file))