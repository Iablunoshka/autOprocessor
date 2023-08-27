from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Upload to YouTube
credentials_file = 'D:\\auto\\client_secret_392874847723-kturqftmjtbmrk54q224faq7dbef3gqn.apps.googleusercontent.com.json'
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

