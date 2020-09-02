---
title: 'Chapter 4: Getting the word out'
description:
  "In this chapter, you'll learn how to disseminate messages effectively and how to implement your campaign in a professional manner. You'll learn how analyze social networks and identify important people or organizations, along with tips and tricks that can make your campaign more cost-effective and impactful."
prev: /chapter3
next: /chapter5
type: chapter
id: 4
---

<exercise id="1" title="Exposure as the cornerstone of communication effects" type="slides,video">

<slides source="chapter4_01_training-updating-models" start="35:02" end="38:495">
</slides>

</exercise>

<exercise id="2" title="Social Networks">

While spaCy comes with a range of pre-trained models to predict linguistic
annotations, you almost _always_ want to fine-tune them with more examples. You
can do this by training them with more labelled data.

What does training **not** help with?

<choice>

<opt text="Improve model accuracy on your data.">

If a pre-trained model doesn't perform well on your data, training it with more
examples is often a good solution.

</opt>

<opt text="Learn new classification schemes.">

You can use training to teach the model new labels, entity types or other
classification schemes.

</opt>

<opt text="Discover patterns in unlabelled data." correct="true">

spaCy's components are supervised models for text annotations, meaning they can
only learn to reproduce examples, not guess new labels from raw text.

</opt>

</choice>

</exercise>

<exercise id="3" title="Hands-on: Analyzing Networks">

spaCy's rule-based `Matcher` is a great way to quickly create training data for
named entity models. A list of sentences is available as the variable `TEXTS`.
You can print it to inspect it. We want to find all mentions of different iPhone
models, so we can create training data to teach a model to recognize them as
`"GADGET"`.

- Write a pattern for two tokens whose lowercase forms match `"iphone"` and
  `"x"`.
- Write a pattern for two tokens: one token whose lowercase form matches
  `"iphone"` and a digit using the `"?"` operator.

<codeblock id="04_03">

- To match the lowercase form of a token, you can use the `"LOWER"` attribute.
  For example: `{"LOWER": "apple"}`.
