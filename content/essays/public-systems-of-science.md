---
title: "Public Systems of Science"
series: "SciOS"
author: "Ashish Uppala"
date: "June 2025"
abstract: "How can we unbundle a paper to transform science from a Cathedral into a Bazaar, and transfer power back to scientists?"
---

#### NOTE! This is just a draft! The final version is under review and will be published elsewhere, but sharing in the spirit of feedback.

> I believed that the most important software [...] needed to be built like cathedrals, carefully crafted by individual wizards or small bands of mages working in splendid isolation... the Linux community seemed to resemble a great babbling bazaar of differing agendas and approaches out of which a coherent and stable system could seemingly emerge. - Eric Raymond, The Cathedral and the Bazaar

Not too long ago, there was only "one correct way" to build software: highly centralized, hierarchical, meticulously planned, opaque. Eventually, a new decentralized mechanism to coordinate those involved emerged within the Linux ecosystem. It was almost Darwinian - the way ideas surfaced, got developed, and were maintained over time. Though it seemed chaotic from the outside, there was a seductive fluidity, and this new system proved far more adaptive and transparent.

This exact tension exists in our systems of science today. Traditionally slow, siloed, static. Great science still happens - this is after all a system that gave us CRISPR, CAR-T cell therapy, and so much more.

But how much better could it be?

Reflecting on Eric Raymond's analysis in *The Cathedral and the Bazaar*, I can't help but wonder: what if science, too, operated in a more public and fluid way? Where researchers share knowledge as it emerges, not just after it's polished? Could such a system unlock even more transformative discoveries?

### The Cathedral of Science

Back in my research days, we'd have weekly lab meetings with our team of overworked, underpaid, unbelievably brilliant scientists.

We'd share updates on experiments and hypotheses, chat about a new paper someone published about a really specific immune target, and show off what we knew, all while devouring glorious free food: donuts, bagels, coffee.

We held each other accountable, and learned from one another. All that juicy knowledge tucked away in each of our brains.

> "No, no, you can't trust that paper. That PI always fudges their data in these ways. See? I'm not sure we can incorporate those ideas into our own experiments."


> "Hmm. It'd be interesting if we could induce liver cancer in mice with underlying cirrhosis. We already have a way of doing the latter with CCL4. What about an AAV-8 mediated approach?"

I wish I recorded these conversations. Across all labs. And then indexed them to be discovered by others.

Instead, the knowledge contained within that months to years long process of hypothesizing and running experiments, constantly refined through ongoing discussions and tinkering with our entire team, was collapsed into one paper.

We'd finish a draft, submit it for peer review, and then went through yet another opaque process that took months with editing, revisions, sometimes new experiments.

Eventually, months or years later, our revised, typeset manuscript would be beautifully displayed for others. Hopefully with the word `nature` somewhere in the header. And a list of authors, where the first and last got the bulk of the credit and the rest were just there, doing who knows what.

Does it really have to be this way?

### The Experiment is our Building Block

Indeed many have lamented the problems plaguing science. Solutions have been difficult, because unlike classic software where users flock to better products and services, this ecosystem is gripped by a career incentive system comprised of universities and publishers.  Papers, and the citations they accrue, are still the dominant currency for grants, promotions, and tenure.

Communities of scientists have long recognized these problems and attempted to address it from within. Physicists started making their own findings accessible faster in the early 90s, which eventually turned into arXiv. Now, we have a number of preprint servers from bioRxiv, chemRxiv, medRxiv that allow scientists in those fields to share their publications before peer-review.

Though preprints were an important step in making science more accessible, they continued to treat the paper as the fundamental output of the scientific process.

That’s not to say that papers should go away - they are valuable for long-form, contextualized descriptions of findings. But what’s missing is a way to share knowledge sooner. Science isn’t done in papers, but in weekly experiments full of discussions, dead ends, tinkering, refining, and occasional flashes of insight.

Can the paper itself be unbundled into smaller units of knowledge? Stated differently, what if we published smaller units of knowledge, with which we could assemble papers?

New approaches led by researchers are gradually emerging to address some of these ideas. Consider for example [Discourse Graphs](https://joelchan.me/assets/pdf/Discourse_Graphs_for_Augmented_Knowledge_Synthesis_What_and_Why.pdf) which were originally described by Joel Chan and are becoming a [new, usable protocol](https://discoursegraphs.com/) for researchers to share their own knowledge -- within their labs and outside.

Discourse Graphs represent research ideas as modular, interlinked claims: hypotheses, evidence, critiques, questions. Each node can be attributed, versioned, and connected to others, making it possible to track the evolution of thought over time. They enable insights to be published in smaller chunks - like code commits or GitHub issue threads - while maintaining traceability, credit, and context.

Equally important is that the intermediate and final results wouldn’t be locked away in PowerPoints and PDFs – two formats that are notoriously difficult for machine readability.

Imagine if every lab meeting, idea, brainstorming session, experimental decision lived in such a shared, explorable graph. Not buried in notebooks or brains, but organized, attributed, and discoverable -- by your future self, your peers, and the broader scientific community.

### Public Science has Transformative Potential

In the 1990s, Martine Rothblatt was the CEO of SiriusXM. Her daughter, Jenesis, had been diagnosed with a terminal illness: Pulmonary Arterial Hypertension (PAH). Determined to find a cure, she famously found relevant research papers, applied citation chaining - or shepardizing, to borrow from law - to trace ideas through older articles, and spotted a key figure in an older paper that might have therapeutic potential.

In [her own words](https://tim.blog/2020/12/17/martine-rothblatt-transcript/):

> Finally, I read about a molecule that a researcher at Glaxo Wellcome had written in which they described testing this molecule for congestive heart failure. And it failed in its test of congestive heart failure. It did not work, but in the article, they had charts of what the molecule did. And the one thing that the molecule did that grabbed my attention was that it reduced the pressure between the lung and the heart, which is called the pulmonary artery. It reduced the pulmonary artery pressure while leaving the pressures and all of the rest of the body perfectly fine. Well, that’s exactly the problem with pulmonary arterial hypertension, the people who have this disease.

She found a paper that wasn’t about PAH, spotted an individual chart directly relevant to the disease, connected the dots, and quickly moved to form a company - United Therapeutics - and brought this new drug into the market.

What if that figure had never been published? How many other figures and insights are tucked away in powerpoint slides, lab notebooks, minds of individual scientists, in that chaotic process leading up to a polished paper?

Innovations like Discourse Graphs point to what’s possible: a future where scientists and innovators can scale with the explosion of information, receive credit that reflects their real contributions, and spark transformative insights beyond their own epistemic bubbles.

This isn’t just about individual protocols, but a broader, public system of science, where knowledge is shared as it’s built, not only after it’s polished; where collaboration happens across the epistemic confines of labs and disciplines, not just within them; and where the system of scientific invites openness and reuse without compromising credit.

It’s time to publish the experiment. To enable public work by creating a new infrastructure where scientists, funders, investors, and innovators can build, share, and evolve ideas together, in the open. Like the Bazaar, it may be messy – but I'll bet it's far more powerful than we’ve dared to imagine.

If you'd like to develop some of these thoughts further, or are working on some of these problems, get in touch at ashish.uppala.93@gmail.com.


*Many thanks to Niko McCarthy, John Wilbanks, and Karthik Ram for ongoing discussions which helped cement these ideas.*