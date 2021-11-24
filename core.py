from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch as pt
import re

model = AutoModelForSequenceClassification.from_pretrained("alberti-finetuned", use_auth_token=True)
tokenizer = AutoTokenizer.from_pretrained("alberti-finetuned", local_files_only=True)


def get_stanza_type(stanza):
    inputs = tokenizer(stanza, return_tensors="pt")
    outputs = model(**inputs)
    best = pt.argmax(outputs.logits, dim=-1).item()
    return model.config.id2label[best]


def split_stanzas(poem):
    return re.split(r"\n{2,}", poem)


def get_stanzas(poem):
    res_dict = {}
    stanza_list = split_stanzas(poem)
    if stanza_list:
        for idx, stanza in enumerate(stanza_list):
            res_dict[idx] = {"stanza": stanza,
                            "type_of_stanza": get_stanza_type(stanza)}
        return res_dict
    return False
