---
title: "The Bazaar of Scientific Knowledge"
series: "SciOS"
author: "Ashish Uppala"
date: "June 2025"
abstract: "Is the current form of the scientific paper still optimal in 2025? How do we preserve, and efficiently leverage, the uncut gems of the scientific process?"
---

> I believed that the most important software [...] needed to be built like cathedrals, carefully crafted by individual wizards or small bands of mages working in splendid isolation... the Linux community seemed to resemble a great babbling bazaar of differing agendas and approaches out of which a coherent and stable system could seemingly emerge. - Eric Raymond, The Cathedral and the Bazaar

Not too long ago, there was one dominant way to build software: highly centralized, hierarchical, meticulously planned, opaque. Eventually, a new decentralized mechanism emerged within the Linux ecosystem. It was Darwinian, the way ideas surfaced, evolved, and endured. Though it seemed chaotic from the outside, it proved far more adaptive and transparent

Our current system of science is similarly slow, siloed, and centered around crafted, polished papers. A process that was optimized for a different era. And though this system gave us breakthroughs like CRISPR, CAR-T cell therapy, and so much more, as I reflect on Eric Raymond’s analysis in *The Cathedral and the Bazaar*, I can’t help but wonder how much more we could achieve if we borrowed lessons from the Bazaar for science, too.

By rethinking how we represent knowledge at a level deeper than the paper and properly tracking and crediting intellectual contributions of authors, we can lay a new foundation that unlocks a future of science which reflects how science actually happens, with more collaboration, faster iteration, and efficient, transformative discovery.

### Polish and Perish: The Cathedral Erases Knowledge 

In my research days, we'd have weekly lab meetings with our team of overworked, underpaid, unbelievably brilliant scientists.

We'd share updates on experiments and hypotheses, discuss a new paper someone published about a really specific immune target, and show off what we knew.

These meetings were, in a way, our weekly bazaars. Sometimes structured, sometimes chaotic. Full of food – donuts, bagels, and coffee. We didn’t just run off and work by ourselves for months. We had to iterate. Propose experiments, discuss them. It’s how we learned from one another and held each other accountable. All that juicy knowledge tucked away in each of our brains.

> "No, no, you can't trust that paper. That PI always fudges their data in these ways. See? I'm not sure we can incorporate those ideas into our own experiments."


> "Hmm. It'd be interesting if we could induce liver cancer in mice with underlying cirrhosis. We already have a way of doing the latter with CCL4. What about an AAV-8 mediated approach?"

I wish I recorded these conversations (well, parts of them).

Instead, the knowledge from our months or sometimes years of hypothesizing and running experiments, constantly refined through discussions and tinkering with our entire team, was lost. At best it was trapped in lab notebooks and powerpoint slides, never to be looked at again by a person, or a machine.

Over a period of months to years, we’d analyze data, finish a draft, submit it for peer review, and then get a revised, typeset manuscript that would be beautifully displayed as a PDF. For human eyes only.

Future readers would never know how we got there, only what we chose to include after some intellectual arm-wrestling with our editor and reviewers.

What detours did we take in that process of coming up with hypotheses that sometimes feels like a large-language model hallucinating? Which of those were dead ends? Why? How did we know not to try a certain approach? In what ways did we troubleshoot failures? And of all the authors on this paper, who actually contributed to which parts, intellectually or otherwise?

Science isn’t done in papers. And their existing format, while well-intentioned, doesn’t adequately capture different types of knowledge that’s generated in the scientific process. To publish today is to polish, and in polishing, we erase. We need to preserve the uncut gems of the scientific process.

### Publish Discrete Knowledge Units, Not Just the Paper

The familiar form of the scientific paper - Introduction, Methods, Results, and Discussion - solved a real problem: it gave scientists a predictable structure to clearly communicate their work, with context, and ensured others could reproduce their experiments. Papers became a way of representing our cumulative knowledge, as peers within fields built off of their collective understanding and approximation of reality.

Before the internet, this infrastructure, or substrate for knowledge, was organized at _people scale_: the natural limits at which a group of people can reasonably organize and do things.

But technology transformed what’s possible, and a system that evolved over decades on outdated assumptions couldn’t keep pace.

