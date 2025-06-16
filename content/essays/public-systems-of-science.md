---
title: "The Bazaar of Scientific Knowledge"
series: "SciOS"
author: "Ashish Uppala"
date: "June 2025"
abstract: "What's an alternative to the Cathedral of the Scientific Paper, and how can unbundling the paper transfer power back to scientists?"
---

#### NOTE! This is just a draft, but is under review and might be published elsewhere if accepted. Sharing here to avoid the irony!

> I believed that the most important software [...] needed to be built like cathedrals, carefully crafted by individual wizards or small bands of mages working in splendid isolation... the Linux community seemed to resemble a great babbling bazaar of differing agendas and approaches out of which a coherent and stable system could seemingly emerge. - Eric Raymond, The Cathedral and the Bazaar

Not too long ago, there was one dominant way to build software: highly centralized, hierarchical, meticulously planned, opaque. Eventually, a new decentralized mechanism to coordinate those involved emerged within the Linux ecosystem. It was Darwinian, the way ideas surfaced, got developed, and were maintained over time. Though it seemed chaotic from the outside, there was a seductive fluidity, and this new system proved far more adaptive and transparent.

This exact tension exists in our systems of science today: slow, siloed, seemingly static. Great science still happens – this is the same system that gave us CRISPR, CAR-T cell therapy, and so much more.

Yet as I reflect on Eric Raymond's analysis in *The Cathedral and the Bazaar*, I can't help but wonder: what if science, too, operated in a more public and fluid way? Where researchers share knowledge as it emerges, not just after it's polished? Could such a system unlock even more transformative discoveries?

### The Cathedral of the Scientific Paper

Back in my research days, we'd have weekly lab meetings with our team of overworked, underpaid, unbelievably brilliant scientists.

We'd share updates on experiments and hypotheses, discussed a new paper someone published about a really specific immune target, and show off what we knew, all while devouring glorious free food: donuts, bagels, coffee.

We held each other accountable, and learned from one another. All that juicy knowledge tucked away in each of our brains.

> "No, no, you can't trust that paper. That PI always fudges their data in these ways. See? I'm not sure we can incorporate those ideas into our own experiments."


> "Hmm. It'd be interesting if we could induce liver cancer in mice with underlying cirrhosis. We already have a way of doing the latter with CCL4. What about an AAV-8 mediated approach?"

I wish I recorded these conversations (well, parts of them). Across all labs. And then indexed them to be discovered by others.

Instead, the knowledge from that months to years long process of hypothesizing and running experiments, constantly refined through ongoing discussions and tinkering with our entire team, was collapsed into one paper.

We'd finish a draft, submit it for peer review, and then after a few more months of back and forth (at a minimum), our revised, typeset manuscript would be beautifully displayed as a PDF for others. Hopefully with the word  `nature` somewhere in the header. And a list of authors, where the first and last got the bulk of the credit and the rest were just there, doing who knows what.

Does it really have to be this way?

### Publish the Knowledge, Not Just the Paper

Indeed many have lamented the problems plaguing science. Solutions have been difficult, because unlike classic software where users flock to better products and services, this ecosystem is gripped by a career incentive system where papers, and the citations they accrue, are still the dominant currency for grants, promotions, tenure, and prestige.

Communities of scientists have long recognized these problems and attempted to address it from within. Physicists started making their own findings accessible faster in the early 90s, which eventually turned into arXiv. Today, we have a number of preprint servers from bioRxiv, chemRxiv, medRxiv that allow scientists in their respective fields to share their publications before peer-review.

Though preprints were an important step in making science more accessible, they continued to treat the paper as the fundamental output of the scientific process.

That’s not to say that papers should go away - they are valuable for long-form, contextualized descriptions of findings. But we lack a way to share knowledge in a way that reflects how we got there. Science isn’t done in papers, but through ongoing experiments full of discussions, dead ends, and occasional flashes of insight.

What if the paper itself was unbundled into smaller units of knowledge? Stated differently, what if we quickly published smaller units of knowledge, from which we could assemble papers?

