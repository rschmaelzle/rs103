import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/en/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{____: ____}, {____: ____}]

# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{____: ____}, {____: ____}]

# Add patterns to the matcher and check the result
matcher.add("GADGET", None, pattern1, pattern2)
for doc in nlp.pipe(TEXTS):
    print([doc[start:end] for match_id, start, end in matcher(doc)])
