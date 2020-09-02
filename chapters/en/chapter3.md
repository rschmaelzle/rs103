---
title: 'Chapter 3: Theory Pharmacy'
description:
  "This chapter will introduce you to the most important theories that can guide your strategy. You'll learn about theories that explain health behavior change, information processing, and message effects. Just like a doctor can draw from different treatment options (e.g. pills vs. surgery), you will obtain a set of theoretically sound and thus immensely practical tools."
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Theory & Practice" type="slides,video">

<slides source="chapter3_01_processing-pipelines" start="23:36" end="26:12">
</slides>

</exercise>

<exercise id="2" title="Health Belief Model">

What does spaCy do when you call `nlp` on a string of text?

```python
doc = nlp("This is a sentence.")
```

<choice>

<opt text="Run the tagger, parser and entity recognizer and then the tokenizer.">

The tokenizer is always run _before_ all other pipeline components, because it
transforms a string of text into a `Doc` object. The pipeline also doesn't have
to consist of the tagger, parser and entity recognizer.

</opt>

<opt text="Tokenize the text and apply each pipeline component in order." correct="true">

The tokenizer turns a string of text into a `Doc` object. spaCy then applies
every component in the pipeline on document, in order.

</opt>

<opt text="Connect to the spaCy server to compute the result and return it.">

spaCy computes everything on the machine and doesn't need to connect to any
server.

</opt>

<opt text="Initialize the language, add the pipeline and load in the binary model weights.">

When you call `spacy.load()` to load a model, spaCy will initialize the
language, add the pipeline and load in the binary model weights. When you _call_
the `nlp` object on a text, the model is already loaded.

</opt>

</exercise>

<exercise id="3" title="Theory of Reasoned Action">

Let's inspect the small English model's pipeline!

- Load the `en_core_web_sm` model and create the `nlp` object.
- Print the names of the pipeline components using `nlp.pipe_names`.
- Print the full pipeline of `(name, component)` tuples using `nlp.pipeline`.

<codeblock id="03_03">

The list of component names is available as the `nlp.pipe_names` attribute. The
full pipeline consisting of `(name, component)` tuples is available as
`nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="EPPM (Fear Appeals)" type="slides,video">

<slides source="chapter3_02_custom-pipeline-components" start="26:235" end="29:05">
</slides>

</exercise>

<exercise id="5" title="Social Norms">

Which of these problems can be solved by custom pipeline components? Choose all
that apply!

1. Updating the pre-trained models and improving their predictions
2. Computing your own values based on tokens and their attributes
3. Adding named entities, for example based on a dictionary
4. Implementing support for an additional language

<choice>

<opt text="1 and 2.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly.

</opt>

<opt text="1 and 3.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly.

</opt>

<opt text="1 and 4.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly. They're also added to the pipeline after the
language class is already initialized and after tokenization, so they're not
suitable to add new languages.

</opt>

<opt text="2 and 3." correct="true">

Custom components are great for adding custom values to documents, tokens and
spans, and customizing the `doc.ents`.

</opt>

<opt text="2 and 4.">

Custom components are added to the pipeline after the language class is already
initialized and after tokenization, so they're not suitable to add new
languages.

</opt>

<opt text="3 and 4.">

Custom components are added to the pipeline after the language class is already
initialized and after tokenization, so they're not suitable to add new
languages.

</opt>

</choice>

</exercise>

<exercise id="6" title="Social Cognitive Theory & Entertainment Education">

The example shows a custom component that prints the token length of a document.
Can you complete it?

- Complete the component function with the `doc`'s length.
- Add the `length_component` to the existing pipeline as the **first**
  component.
- Try out the new pipeline and process any text with the `nlp` object – for
  example "This is a sentence.".

<codeblock id="03_06">

- To get the length of a `Doc` object, you can call Python's built-in `len()`
  method on it.
- Use the `nlp.add_pipe` method to add the component to the pipeline. Remember
  to set the `first` keyword argument to `True` to make sure it's added before
  all other components.
- To process a text, call the `nlp` object on it.

</codeblock>

</exercise>

<exercise id="7" title="Reactance Theory">

In this exercise, you'll be writing a custom component that uses the
`PhraseMatcher` to find animal names in the document and adds the matched spans
to the `doc.ents`. A `PhraseMatcher` with the animal patterns has already been
created as the variable `matcher`.

- Define the custom component and apply the `matcher` to the `doc`.
- Create a `Span` for each match, assign the label ID for `"ANIMAL"` and
  overwrite the `doc.ents` with the new spans.
- Add the new component to the pipeline _after_ the `"ner"` component.
- Process the text and print the entity text and entity label for the entities
  in `doc.ents`.

<codeblock id="03_07">

- Remember that the matches are a list of `(match_id, start, end)` tuples.
- The `Span` class takes 4 arguments: the parent `doc`, the start index, the end
  index and the label.
- To add a component after another, use the `after` keyword argument on
  `nlp.add_pipe`.

</codeblock>

</exercise>

<exercise id="8" title="Framing" type="slides,video">

<slides source="chapter3_03_extension-attributes" start="29:16" end="32:23">
</slides>

</exercise>

<exercise id="9" title="Inoculation Theory">

Let's practice setting some extension attributes.

### Step 1

- Use `Token.set_extension` to register `"is_country"` (default `False`).
- Update it for `"Spain"` and print it for all tokens.

<codeblock id="03_09_01">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

### Step 2

- Use `Token.set_extension` to register `"reversed"` (getter function
  `get_reversed`).
- Print its value for each token.

<codeblock id="03_09_02">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="So many Theories: Which one to chose?">

Let's try setting some more complex attributes using getters and method
extensions.

### Part 1

- Complete the `get_has_number` function .
- Use `Doc.set_extension` to register `"has_number"` (getter `get_has_number`)
  and print its value.

<codeblock id="03_10_01">

- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.
- The `get_has_number` function should return whether any of the tokens in the
  `doc` return `True` for `token.like_num` (whether the token resembles a
  number).

</codeblock>

### Part 2

- Use `Span.set_extension` to register `"to_html"` (method `to_html`).
- Call it on `doc[0:2]` with the tag `"strong"`.

<codeblock id="03_10_02">

- Method extensions can take one or more arguments. For example:
  `doc._.some_method("argument")`.
- The first argument passed to the method is always the `Doc`, `Token` or `Span`
  object the method was called on.

</codeblock>

</exercise>

<exercise id="11" title="Hands-On: Writing the Theory-Section and Crafting a Message Brief">

In this exercise, you'll combine custom extension attributes with the model's
predictions and create an attribute getter that returns a Wikipedia search URL
if the span is a person, organization, or location.

- Complete the `get_wikipedia_url` getter so it only returns the URL if the
  span's label is in the list of labels.
- Set the `Span` extension `"wikipedia_url"` using the getter
  `get_wikipedia_url`.
- Iterate over the entities in the `doc` and output their Wikipedia URL.

<codeblock id="03_11">

- To get the string label of a span, use the `span.label_` attribute. This is
  the label predicted by the entity recognizer if the span is an entity span.
- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.

</codeblock>

</exercise>
