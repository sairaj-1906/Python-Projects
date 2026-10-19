from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image path
image_paths = [
    r"D:\Wallpapers\New folder\wallpaperflare.com_wallpaper.jpg",
    r"D:\Wallpapers\captain-america-the-3840x2160-24343.jpg",
    r"D:\Wallpapers\iron-man-marvel-superheroes-marvel-comics-3840x2160-7871.jpg",
    r"D:\Wallpapers\wallpaperflare.com_wallpaper (3).jpg",
    r"D:\Wallpapers\wallpapersden.com_i-am-the-knight-moon-knight_3840x2160.jpg",
    r"D:\Wallpapers\wallpaperflare.com_wallpaper (1).jpg",
]

# Resize the image to 1920x1080
image_size = (1920, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()