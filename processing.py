#Video processing to 'short' type
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


