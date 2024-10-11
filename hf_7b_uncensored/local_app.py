from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cognitivecomputations/WizardLM-7B-Uncensored")
tokenizer = AutoTokenizer.from_pretrained("cognitivecomputations/WizardLM-7B-Uncensored")
