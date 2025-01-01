from PIL import Image
import os

# Define input and output folders
input_folder = "flags_png"  # Folder with PNG files
output_folder = "flags_gif"  # Folder to save GIF files

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each PNG file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".png"):
        try:
            with Image.open(os.path.join(input_folder, file_name)) as img:
                # Ensure the image is converted to RGBA for consistent handling
                if img.mode != "RGBA":
                    img = img.convert("RGBA")

                # Convert to "P" mode (palette-based) for GIF
                img = img.convert("P", palette=Image.ADAPTIVE)

                # Strip transparency by adding a solid white background if needed
                if "transparency" in img.info:
                    new_img = Image.new("RGBA", img.size, (255, 255, 255, 255))
                    new_img.paste(img, (0, 0), img)
                    img = new_img.convert("P", palette=Image.ADAPTIVE)

                # Define the output file path
                gif_file = os.path.join(output_folder, file_name.replace(".png", ".gif"))

                # Save as GIF
                img.save(gif_file, "GIF")
                print(f"Converted: {file_name} -> {gif_file}")

        except Exception as e:
            print(f"Error converting {file_name}: {e}")