Communities of scientists have long recognized that this system slowed down communication with increasingly longer review cycles and attempted to address it from within. Physicists started making their own findings accessible faster in the early 90s, which eventually turned into arXiv. Today, we have a number of preprint servers from bioRxiv, chemRxiv, medRxiv that allow scientists in their respective fields to share their publications before peer-review.

Though preprints were an important step in improving the speed of knowledge sharing (long peer-review times) and accessibility of research (paywalls), they continued to treat the paper as the fundamental output of the scientific process, bundling the introduction, methods, results, and discussion as one.

What if the paper itself was decomposed into smaller units of knowledge? Stated differently, what if we published smaller units of knowledge, from which we could assemble papers, and synthesize new ideas?

Some early efforts have tried to move in this direction. There are [nanopublications](https://nanopub.net/), which allow scientists to share the smallest possible unit of publishable information, such as an individual claim with supporting context.

[Discourse Graphs](https://joelchan.me/assets/pdf/Discourse_Graphs_for_Augmented_Knowledge_Synthesis_What_and_Why.pdf), developed by Dr. Joel Chan and others, mimic the research process itself: iteratively asking questions and attempting to invalidate hypotheses. They model ideas into a modular graph composed of questions, claims, and evidence. Each node can be attributed, versioned, and connected to others, making it possible to track the evolution of thought over time. They enable insights from researchers to be published in smaller chunks - like code commits in software development - while maintaining traceability, credit, and context.

While these new approaches show promise in re-calibrating what counts as “publishable”, what they lack are reasons for adoption, positioning for scale across and within disciplines, a pathway for interoperability with existing scientific infrastructure today, and top-down support from funders to help drive change.

### Infrastructure for Scientific Collaboration at Scale

What's necessary is infrastructure that goes beyond letting researchers track questions, claims, and evidence in their note-taking tools. One which unifies that granular element of scientific inquiry in a centralized graph with permission boundaries for public domain, the scope of a lab, and so on.

Of course, not everything in research is text: sometimes we have datasets, complex figures, videos, so multimodal support is essential. And like existing science, it would need the concept of citations, not just between papers to papers, but expanded to more types of nodes in the graph, e.g. to a type of dataset, software, or chart.

Authorship would be tracked similar to code commits (think of github), unlocking new ways of recognizing the contributions of individual scientists. There’s no reason that career outcomes in science should be as bimodally distributed as they are. Imagine a more liquid job market for researchers, who can easily point to the thing they did and meaningfully demonstrate its downstream impact to have more optionality in their careers.

Knowledge units could - perhaps automatically - be synthesized into a longer, narrative representation that contextualizes the problem, what the results are (assembled through each building block), and offer a discussion. Multiple blocks of knowledge units could stack into a paper, while individual blocks and papers would generally broaden the surface area for transformative insight.

New investigators could easily narrow in on the part of a field they were interested in and trace ideas more naturally. Back in my day, I was secretly logging into drives of postdocs on our shared network and rummaging through folders of poorly named PDFs!

Most ideas around interventions for metascience fall short when positioned as a replacement for something that everyone is incentivized to keep. This new stack wouldn’t have to be a replacement, but a viable alternative that proves its value over time.

Does this mean that every researcher suddenly has to adopt yet another new tool? Not necessarily. A common data infrastructure means that AI agents could parse your notes or powerpoint slides, wherever they were, generate these more granular units, and bring them into the central graph (with your review). It’d even be possible to leverage state of the art reasoning models to map existing knowledge published across all scientific papers (PDFs, XML, even OCR’d documents) into this new structure so scientists don’t lose anything by moving over.

This new stack would support different types of knowledge. Science today only distributes the type of knowledge that makes it through the publication gauntlet. What about negative results that didn’t make the cut, which are equally important? Or other types of arguments and tacit knowledge that are crucial for understanding something, discussed in lab meetings as a way to teach new researchers, but aren’t distributed evenly across each field?

Unlike our existing stack, this one would enable AI agents to efficiently reason across claims, connect distant fields, and propose new experiments based on the right primitives for each field.

Most importantly, this isn't primarily a technical problem, but a social one. Funders and universities have an important role in driving the adoption of new forms of sharing research, and creating new ways to help investigators demonstrate the impact of their work.

Some of this is already happening in fragmented ways across disciplines and across the ecosystem. Consider computational fields that embrace open science and create public datasets for sharing and reuse by others, which opens new doors for communicating researcher impact (how many times a dataset was used, where it was used, etc.). How do we extend that to different types of knowledge in a way that can scale?

The core of this new data model - sharing individual units of knowledge - brings us full circle to an earlier mode of scholarly communication before *IMRaD* - but now with modern infrastructure and guardrails that enforce data quality and consistency while preserving authorship attribution and invention priority.

Scientific papers would still have a place, but as structured outputs of a deeper, more granular, shared substrate of scientific knowledge.

Imagine if questions, claims, and findings from lab meetings and experiments were documented in a living, explorable graph, published as they came about, and were unified across all labs. Not buried in notebooks, slides, and brains, but organized and discoverable with proper attribution -- by scientists, and those adjacent.

### The Transformative Potential of the Bazaar

In the 1990s, Martine Rothblatt was the CEO of SiriusXM. Her daughter, Jenesis, had been diagnosed with a terminal illness: Pulmonary Arterial Hypertension (PAH). Determined to find a cure, she famously found relevant research papers, applied citation chaining - or shepardizing, to borrow from law - to trace ideas through older articles, and spotted a key figure in an older paper that might have therapeutic potential.

In [her own words](https://tim.blog/2020/12/17/martine-rothblatt-transcript/):

> Finally, I read about a molecule that a researcher at Glaxo Wellcome had written in which they described testing this molecule for congestive heart failure. And it failed in its test of congestive heart failure. It did not work, but in the article, they had charts of what the molecule did. And the one thing that the molecule did that grabbed my attention was that it reduced the pressure between the lung and the heart, which is called the pulmonary artery. It reduced the pulmonary artery pressure while leaving the pressures and all of the rest of the body perfectly fine. Well, that’s exactly the problem with pulmonary arterial hypertension, the people who have this disease.

She found a paper reporting a negative result in a different disease, spotted a figure directly relevant to PAH, connected the dots, and quickly moved to form a company - United Therapeutics - and brought this new drug into the market.

What if that figure had never been published? How many other figures and insights are tucked away in slides, notebooks, or the minds of individual scientists, but never make the cut in that chaotic process leading up to a polished paper, or preprint? What tacit knowledge do scientists have that would help them quickly invalidate a published experimental result, that an outsider like Martine might not have?

People have increasingly been saying “do the f@$%ing experiment”. I think it’s high time to publish the questions, experiments, claims, and findings as they come about.

By re-thinking the underlying representation of knowledge, and the funding and technology stack that helps us maintain and scale it, we can move towards a future where knowledge is shared faster, and where we're able to leverage evidence much more effectively. One where scientists can spark transformative insights beyond their own epistemic bubbles, and receive credit that reflects their real contributions.

Such a future isn't about one particular technology, but a shift in how scientists work, new ways of augmenting them with technology, all while preserving the basic tenets of scientific inquiry. It [needs new infrastructure](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4EXyZ14AAAAJ&sortby=pubdate&citation_for_view=4EXyZ14AAAAJ:SIv7DqKytYAC) to ensure scientists, funders, and others are incentivized to openly share knowledge as it's developed.

This future certainly won't be built through top-down, hierarchical coordination. Like the Bazaar, this public version of science may appear messy. But I’ll bet the end result is far more powerful than we’ve dared to imagine.

---

*This is part of a series where I conceptually explore a world where augmented scientists work iteratively, in public, and the sort of things that have to be systemically true to support that future. I'd love to hear from anyone excited, or completely appalled, by this. Please get in touch at shishyko@gmail.com*

*Many thanks to Niko McCarthy, John Wilbanks, and Karthik Ram for their thoughtful responses to my incoherent babbling.*

_This is a continuation of [A New Scientific Operating System](https://www.shishyko.com/essays/scientific-operating-system.html). To subscribe to the newsletter, fill out your email [at the bottom of the page](https://www.shishyko.com/index.html#contact)._