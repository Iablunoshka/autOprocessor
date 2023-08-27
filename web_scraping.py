# Start the browser, scroll the page to load memes
driver = webdriver.Edge(executable_path='D:\python\msedgedriver.exe')
driver.get('https://9gag.com/trending')
time.sleep(10)
html = driver.find_element(By.TAG_NAME, 'html')
downloaded_videos = set()

# Scroll down to load more content
for i in range(50):
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Find relevant HTML elements
    elems = driver.find_elements(By.CSS_SELECTOR, 'div.post-view.video-post')

    for elem in elems:
        print(elem.text)
        print(elem)
        videos = elem.find_elements(By.CSS_SELECTOR, 'video')
        if videos:
            print("Found <video> element")
        else:
            print("<video> element not found")
        for video in videos:
            source = video.find_element(By.CSS_SELECTOR, 'source')
            src = source.get_attribute('src')
            if src not in downloaded_videos:
                downloaded_videos.add(src)
                print(f"Video link: {src}")

                # Generate a unique file name with current date and time
                filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.webm'
                path = f'D:\\meme\\{filename}'

                # Download the video
                response = requests.get(src)
                with open(path, 'wb') as file:
                    file.write(response.content)

# Close the browser and wait
time.sleep(1)
driver.quit()
        