- To find a digit token, you can use the `"IS_DIGIT"` flag. For example:
  `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Diffusion of Innovations">

Let's use the match patterns we've created in the previous exercise to bootstrap
a set of training examples. A list of sentences is available as the variable
`TEXTS`.

- Create a doc object for each text using `nlp.pipe`.
- Match on the `doc` and create a list of matched spans.
- Get `(start character, end character, label)` tuples of matched spans.
- Format each example as a tuple of the text and a dict, mapping `"entities"` to
  the entity tuples.
- Append the example to `TRAINING_DATA` and inspect the printed data.

<codeblock id="04_04">

- To find matches, call the `matcher` on a `doc`.
- The returned matches are `(match_id, start, end)` tuples.
- To add an example to the list of training examples, you can use
  `TRAINING_DATA.append()`.

</codeblock>

</exercise>

<exercise id="5" title="Hands-on: Analyzing Diffusion" type="slides,video">

<slides source="chapter4_02_training-loop" start="39:00" end="42:25">
</slides>

</exercise>

<exercise id="6" title="Assessing Channels">

In this exercise, you'll prepare a spaCy pipeline to train the entity recognizer
to recognize `"GADGET"` entities in a text – for example, "iPhone X".

- Create a blank `"en"` model, for example using the `spacy.blank` method.
- Create a new entity recognizer using `nlp.create_pipe` and add it to the
  pipeline.
- Add the new label `"GADGET"` to the entity recognizer using the `add_label`
  method on the pipeline component.

<codeblock id="04_06">

- To create a blank entity recognizer, you can call `nlp.create_pipe` with the
  string `"ner"`.
- To add the component to the pipeline, use the `nlp.add_pipe` method.
- The `add_label` method is a method of the entity recognizer pipeline
  component, which you've stored in the variable `ner`. To add a label to it,
  you can call `ner.add_label` with the string name of the label, for example
  `ner.add_label("SOME_LABEL")`.

</codeblock>

</exercise>

<exercise id="7" title="Implementing the Campaign">

Let's write a simple training loop from scratch!

The pipeline you've created in the previous exercise is available as the `nlp`
object. It already contains the entity recognizer with the added label
`"GADGET"`.

The small set of labelled examples that you've created previously is available
as `TRAINING_DATA`. To see the examples, you can print them in your script.

- Call `nlp.begin_training`, create a training loop for 10 iterations and
  shuffle the training data.
- Create batches of training data using `spacy.util.minibatch` and iterate over
  the batches.
- Convert the `(text, annotations)` tuples in the batch to lists of `texts` and
  `annotations`.
- For each batch, use `nlp.update` to update the model with the texts and
  annotations.

<codeblock id="04_07">

- To start the training and reset the weights call, the `nlp.begin_training()`
  method.
- To divide the training data into batches, call the `spacy.util.minibatch`
  function on the list of training examples.

</codeblock>

</exercise>

<exercise id="8" title="Implementation best practices">

Let's see how the model performs on unseen data! To speed things up a little, we
already ran a trained model for the label `"GADGET"` over some text. Here are
some of the results:

| Text                                                                                                              | Entities               |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple is slowing down the iPhone 8 and iPhone X - how to stop it                                                  | `(iPhone 8, iPhone X)` |
| I finally understand what the iPhone X 'notch' is for                                                             | `(iPhone X,)`          |
| Everything you need to know about the Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| Looking to compare iPad models? Here’s how the 2018 lineup stacks up                                              | `(iPad,)`              |
| The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple                         | `(iPhone 8, iPhone 8)` |
| what is the cheapest ipad, especially ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics | `(Samsung Galaxy,)`    |

Out of all the entities in the texts, **how many did the model get correct**?
Keep in mind that incomplete entity spans count as mistakes, too! Tip: Count the
number of entities that the model _should_ have predicted. Then count the number
of entities it _actually_ predicted correctly and divide it by the number of
total correct entities.

<choice>

<opt text="45%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

<opt text="60%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

<opt text="70%" correct="true">

On our test data, the model achieved an accuracy of 70%.

</opt>

<opt text="90%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

</choice>

</exercise>

<exercise id="9" title="Let's not forget this: Finances" type="slides,video">

<slides source="chapter4_03_training-best-practices" start="42:36" end="44:55">
</slides>

</exercise>

<exercise id="10" title="Keeping count: Process Evaluation">

Here's an excerpt from a training set that labels the entity type
`TOURIST_DESTINATION` in traveler reviews.

```python
TRAINING_DATA = [
    (
        "i went to amsterdem last year and the canals were beautiful",
        {"entities": [(10, 19, "TOURIST_DESTINATION")]},
    ),
    (
        "You should visit Paris once in your life, but the Eiffel Tower is kinda boring",
        {"entities": [(17, 22, "TOURIST_DESTINATION")]},
    ),
    ("There's also a Paris in Arkansas, lol", {"entities": []}),
    (
        "Berlin is perfect for summer holiday: lots of parks, great nightlife, cheap beer!",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
```

### Part 1

Why is this data and label scheme problematic?

<choice>

<opt text="Whether a place is a tourist destination is a subjective judgement and not a definitive category. It will be very difficult for the entity recognizer to learn." correct="true">

A much better approach would be to only label `"GPE"` (geopolitical entity) or
`"LOCATION"` and then use a rule-based system to determine whether the entity is
a tourist destination in this context. For example, you could resolve the
entities types back to a knowledge base or look them up in a travel wiki.

</opt>

<opt text="Paris should also be labelled as tourist destinations for consistency. Otherwise, the model will be confused.">

While it's possible that Paris, AK is also a tourist attraction, this only
highlights how subjective the label scheme is and how difficult it will be to
decide whether the label applies or not. As a result, this distinction will also
be very difficult to learn for the entity recognizer.

</opt>

<opt text="Rare out-of-vocabulary words like the misspelled 'amsterdem' shouldn't be labelled as entities.">

Even very uncommon words or misspellings can be labelled as entities. In fact,
being able to predict categories in misspelled text based on the context is one
of the big advantages of statistical named entity recognition.

</opt>

</choice>

### Part 2

- Rewrite the `TRAINING_DATA` to only use the label `"GPE"` (cities, states,
  countries) instead of `"TOURIST_DESTINATION"`.
- Don't forget to add tuples for the `"GPE"` entities that weren't labeled in
  the old data.

<codeblock id="04_10">

- For the spans that are already labelled, you'll only need to change the label
  name from `"TOURIST_DESTINATION"` to `"GPE"`.
- One text includes a city and a state that aren't labeled yet. To add the
  entity spans, count the characters to find out where the entity span starts
  and where it ends. Then add `(start, end, label)` tuples to the entities.

</codeblock>

</exercise>
