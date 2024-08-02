import os
from PIL import Image
from image_processing_pipeline import image_transformers_pipeline


def get_file_extension(file_path: str):
    _, extension = os.path.splitext(file_path)
    return extension


def is_image(file_path: str):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False


def input_image_path(message: str):
    while True:
        print(message)
        image_path_input = input()
        if not os.path.isfile(image_path_input):
            print("Error: invalid image path")

        if not is_image(image_path_input):
            print("Error: file is not a valid image")
            continue
        return image_path_input


def input_integer(message: str):
    while True:
        print(message)
        value = input()
        try:
            value = int(value)
            return value
        except ValueError:
            print("Error: value must be a valid integer")


def main():
    number_of_sample = 3
    while True:
        try:
            image_path = input_image_path("Please provide the path to an image:")
            img = Image.open(image_path)

            while True:
                try:
                    image_sample_sizes: list[(int, int)] = []
                    for i in range(number_of_sample):
                        sample_width = input_integer(f"Please insert width for sample number {i + 1}:")
                        sample_height = input_integer(f"Please insert height for sample number {i + 1}:")
                        image_sample_sizes.append((sample_width, sample_height))

                    images = image_transformers_pipeline(img, image_sample_sizes)

                    for i, image in enumerate(images):
                        output_location = os.path.join(os.getcwd(),
                                                       f"image_output",
                                                       f"sample_{i + 1}{get_file_extension(image_path)}")
                        image.save(output_location)
                    break
                except Exception as error:
                    print(error)
            break

        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
