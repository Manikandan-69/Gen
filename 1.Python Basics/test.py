import os

folder = r"D:/Mani_Siva_Selected_Photos"     # <-- change to your folder path
output_file = r"D:/Mani_Siva_Selected_Photos/selected_photo_names.txt"   # <-- where to save

photo_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

# Extract names (without extension)
photo_names = [
    os.path.splitext(f)[0]
    for f in os.listdir(folder)
    if f.lower().endswith(photo_extensions)
]

# Save into text file
with open(output_file, "w", encoding="utf-8") as file:
    for name in photo_names:
        file.write(name + "\n")

print("Saved successfully to:", output_file)


