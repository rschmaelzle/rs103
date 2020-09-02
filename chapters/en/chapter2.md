---
title: 'Chapter 2: Formative Research'
description:
  "In this chapter, you'll use your new skills to perform formative research that informs your campaign. You''ll learn how to conduct a situation analysis, analyze your audience, and understand what prior (communication) efforts exist and what they achieved."
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Formative research" type="slides,video">

<slides source="chapter2_01_data-structures-1" start="11:06" end="13:37">
</slides>

</exercise>

<exercise id="2" title="Situation analysis">

### Part 1

- Look up the string "cat" in `nlp.vocab.strings` to get the hash.
- Look up the hash to get back the string.

<codeblock id="02_02_01">

- You can use the string store in `nlp.vocab.strings` like a regular Python
  dictionary. For example, `nlp.vocab.strings["unicorn"]` will return the hash,
  and looking up the hash again will return the string `"unicorn"`.

</codeblock>

### Part 2

- Look up the string label "PERSON" in `nlp.vocab.strings` to get the hash.
- Look up the hash to get back the string.

<codeblock id="02_02_02">

- You can use the string store in `nlp.vocab.strings` like a regular Python
  dictionary. For example, `nlp.vocab.strings["unicorn"]` will return the hash,
  and looking up the hash again will return the string `"unicorn"`.

</codeblock>

</exercise>

<exercise id="3" title="Audience analysis">

Why does this code throw an error?

```python
from spacy.lang.en import English
from spacy.lang.de import German

# Create an English and German nlp object
nlp = English()
nlp_de = German()

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Look up the ID for "Bowie" in the vocab
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='The string <code>"Bowie"</code> isn’t in the German vocab, so the hash can’t be resolved in the string store.'>

Hashes can't be reversed. To prevent this problem, add the word to the new vocab
by processing a text or looking up the string, or use the same vocab to resolve
the hash back to a string.

</opt>

<opt text='<code>"Bowie"</code> is not a regular word in the English or German dictionary, so it can’t be hashed.'>

Any string can be converted to a hash.

</opt>

<opt text="<code>nlp_de</code> is not a valid name. The vocab can only be shared if the <code>nlp</code> objects have the same name.">

The variable name `nlp` is only a convention. If the code used the variable name
`nlp` instead of `nlp_de`, it'd overwrite the existing `nlp` object, including
the vocab.

</opt>

</choice>

</exercise>

<exercise id="4" title="Hands-on: Audience analysis" type="slides,video">

<slides source="chapter2_02_data-structures-2" start="13:475" end="15:47">
</slides>

</exercise>

<exercise id="5" title="Creating a Doc">

Let's create some `Doc` objects from scratch!

### Part 1

- Import the `Doc` from `spacy.tokens`.
- Create a `Doc` from the `words` and `spaces`. Don't forget to pass in the
  vocab!

<codeblock id="02_05_01">

The `Doc` class takes 3 arguments: the shared vocabulary, usually `nlp.vocab`, a
list of `words` and a list of `spaces`, boolean values, indicating whether the
word is followed by a space or not.

</codeblock>

### Part 2

- Import the `Doc` from `spacy.tokens`.
- Create a `Doc` from the `words` and `spaces`. Don't forget to pass in the
  vocab!

<codeblock id="02_05_02">

Look at each word in the desired text output and check if it's followed by a
space. If so, the spaces value should be `True`. If not, it should be `False`.

</codeblock>

### Part 3

- Import the `Doc` from `spacy.tokens`.
- Complete the `words` and `spaces` to match the desired text and create a
  `doc`.

<codeblock id="02_05_03">

Pay attention to the individual tokens. To see how spaCy usually tokenizes that
string, you can try it and print the tokens for `nlp("Oh, really?!")`.

</codeblock>

</exercise>

<exercise id="6" title="Previous campaign analysis">

In this exercise, you'll create the `Doc` and `Span` objects manually, and
update the named entities – just like spaCy does behind the scenes. A shared
`nlp` object has already been created.

- Import the `Doc` and `Span` classes from `spacy.tokens`.
- Use the `Doc` class directly to create a `doc` from the words and spaces.
- Create a `Span` for "David Bowie" from the `doc` and assign it the label
  `"PERSON"`.
- Overwrite the `doc.ents` with a list of one entity, the "David Bowie" `span`.

<codeblock id="02_06">

- The `Doc` is initialized with three arguments: the shared vocab, e.g.
  `nlp.vocab`, a list of words and a list of boolean values indicating whether
  the word should be followed by a space.
- The `Span` class takes four arguments: the reference `doc`, the start token
  index, the end token index and an optional label.
- The `doc.ents` property is writable, so you can assign it any iterable
  consisting of `Span` objects.

</codeblock>

</exercise>

<exercise id="7" title="Hands on: What messages are out there?">

The code in this example is trying to analyze a text and collect all proper
nouns that are followed by a verb.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Get all tokens and part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Check if the current token is a proper noun
    if pos == "PROPN":
        # Check if the next token is a verb
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### Part 1

Why is the code bad?

<choice>

<opt text="The <code>result</code> token should be converted back to a <code>Token</code> object. This will let you reuse it in spaCy.">

It shouldn't be necessary to convert strings back to `Token` objects. Instead,
try to avoid converting tokens to strings if you still need to access their
attributes and relationships.

</opt>

<opt correct="true" text="It only uses lists of strings instead of native token attributes. This is often less efficient, and can't express complex relationships.">

Always convert the results to strings as late as possible, and try to use native
token attributes to keep things consistent.

</opt>

<opt text='<code>pos_</code> is the wrong attribute to use for extracting proper nouns. You should use <code>tag_</code> and the <code>"NNP"</code> and <code>"NNS"</code> labels instead.'>

The `.pos_` attribute returns the coarse-grained part-of-speech tag and
`"PROPN"` is the correct tag to check for proper nouns.

</opt>

</choice>

### Part 2

- Rewrite the code to use the native token attributes instead of lists of
  `token_texts` and `pos_tags`.
- Loop over each `token` in the `doc` and check the `token.pos_` attribute.
- Use `doc[token.i + 1]` to check for the next token and its `.pos_` attribute.
- If a proper noun before a verb is found, print its `token.text`.

<codeblock id="02_07">

- Remove the `token_texts` and `pos_tags` – we don't need to compile lists of
  strings upfront!
- Instead of iterating over the `pos_tags`, loop over each `token` in the `doc`
  and check the `token.pos_` attribute.
- To check if the next token is a verb, take a look at `doc[token.i + 1].pos_`.

</codeblock>

</exercise>

<exercise id="8" title="Writing the section on formative research" type="slides,video">

<slides source="chapter2_03_word-vectors-similarity" start="15:58" end="19:47">
</slides>

</exercise>
