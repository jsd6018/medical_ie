#package used from https://allenai.github.io/scispacy/
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
import os
import json
#tokenizer = AutoTokenizer.from_pretrained("samrawal/bert-base-uncased_clinical-ner")
#model = AutoModelForTokenClassification.from_pretrained("samrawal/bert-base-uncased_clinical-ner")
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

files = os.listdir("output/")
for i in range(len(files)):
    print("------------- FILE: ",files[i]," -------------")
    data = open("output/"+files[i], 'r', encoding='utf-8').read()
    x = nlp(data)
    print(type(x))
    print(x)
    f = open("ner_outputs/bert_base/"+files[i], "w")
    f.write(str(x))
