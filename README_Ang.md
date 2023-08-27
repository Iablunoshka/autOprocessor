Automated Script for Uploading and Processing Videos on YouTube

This repository contains an automated script written in Python that enables you to upload, process, and publish videos on YouTube. The script is designed to automate the process of finding, uploading, processing, and publishing video content to your YouTube channel.

Features:

Video Download from 9gag: The script automatically finds and downloads video content from the popular source, 9gag.
Format Conversion: Videos downloaded in webm format are automatically converted to mp4 format for compatibility with most platforms.
Duration Sorting: Videos are automatically sorted into short (less than 1 minute) and long (more than 1 minute) categories, placed in their respective folders.
Video Processing: Videos with a duration of less than 1 minute are processed for optimal vertical display.
YouTube Upload: After processing, videos are automatically uploaded to your YouTube channel.
Requirements:

To use the script, you'll need the following modules and libraries:

Selenium: Used for automatic video download from websites.
Requests: Used for downloading videos from URLs.
DateTime: Used for generating unique file names based on the current date and time.
OS: Used for working with the file system.
Subprocess: Used for executing commands in the terminal, such as video conversion.
MoviePy: Used for working with video files and video processing.
Google API Client: Used for automated video uploads to YouTube.
WebDriver (Selenium): Used for automating browser actions.
How to Use:

Run the script. The script will download videos from the website and save them to the "D:\meme" folder.
Videos will be automatically converted from webm format to mp4.
Videos will be automatically sorted by duration into the "D:\meme\1min" and "D:\meme\more_min" folders.
Videos with a duration of less than 1 minute will be processed and moved to the "D:\meme\processed" folder.
Replace the path to the "client_secret.json" file for YouTube API usage.
After processing, videos will be automatically uploaded to your YouTube channel.
License:

This project is distributed under the MIT License.

Author:

Iablunoshka

Contact:

If you have questions or suggestions, you can reach me on Discord: 6masia9

Disclaimer:

This script is provided "as is" and is developed for personal purposes. Before using, make sure you have all required libraries and modules, and that you've properly set up access to the YouTube API.