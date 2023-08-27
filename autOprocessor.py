from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from datetime import datetime
import os
import subprocess
import shutil
from moviepy.editor import VideoFileClip
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Launch the browser scrolling the page to load memes
driver = webdriver.Edge(executable_path='D:\python\msedgedriver.exe')
driver.get('https://9gag.com/trending')
time.sleep(10)
html = driver.find_element(By.TAG_NAME, 'html')
downloaded_videos = set()
for i in range(50):
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Finding the right html elements
    elems = driver.find_elements(By.CSS_SELECTOR, 'div.post-view.video-post')

    for elem in elems:
        print(elem.text)
        print(elem)
        videos = elem.find_elements(By.CSS_SELECTOR, 'video')
        if videos:
            print("Item found <video>")
        else:
            print("Item <video> Not Found")
        for video in videos:
            source = video.find_element(By.CSS_SELECTOR, 'source')
            src = source.get_attribute('src')
            if src not in downloaded_videos:
                downloaded_videos.add(src)
                print(f"Link to the videо: {src}")

                # Generate a unique file name with the current date and time
                filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.webm'
                path = f'D:\\meme\\{filename}'

                response = requests.get(src)
                with open(path, 'wb') as file:
                    file.write(response.content)

# Closing of the Bruezer and Waiting Time
time.sleep(1)
driver.quit()

# Convert all webm videos to mp4
input_folder = 'D:\\meme'
output_folder = 'D:\\meme'

for filename in os.listdir(input_folder):
    if filename.endswith('.webm'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp4')
        subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-c:a', 'aac', output_path])
        os.remove(input_path)

# Video filtering by duration

# Paths to video folders
video_folder = 'D:\meme'
short_videos_folder = os.path.join(video_folder, '1min')
long_videos_folder = os.path.join(video_folder, 'more_min')

# Create folders if they don't exist
os.makedirs(short_videos_folder, exist_ok=True)
os.makedirs(long_videos_folder, exist_ok=True)

# Get list of video files
video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)

    with VideoFileClip(video_path) as video:
        duration = video.duration

    threshold = 60  # 1 minute

    if duration <= threshold:
        destination = os.path.join(short_videos_folder, video_file)
        shutil.move(video_path, destination)
    else:
        destination = os.path.join(long_videos_folder, video_file)
        shutil.move(video_path, destination)

    print(f"Video '{video_file}' moved to {destination}")
    time.sleep(1)

print("Sorting completed.")

# Video processing to 'short' type
def process_video(input_path, output_path, width, height):
    if width >= height:
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale=1080:960, pad=1080:1920:0:(oh-ih)/2:color=black',
            output_path
        ]
    else:
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale=1080:960, setsar=1:1, pad=1080:1920:0:(oh-ih)/2:color=black',
            output_path
        ]
    subprocess.run(cmd, check=True)

def main():
    video_folder = 'D:/meme/1min'
    processed_folder = 'D:/meme/processed'

    os.makedirs(processed_folder, exist_ok=True)

    video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

    for video_file in video_files:
        input_path = os.path.join(video_folder, video_file)
        output_file = os.path.splitext(video_file)[0] + '_processed.mp4'
        output_path = os.path.join(processed_folder, output_file)

        video = VideoFileClip(input_path)
        width, height = video.size
        video.close()

        if width >= height:
            process_video(input_path, output_path, width, height)
            os.remove(input_path)
            print(f"Processed and moved: {output_path}")
        elif width == height:
            process_video(input_path, output_path, width, height)
            os.remove(input_path)
            print(f"Processed and moved (square video): {output_path}")
        else:
            shutil.move(input_path, os.path.join(processed_folder, video_file))
            print(f"Video with inappropriate aspect ratio moved: {input_path}")

if __name__ == "__main__":
    main()

# Upload to YouTube
credentials_file = 'Path_to_your_Json_file'
flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes=['https://www.googleapis.com/auth/youtube.upload'])
credentials = flow.run_local_server(port=8080)
youtube = build('youtube', 'v3', credentials=credentials)

video_folder = 'D:\\meme\\processed'
video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)

    request_body = {
        'snippet': {
            'title': 'Video Title',
            'description': 'Video Description',
            'tags': ['tag1', 'tag2']
        },
        'status': {
            'privacyStatus': 'unlisted'  # Private video
        }
    }

    media = MediaFileUpload(video_path)
    response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()

    print(f"Video '{video_file}' successfully uploaded to YouTube as private:", response['id'])
    time.sleep(300)  # Delay for 5 minutes before uploading the next video
    
    
