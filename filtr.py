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