[Nanopublications](https://nanopub.net/) were one approach which allowed scientists to share the smallest possible unit of publishable information, such as an individual claim with supporting context. [Though they haven’t seen mainstream adoption](https://arxiv.org/pdf/1303.2446), due in part to career incentive structures, they were another step, like preprints, towards a faster dissemination of scientific knowledge.

Another notable approach that builds on this is the [Discourse Graph](https://joelchan.me/assets/pdf/Discourse_Graphs_for_Augmented_Knowledge_Synthesis_What_and_Why.pdf), which was originally described by Dr. Joel Chan and is being tested as a [new, usable protocol](https://discoursegraphs.com/) for researchers to document and share their own knowledge -- within their labs and outside.

Discourse Graphs, in a way, mimic the research process itself. They model ideas into a modular graph composed of questions, claims, and evidence. Each node can be attributed, versioned, and connected to others, making it possible to track the evolution of thought over time. They enable insights from researchers to be published in smaller chunks - like code commits in software development - while maintaining traceability, credit, and context.

Within the walls of a lab, basic aspects of science - like ramping up new scientists - suddenly become much easier. Back in my day, I snuck into a post-doc’s drive on our shared network to rummage through folders of poorly labeled PDFs!

Now imagine if questions, claims, and findings from lab meetings and experiments were documented in a living, shared, explorable graph, published as they came about at the speed of software, and were unified across all labs. Not buried in notebooks, slides, and brains, but organized and discoverable with proper attribution -- by scientists, and those adjacent.

### The Transformative Potential of the Bazaar

In the 1990s, Martine Rothblatt was the CEO of SiriusXM. Her daughter, Jenesis, had been diagnosed with a terminal illness: Pulmonary Arterial Hypertension (PAH). Determined to find a cure, she famously found relevant research papers, applied citation chaining - or shepardizing, to borrow from law - to trace ideas through older articles, and spotted a key figure in an older paper that might have therapeutic potential.

In [her own words](https://tim.blog/2020/12/17/martine-rothblatt-transcript/):

> Finally, I read about a molecule that a researcher at Glaxo Wellcome had written in which they described testing this molecule for congestive heart failure. And it failed in its test of congestive heart failure. It did not work, but in the article, they had charts of what the molecule did. And the one thing that the molecule did that grabbed my attention was that it reduced the pressure between the lung and the heart, which is called the pulmonary artery. It reduced the pulmonary artery pressure while leaving the pressures and all of the rest of the body perfectly fine. Well, that’s exactly the problem with pulmonary arterial hypertension, the people who have this disease.

She found a paper reporting a negative result in a different disease, spotted a figure directly relevant to PAH, connected the dots, and quickly moved to form a company - United Therapeutics - and brought this new drug into the market.

What if that figure had never been published? How many other figures and insights are tucked away in slides, notebooks, or the minds of individual scientists, but never made the cut in that chaotic process leading up to a polished paper, or preprint?

People have increasingly been saying “do the f@$%ing experiment”. I think it’s high time to publish the questions, experiments, claims, and findings as they come about.

Ideas like Discourse Graphs point to what’s possible: a potential future where scientists and innovators can share knowledge faster and leverage evidence more effectively. One where they can spark transformative insights beyond their own epistemic bubbles, and receive credit that reflects their real contributions.

Such a future isn't about one particular technology, but a shift in how scientists work, new ways of augmenting them with technology, all while preserving the basic tenets of scientific inquiry. It [needs new infrastructure](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4EXyZ14AAAAJ&sortby=pubdate&citation_for_view=4EXyZ14AAAAJ:SIv7DqKytYAC) to ensure scientists, funders, and others are incentivized to openly share knowledge as it's developed.

This future certainly won't be built through top-down, hierarchical coordination. And like the Bazaar, this public version of science may appear messy, but I’ll bet the end result is far more powerful than we’ve dared to imagine.

*This is the first part of a series where I conceptually explore a future of science where augmented scientists work iteratively, in public, and the sort of things that have to be systemically true to support that future. I'd love to hear from anyone excited, or completely appalled, by this. Please get in touch at shishyko@gmail.com*

*Many thanks to Niko McCarthy, John Wilbanks, and Karthik Ram for listening to me babble about this in recent conversations.*