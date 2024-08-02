from PIL import Image
from typing import List
from .ImageSample import ImageSample
from .RandomWalk import RandomWalk
from rectpack import newPacker


def random_sample_transformation(image: Image.Image, sample_sizes: list[(int, int)]):
    bin_width, bin_height = image.size
    packer = newPacker()

    packer.add_bin(bin_width, bin_height)
    for sample in sample_sizes:
        packer.add_rect(*sample)

    packer.pack()

    image_samples: List[ImageSample] = []
    for packer_bin in packer:
        for sample in packer_bin:
            image_samples.append(ImageSample(sample.x, sample.y, sample.width, sample.height))

    if len(image_samples) < len(sample_sizes):
        raise Exception(f"Error: The total size of your samples cannot fit the provided image of size "
                        f"{bin_width}x{bin_height}px without overlapping, "
                        f"please consider reducing the size of the samples")

    return __image_sampler(image, image_samples)


def __image_sampler(image: Image.Image, image_samples: List[ImageSample]):
    canvas_width, canvas_height = image.size

    total_size = [0, 0]
    for sample in image_samples:
        total_size[0] += sample.x
        total_size[1] += sample.y

    if total_size[0] > canvas_width and total_size[1] > canvas_height:
        raise Exception(f"Error: The total size of the samples exceeds the Image size.")

    random_walk = RandomWalk(canvas_width, canvas_height, image_samples, 10000)
    random_walk.run()

    image_crops = []
    for sample in image_samples:
        image_crops.append(image.crop(sample.get_bounds()))

    return image_crops
