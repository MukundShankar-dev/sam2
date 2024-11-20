import os
import cv2
from tqdm import tqdm

for fn in os.listdir('video_samples'):
    fname = f'video_samples/{fn}/FineGym_{fn}.mp4'
    cap = cv2.VideoCapture(fname)
    if not cap.isOpened():
        print(f'Error: Unable to open file {fname}')
        exit(1)

    framerate = cap.get(cv2.CAP_PROP_FPS)
    video_len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"frame rate: {framerate}")

    frames_dir = f'video_samples/{fn}/frames'
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir, exist_ok=True)

    for i in tqdm(range(video_len)):
        ret, frame = cap.read()
        if not ret:
            print(f'Error: Unable to read frame {i}')
            break
        cv2.imwrite(f'video_samples/{fn}/frames/{i}.jpg', frame)