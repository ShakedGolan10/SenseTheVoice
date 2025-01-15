# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# class GrammarCorrectionService:
#     def __init__(self):
#         self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#         print(f"Using device: {self.device}")

#         # Initialize the tokenizer and model
#         self.model_name = 'Salesforce/ctrl'
#         self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
#         self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)

#     def analyze_text(self, text: str) -> str:
#         # Define the control code for grammar correction
#         control_code = 'Fix grammar mistakes in the text: '
#         prompt = control_code + text

#         # Tokenize the input
#         inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

#         # Generate the corrected text
#         outputs = self.model.generate(
#             **inputs,
#             max_length=512,
#             num_return_sequences=1,
#             top_k=50,
#             top_p=0.95,
#             temperature=0.7,
#             no_repeat_ngram_size=2,
#             do_sample=True,
#             pad_token_id=self.tokenizer.eos_token_id
#         )

#         # Decode the generated text
#         corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
#         return corrected_text[len(control_code):]  # Remove the control code from the output
