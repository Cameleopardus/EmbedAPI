from typing import List
from InstructorEmbedding import INSTRUCTOR


class InstructEmbeddingInput:
    instruction = ""
    input_text = ""

    def __init__(self, instruction, input_text):
        self.instruction = instruction
        self.input_text = input_text


class InstructorEmbeddingService:
    def __init__(self):
        self.model = INSTRUCTOR("hkunlp/instructor-large")

    def generate_embeddings(self, inputs: List[InstructEmbeddingInput]):
        embeddings = self.model.encode(
            [[input.instruction, input.input_text] for input in inputs]
        )
        return embeddings

    def generate_embedding(self, instruction, input_text):
        try:
            embedding = self.model.encode([[instruction, input_text]])

            return embedding

        except Exception as e:
            return None, str(e)
