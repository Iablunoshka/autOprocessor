import os
import time
import subprocess
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# Path to JSON file with your OAuth credentials
credentials_file = 'D:\\auto\\client_secret_107282428953-ha76444o9l7fv7fq348htsabfuo1bsve.apps.googleusercontent.com.json'

# Create YouTube API client
flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes=['https://www.googleapis.com/auth/youtube.upload'])
credentials = flow.run_local_server(port=8080)

youtube = build('youtube', 'v3', credentials=credentials)

# Path to video folder
video_folder = 'D:\\meme\\processed'

# Get list of video files
video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

# Load the list of already uploaded videos from a file or database
uploaded_videos = set()  # Replace this with the actual logic to load the list

for video_file in video_files:
    if video_file not in uploaded_videos:  # Check if the video is not already uploaded
        video_path = os.path.join(video_folder, video_file)

        # Video upload parameters
        request_body = {
            'snippet': {
                'title': 'Video Title',
                'description': 'Video Description',
                'tags': ['tag1', 'tag2']
            },
            'status': {
                'privacyStatus': 'private'  # Private video
            }
        }

        # Upload video to YouTube
        media = MediaFileUpload(video_path)
        response = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media).execute()

        print(f"Video '{video_file}' successfully uploaded to YouTube as private:", response['id'])
        
        # Add the uploaded video to the set of uploaded videos
        uploaded_videos.add(video_file)

        # Display message about script restart and uploaded video
        print(f"Script has been restarted. Uploaded video: {video_file}")

        # Delay for 3 minutes before uploading the next video
        time.sleep(180)

# Restarting the script
print("Restarting the script...")
subprocess.run(['python', 'your_script.py'])

