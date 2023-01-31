from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


def select_photo():
    """Select image to work on."""
    path = filedialog.askopenfilename(title="Select a File")
    # Pass filepath to watermark function
    add_watermark(path)


def add_watermark(path):
    """Add watermark to selected image."""
    # Open image
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    # Get watermark text
    text = wm_text.get()
    # Get size of image
    width, height = image.size
    # Set font
    font = ImageFont.truetype("arial", 20)
    # Calculate x,y coordinates for watermark
    x = width / 4
    y = height / 4
    # Draw watermark on image
    draw.text((x, y), text=text, font=font, fill=(255, 0, 0))
    # Show watermarked image
    image.show()


# Set up window
window = Tk()
window.title("Add Watermarks to Your Images")
window.minsize(width=500, height=350)
window.config(padx=100, pady=100, bg="LightGrey")

# Watermark label and box for watermark text
wm_label = Label(window, text="Enter your watermark text!", font="Arial 16 bold", bg="LightGrey")
wm_label.grid(column=0, row=0, padx=100)
wm_text = Entry(window, bd=0, width=30, highlightthickness=0, justify="center")
wm_text.insert(1, "Watermark Text")
wm_text.grid(column=0, row=1, pady=10)

# File select label and button
message = Label(window, text="Click the button to choose a file!", font="Arial 16 bold", bg="LightGrey")
message.grid(column=0, row=2)
select = Button(window, text="Select", command=select_photo)
select.grid(column=0, row=3, pady=10)

# Keep window open until user closes it
window.mainloop()
