
!apt-get install ffmpeg
!pip install pillow moviepy


import os
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import AudioFileClip, ImageClip
import requests
from io import BytesIO


def create_text_image(text, output_image_path, image_path):
    try:
        
        try:
            background_image = Image.open(image_path).convert("RGB")  
        except FileNotFoundError:
            print(f"Background image not found at: {image_path}. Using a black background.")
            background_image = Image.new('RGB', (1920, 1080), color='black')

        image = background_image.copy() 
        draw = ImageDraw.Draw(image)

        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        try:
            font_size = 70
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(f"Font not found at {font_path}. Using default font.")
            font_size = 50
            font = ImageFont.load_default()

        lines = text.splitlines()
        y_offset = 50
        for line in lines:
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            x_position = (image.width - text_width) / 2
            draw.text((x_position, y_offset), line, fill="white", font=font) 
            y_offset += font_size + 20

        image.save(output_image_path)
        print("✅ Text image created successfully.")
        return output_image_path
    except Exception as e:
        print(f"⚠️ Error creating text image: {e}")
        return None



def download_genz_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Image downloaded successfully to {save_path}")
        return save_path
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error downloading image: {e}")
        return None


image_url = "https://i.pinimg.com/560x/e7/ef/42/e7ef42836394292119418c038358f892.jpg" 
image_path = "genz_image.jpg"
downloaded_path = download_genz_image(image_url, image_path)

if downloaded_path is None:
    print("Exiting due to image download failure.")
    exit()


final_summary_short = """This is a GenZ-style video.
Replace this with your content.
Multi-line text works!"""
final_summary_short = ''.join([c if c.isprintable() else ' ' for c in final_summary_short])

text_image_path = "text_image.png"
created_path = create_text_image(final_summary_short, text_image_path, image_path)  # Pass image_path

if created_path is None:
    print("Exiting due to text image creation failure.")
    exit()




audio_clip = AudioFileClip(audio_path)
duration = min(audio_clip.duration, 30)
audio_clip = audio_clip.subclip(0, duration)

image_clip = ImageClip(text_image_path).set_duration(duration)
final_clip = image_clip.set_audio(audio_clip)

output_video_path = "genz_reel.mp4"
final_clip.write_videofile(output_video_path, codec="libx264", fps=1)

print("✅ Video saved as 'genz_reel.mp4'. You can download it now.")


from google.colab import files
files.download(output_video_path)