import sys
from pdf2image import convert_from_path


def pdf_to_image(pdf_path, output_path, dpi=300):
    images = convert_from_path(pdf_path, dpi=dpi)

    if len(images) == 1:
        images[0].save(output_path)
    else:
        total_height = sum(img.height for img in images)
        max_width = max(img.width for img in images)

        combined = Image.new("RGB", (max_width, total_height))
        y_offset = 0
        for img in images:
            combined.paste(img, (0, y_offset))
            y_offset += img.height
        combined.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.pdf output.jpg")
        sys.exit(1)

    from PIL import Image

    pdf_to_image(sys.argv[1], sys.argv[2])
