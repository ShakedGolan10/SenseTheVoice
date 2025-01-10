from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch
from typing import Dict

class TextAnalysisService:
    def __init__(self):
        self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
        self.model = RobertaForSequenceClassification.from_pretrained(
            "cardiffnlp/twitter-roberta-base-sentiment"  # Example fine-tuned model
        )

    def analyze_text(self, text: str) -> Dict:
        # Analyze the text to classify its sentiment or quality.

        encoded_input = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            output = self.model(**encoded_input)
        logits = output.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        confidence, label_idx = torch.max(probabilities, dim=1)

        # Map the label index to the class name (e.g., 'positive', 'negative', 'neutral')
        labels = ["negative", "neutral", "positive"]  # Example labels; adjust based on your model
        sentiment_label = labels[label_idx.item()]
        return {
            "sentiment_label": sentiment_label,
            "confidence": confidence.item(),
            "logits": logits.numpy().tolist()
        }
