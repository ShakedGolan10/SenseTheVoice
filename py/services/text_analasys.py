from transformers import pipeline

class GrammarCorrectionService:
    def __init__(self):
        # Initialize the pipeline with the Grammar Correction T5 Model
        self.model_name = "hassaanik/grammar-correction-model"
        self.pipeline = pipeline(
            task="text2text-generation", 
            model=self.model_name
        )
        print("GrammarCorrectionService initialized with model:", self.model_name)

    def analyze_text(self, text: str) -> str:
        # Use the model pipeline to generate corrected text
        result = self.pipeline(
            text, 
            num_beams=5,  # Beam search for quality outputs
            no_repeat_ngram_size=2  # Avoid repeated phrases
        )
        corrected_text = result[0]['generated_text']
        print(corrected_text)
        return corrected_text

# Example usage
if __name__ == "__main__":
    service = GrammarCorrectionService()
    input_text = "They is going to spent time together."
    corrected_output = service.analyze_text(input_text)
    print("Corrected text:", corrected_output)
