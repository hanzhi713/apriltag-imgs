import cv2
import os
import pathlib
folder = 'tag25h9'
files = os.listdir(folder)
gen_path = os.path.join('generated', folder)

os.makedirs(gen_path, exist_ok=True)
for f in files:
    if f.endswith(".png"):
        img = cv2.imread(os.path.join(folder, f))
        img = cv2.resize(img, (1024, 1024), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(os.path.join(gen_path, f), img)
