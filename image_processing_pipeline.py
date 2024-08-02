from ImageSampler.ImageSampler import random_sample_transformation
from PIL import Image


def image_transformers_pipeline(image: Image.Image, sample_size: list[(int, int)]):
    return random_sample_transformation(image, sample_size)
