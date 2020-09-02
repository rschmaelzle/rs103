---
title: 'Chapter 1: Campaigns: Goals, Past and Present '
description:
  "This chapter will introduce you to the role of Mass Communication within Public Health.
  You'll learn about the history of public communication campaigns, how to set goals that can tell you whether the camaign was successful, and how the new public communication environment (including social media) changes the face, but not the substance of the campaign process."
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introduction" type="slides,video">

<slides source="chapter1_01_introduction-to-spacy" start="0:165" end="3:01">
</slides>

</exercise>

<exercise id="2" title="Health communication in the past">

Let's get started and try out spaCy! In this exercise, you'll be able to try out
some of the 55+ [available languages](https://spacy.io/usage/models#languages).

### Part 1: English

- Import the `English` class from `spacy.lang.en` and create the `nlp` object.
- Create a `doc` and print its text.

<codeblock id="01_02_01"></codeblock>

### Part 2: German

- Import the `German` class from `spacy.lang.de` and create the `nlp` object.
- Create a `doc` and print its text.

<codeblock id="01_02_02"></codeblock>

### Part 3: Spanish

- Import the `Spanish` class from `spacy.lang.es` and create the `nlp` object.
- Create a `doc` and print its text.

<codeblock id="01_02_03"></codeblock>

</exercise>

<exercise id="3" title="Health communication today">

When you call `nlp` on a string, spaCy first tokenizes the text and creates a
document object. In this exercise, you'll learn more about the `Doc`, as well as
its views `Token` and `Span`.

### Step 1

- Import the `English` language class and create the `nlp` object.
- Process the text and instantiate a `Doc` object in the variable `doc`.
- Select the first token of the `Doc` and print its `text`.

<codeblock id="01_03_01">

You can index into a `Doc` the same way you index into a list in Python. For
example, `doc[4]` will give you the token at index 4, which is the fifth token
in the text. Remember that in Python the first index is 0, not 1.

</codeblock>

### Step 2

- Import the `English` language class and create the `nlp` object.
- Process the text and instantiate a `Doc` object in the variable `doc`.
- Create a slice of the `Doc` for the tokens "tree kangaroos" and "tree
  kangaroos and narwhals".

<codeblock id="01_03_02">

Creating a slice of a `Doc` works just like creating a slice of a list in Python
using the `:` notation. Remember that the last token index is _exclusive_ – for
example, `0:4` describes the tokens 0 _up to_ token 4, but not including
token 4.

</codeblock>

</exercise>

<exercise id="4" title="Beyond Communication Science: Multidisciplinary perspectives">

In this example, you'll use spaCy's `Doc` and `Token` objects, and lexical
attributes to find percentages in a text. You'll be looking for two subsequent
tokens: a number and a percent sign.

- Use the `like_num` token attribute to check whether a token in the `doc`
  resembles a number.
- Get the token _following_ the current token in the document. The index of the
  next token in the `doc` is `token.i + 1`.
- Check whether the next token's `text` attribute is a percent sign "%".

<codeblock id="01_04">

To get the token at a certain index, you can index into the `doc`. For example,
`doc[5]` is the token at index 5.

</codeblock>

</exercise>

<exercise id="5" title="Our approach: high-quality and hands-on" type="slides,video">

<slides source="chapter1_02_statistical-models" start="3:12" end="7:01">
</slides>

</exercise>

<exercise id="6" title="Why goals are super-smart" type="choice">

What's **not** included in a model package that you can load into spaCy?

<choice>
<opt text="A meta file including the language, pipeline and license.">

All models include a `meta.json` that defines the language to initialize, the
pipeline component names to load as well as general meta information like the
model name, version, license, data sources, author and accuracy figures (if
available).

</opt>
<opt text="Binary weights to make statistical predictions.">

To predict linguistic annotations like part-of-speech tags, dependency labels or
named entities, models include binary weights.

</opt>
<opt correct="true" text="The labelled data that the model was trained on.">

Statistical models allow you to generalize based on a set of training examples.
Once they're trained, they use binary weights to make predictions. That's why
it's not necessary to ship them with their training data.

</opt>
<opt text="Strings of the model's vocabulary and their hashes.">

Model packages include a `strings.json` that stores the entries in the model's
vocabulary and the mapping to hashes. This allows spaCy to only communicate in
hashes and look up the corresponding string if needed.

</opt>
</choice>

</exercise>

<exercise id="7" title="The campaign project: Introduction">

The models we're using in this course are already pre-installed. For more
details on spaCy's statistical models and how to install them on your machine,
see [the documentation](https://spacy.io/usage/models).

- Use `spacy.load` to load the small English model `"en_core_web_sm"`.
- Process the text and print the document text.

</exercise>

<exercise id="7" title="Writing a problem and goals statement">

The models we're using in this course are already pre-installed. For more
details on spaCy's statistical models and how to install them on your machine,
see [the documentation](https://spacy.io/usage/models).

- Use `spacy.load` to load the small English model `"en_core_web_sm"`.
- Process the text and print the document text.

<codeblock id="01_07">

To load a model, call `spacy.load` on its string name. Model names differ
depending on the language and the data they were trained on – so make sure to
use the correct name.

</codeblock>

</exercise>
