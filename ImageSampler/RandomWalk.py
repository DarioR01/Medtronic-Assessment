from ImageSampler.ImageSample import ImageSample
from typing import List, Dict, Literal
import random

MoveKeys = Literal["top", "right", "left", "bottom"]


class RandomWalk:
    canvas_width: int
    canvas_height: int
    image_samples: List[ImageSample]
    steps: int

    def __init__(self, canvas_width, canvas_height, image_samples: List[ImageSample], steps: int):
        self.canvas_width, self.canvas_height = canvas_width, canvas_height
        self.image_samples = image_samples
        self.steps = steps

    def __possible_moves(self, current_sample: [ImageSample]):
        left_bound, top_bound, right_bound, bottom_bound = current_sample.get_bounds()
        moves: Dict[MoveKeys, int] = {
            "top": top_bound,
            "right": self.canvas_width - right_bound,
            "bottom": self.canvas_height - bottom_bound,
            "left": left_bound
        }

        for other_sample in self.image_samples:
            if other_sample == current_sample:
                continue
            other_left_bound, other_top_bound, other_right_bound, other_bottom_bound = other_sample.get_bounds()

            # Calculate potential moves and update minimum distances
            if left_bound < other_right_bound and right_bound > other_left_bound:
                # They overlap horizontally
                if other_top_bound < top_bound:
                    moves["top"] = min(moves["top"], top_bound - other_bottom_bound)
                if other_bottom_bound > bottom_bound:
                    moves["bottom"] = min(moves["bottom"], other_top_bound - bottom_bound)

            if top_bound < other_bottom_bound and bottom_bound > other_top_bound:
                # They overlap vertically
                if other_right_bound > right_bound:
                    moves["right"] = min(moves["right"], other_left_bound - right_bound)
                if other_left_bound < left_bound:
                    moves["left"] = min(moves["left"], left_bound - other_right_bound)
        return moves

    def run(self):
        for x in range(self.steps):
            for sample in self.image_samples:
                move_keys: list[MoveKeys] = ["top", "right", "left", "bottom"]
                moves = self.__possible_moves(sample)

                random_direction = random.choice(move_keys)
                if random_direction == "top":
                    sample.move(0, -moves["top"])
                elif random_direction == "right":
                    sample.move(moves["right"], 0)
                elif random_direction == "bottom":
                    sample.move(0, moves["bottom"])
                elif random_direction == "left":
                    sample.move(-moves["left"], 0)
        return self.image_samples
