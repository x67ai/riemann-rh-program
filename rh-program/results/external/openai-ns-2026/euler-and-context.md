# Euler blowup and context: OpenAI (unforced Euler), Alpöge–Buckmaster (forced IPM / Boussinesq / Euler), and what the RH program can learn

Reader agent: `euler-context`. Written 2026-09-09. U.S. English. Every claim is tagged with its source; "I infer" marks my own reasoning.

## 0. Provenance of what was read

| Item | How obtained | Result |
|---|---|---|
| (a) `fetched-r4/openai-ns/openai-euler-2026-09-08.pdf` | local, `pdftotext -layout`; page 1 rendered and vision-checked | 57 pp, pdfTeX, no title/author metadata; CreationDate `Wed Sep 9 00:37:51 2026 IST` (= 19:07 UTC Sep 8) |
| (b) Tao's post of 2026-09-07 | `curl` of the WordPress page, HTML stripped; 24 comments captured | full text |
| (c) Buckmaster statement | `curl` of `cims.nyu.edu/~tristanb/statement.pdf`, 4 pp, `pdftotext` | full text |
| (c) Buckmaster homepage | `curl` | biography, grants, Quanta press links only; no preprint links (the preprints were linked from his Mastodon post, found via Tao's post) |
| (c) Preprints | `curl` from `cims.nyu.edu/~tristanb/{euler,ipm,boussinesq}.pdf` into `fetched-r4/openai-ns/alpoge-buckmaster-{euler,ipm,boussinesq}.pdf` | euler 112 pp (CreationDate Sep 8 04:34 IST), boussinesq 76 pp (Sep 8 06:52 IST), ipm 57 pp (Sep 8 09:06 IST) |
| (d) `github.com/tristanbuckmaster/fluid_lean` | GitHub REST API + raw README files (no top-level README exists; each of three sub-projects has one) | full READMEs, `formalization.yaml`, toolchain, tree |
| (e) Axios | Cloudflare JavaScript wall on both WebFetch and curl; **blocked, not read** | — |
| (e) OpenAI announcement `openai.com/index/navier-stokes-solution/` | direct fetch blocked (JS wall); read through the `r.jina.ai` text proxy | full text |
| (e) Quanta (2026-09-08), TechCrunch (2026-09-08), Scientific American (2026-09-08) | WebFetch summaries | facts and quotes below |
| (e) Buckmaster's Mastodon (`mastodon.social/@tristanbuckmaster`) | RSS feed via curl | four posts, Sep 8 |

Nothing was fabricated to fill the Axios gap; the dispute facts come from Buckmaster's statement, OpenAI's own page, Quanta, TechCrunch and SciAm.

---

## A. OpenAI, "Finite time blowup for the Euler equation" (57 pp)

### A.1 The main theorem, verbatim (vision-checked against the rendered page 1)

Abstract: "We exhibit finite-time blowup for the three-dimensional incompressible, unforced Euler equations from smooth, compactly supported, divergence-free initial data."

Setting (1.1): ∂_t u + (u·∇)u + ∇p = 0, ∇·u = 0, u(·,0) = u_0 on R^3. Definition (1.2): C^∞_{c,σ}(R^3) = {u_0 ∈ C^∞_c(R^3; R^3) : ∇·u_0 = 0}; T_*(u_0) is the maximal lifespan of the smooth Euler solution.

"**Theorem 1.1.** There exists u_0 ∈ C^∞_{c,σ}(R^3) such that 0 < T_*(u_0) < ∞. Its smooth Euler solution satisfies

  limsup_{t↑T_*} ‖∇u(t)‖_{L^∞} = ∞,   ∫_0^{T_*} ‖curl u(t)‖_{L^∞} dt = ∞."

The second conclusion is exactly the Beale–Kato–Majda divergence, which the paper notes is necessary for breakdown (§1.1).

### A.2 Proof architecture, in plain terms

The paper's own outline (§2, "The amplification mechanism and proof order") is an inductive cascade:

1. Start from a smooth, odd, compactly supported base Euler flow U_B (§5.1). Oddness pins the origin as a fixed particle: X(t,0)=0.
2. At stage j, take the parent flow U_{j−1} and add a "packet": a localized, high-frequency oscillation of the form (2.5), w_lead = (ℓα/k) χ_1(y) v(t,y) f_δ(k m_0·y), written in particle (Lagrangian) coordinates so its phase is frozen. Its phase normal m and amplitude v obey the WKB-type leading system (2.4): m_t = −M^T m, v_t = −Mv + 2m (m·Mv)/|m|^2, with M = ∇u along the trajectory. The paper attributes this leading system to Lifschitz–Hameiri and Friedlander–Vishik [28, 21] (local instability of inviscid flow) and the nonlinear phase-correction idea to Cheverry [8].
3. The parent's velocity gradient at the origin contains a rank-one shear h q p^T; this shear rotates m and amplifies v (Proposition 4.1, "Amplification and transfer of the wave geometry"). At the target time t_j the packet's own leading gradient αδ^{−1} v⊗m becomes the shear for the next packet: "Choosing α makes the new leading rank-one gradient the parent shear for the next packet" (§2.1). The paper credits the parent-child layer idea explicitly: "Córdoba and Martínez-Zoroa also use a vorticity layer to amplify a more localized layer in their forced Euler construction [10, §1.2]."
4. The essential difference from forced constructions: the packet is corrected to an **exact** Euler solution rather than absorbing the residual into a force. Proposition 3.1 builds mean and oscillatory corrections as a finite series in k^{−1} with the phase θ treated as an independent variable on R^3×T (a two-scale/homogenization device, §2.1 and §3.5), then Lemma 3.3 "constructs a further correction that cancels this error" (§2.1) using Gevrey-order-2 weighted derivative norms (§2.4, (3.43)). Because every derivative order must be controlled at once, the analysis carries factorial bounds `|f|_n ≤ C R^n (n!)^2` throughout.
5. A global constraint is maintained through all stages: the pressure Hessian satisfies ∇²p_j ≤ K_+ I (§2, §2.2), used for coercivity of the displacement boundary-value problem that selects each packet's history (3.11).
6. Scales are chosen (§5) so that the initial-data increments are summable in every H^m: (2.1) states |∇U_j(t_j,0)| → ∞ while Σ_j ‖U_j(0)−U_{j−1}(0)‖_{H^m} < ∞. Section 6 passes to the limit u_0 = lim U_j(0) (6.3), shows by H^3 stability that a smooth solution past the accumulation time T_∞ would inherit the unbounded gradients (6.5)–(6.6), and proves the two continuation conclusions (§6.3, with the log-Lipschitz bound (6.7)).

Figure 1 is a flowchart of exactly this loop. Only two named propositions (3.1, 4.1) and a handful of lemmas carry the argument; Proposition 3.1 is split into "Claims 1–3".

**Technique family (my classification).** Córdoba–Martínez-Zoroa multiscale layer cascade (their refs [10] forced Euler, [11] IPM, [13] Euler C^{1,α}) + WKB/geometric-optics local instability along a Lagrangian trajectory (Lifschitz–Hameiri; Friedlander–Vishik) + exact two-scale nonlinear correction in Gevrey classes (Cheverry-style) so that no external force is needed. The paper also positions itself against the self-similar school (Elgindi [15]; Elgindi–Ghoul–Masmoudi [16]; Chen–Hou [6,7] with boundary; Chen and Shkoller 2026 preprints [5, 29]) and the Craik–Criminale exact-wave line [14, 20, 25].

### A.3 What it presents as new

The paper makes one explicit priority claim: "For smooth initial data, Chen and Hou [6, 7] proved blowup in an axially periodic cylinder with an impermeable wall, combining analysis with rigorous numerical estimates. Theorem 1.1 treats smooth, compactly supported initial velocities on R^3" (§1.1). I.e. smooth data, whole space, no boundary, no force, no symmetry assumption, finite energy (compact support). It does not claim novelty of mechanism; it credits CM-Z for the layer idea.

### A.4 Citations — who it cites, who it does not

29 references. It cites Córdoba–Martínez-Zoroa [9,10,11], CM-Z–Zheng [13], CM-Z–Ożański [12], Jeong–Martínez-Zoroa–Ożański [23]. It cites Buckmaster only as a coauthor of the Onsager paper [4]. **It does not cite Alpöge–Buckmaster** (any of the three preprints), nor Córdoba–Laín-Sanclemente–Martínez-Zoroa (Boussinesq pendula), nor CM-Z–Zheng hypodissipative NS. This is consistent with OpenAI's statement that the agents "did not see any of their work through any means until they released it publicly" — and also consistent with a document written before Sep 8 and not updated.

### A.5 Signs of machine production

- Author line is literally "OPENAI"; no acknowledgments, funding, AI-use statement, affiliations, date, or arXiv identifier anywhere in the 57 pages. The A–B preprints, by contrast, carry an "AI statement" section and acknowledgments.
- No mention of Lean, formalization, or verification anywhere in the text (grep for `lean`, `formaliz`, `verif` finds only ordinary "verify the hypotheses" uses). The Euler result is therefore, on the evidence of the paper itself, **not formally verified**; OpenAI's page states Lean verification only for the Navier–Stokes result ("Lean formalization and verification took an additional 17 hours").
- Uniform, terse, declarative prose with almost no remarks, no footnotes, no historical asides beyond §1.1; an unusual two-page "Notation index" table (§2.4) that locates every symbol by equation number — the kind of artifact a coordinating system produces to keep many workers consistent.
- Exhaustive constant-tracking of the "P^c, K_h^c, enlarged finitely many times" kind, and Gevrey-2 factorial bookkeeping through every product rule ((3.2), (3.3)) — mechanical thoroughness rather than human economy.
- The "proof order" section (§2.3) with an explicit dependency flowchart (Figure 1) reads like a plan handed to sub-workers.
- Vocabulary such as "verify", "the checks in Section 5.7", "closing the induction" recurs.
- The PDF's creation timestamp (Sep 8, 19:07 UTC) is after the A–B preprints (Sep 7, 23:04 UTC for euler.pdf).

### A.6 Doubts (mine; nothing here is a claim that the proof is wrong)

- Unreviewed and, per the paper, unformalized. The 57-page length for an unforced, whole-space, smooth-data Euler singularity is short relative to the 112-page forced axisymmetric construction by A–B and the ~100 pages OpenAI reports for NS; brevity via Gevrey/two-scale machinery is plausible but is exactly what a referee would test.
- The uniform pressure-Hessian bound H ≤ K_+ I across infinitely many stages, with the whole-space nonlocal pressure ("no spatial locality of the pressure is assumed", §5.7), is the structural hypothesis everything hangs on; the paper's summability argument for it (§5.5, §5.7) is where I would look first.
- The exact-cancellation step (Lemma 3.3) in Gevrey-2 classes with "expansion length N_k = ⌊k^ϑ⌋, ϑ = 10^{−6}" is a delicate small-divisor-free but derivative-hungry construction; whether the weighted norm ‖·‖_ρ closes uniformly in the stage index is the second place to check.
- Buckmaster's Mastodon (Sep 8, 21:32 UTC) implies unforced Euler was already in the air: "our hypodissipative result (which is not public), but as I understand it part of their training data was already pointing to the fact that unforced Euler was possible." Tao (Sep 7): "it should even be possible to do without the forcing term."

---

## B. Terence Tao's post (2026-09-07)

Title: "Finite time blowup with smooth forcing term for the incompressible porous medium, Boussinesq, and incompressible Euler equations". 24 comments as of read.

**What A–B proved, per Tao.** "It is now widely expected that it should be possible to construct smooth initial data and smooth forcing term that would make these equations develop singularities in finite time; and it should even be possible to do without the forcing term. While these authors do not quite achieve these goals yet, they have made enough of a breakthrough that it looks very feasible to complete these goals in the near future. In particular, they have demonstrated such finite time blowup for three simpler model equations: the incompressible porous medium (IPM) equation, the two-dimensional Boussinesq equation, and the three-dimensional incompressible Euler equations. (The first of these equations was already handled by Córdoba and Martínez-Zoroa, but Alpöge and Buckmaster found a variant of their method that also extended to the other two equations, and has a high likelihood of also extending to Navier-Stokes as well.) As is now remarkably feasible in the modern era of autoformalization agents, their work has also been formalized in Lean."

**On AI and the writeup.** "As one may expect nowadays, the arguments here are heavily AI-assisted, but the authors have been working over the last few weeks to simplify and rewrite the proofs from what they literally call 'the worst writeup we had ever seen in the history of mathematics' into something far more readable and of professional quality. This is still a work in progress: unfortunately, they were forced to release their preliminary preprints before they were completely digested and polished, due to external events that are documented on the above link. Nevertheless, the introduction to the Boussinesq paper at least is in pretty good shape, and can serve as an initial starting point. I was also fortunate to have Tristan Buckmaster explain the main ideas of the paper in a half-hour phone conversation, although I still need to work some more (probably with some combination of a blackboard and modern AI tools) to digest things more."

**On what matters.** "the actual solving of these problems is only a proxy goal for the primary goal of developing mathematical understanding and insight. Without such understanding, even a problem as infamous as the Navier-Stokes regularity problem of far less intrinsic significance to mathematics than is sometimes promoted in popular media."

**The method, abstractly (Tao's description of the CM-Z strategy).** "The basic strategy, due to Cordoba and Martínez-Zoroa, is to iteratively build up the solution to such equations in stages, repeatedly adding small high frequency corrections to a previous (forced) solution in a manner that makes the solution more singular towards the blowup time while keeping the forcing term well behaved." With N(u)=f: from N(u_lo)=f_lo build N(u_lo+u_hi)=f_lo+f_hi, "If one can make the amplitude of the solution correction u_hi relatively large while keeping the amplitude of the correction f_hi very low, and the frequencies of the corrections increase rapidly with each iteration, then one can hope to iterate this procedure and pass to a limit". u_hi should approximately solve the linearized equation N'(u_lo)u_hi ≈ 0; "The game is then to design the background solution u_lo in such a way that the evolution equation N'(u_lo) u_hi = 0 exhibits some sort of exploitable instability, in which a solution u_hi to such an equation can start off exponentially small at early times, but become large near the blowup time... if one can time the emergence of large amplitudes just right, one can hope to arrive at a sweet spot where, by the blowup time, the amplitude has become large enough to disrupt smoothness, but not so large to destabilize the analysis."

**The improvements.** "In the case of the Boussinesq equation at least, there is an explicit ansatz... in which, at times close to blowup and locations close to the origin, u_lo behaves linearly in space, and u_hi behaves like a high frequency plane wave. Remarkably, this ansatz can be solved exactly (without any nonlinear correction terms), leading to an explicit system of ODE modulation equations that have the required instability property... The Alpöge–Buckmaster construction has some technical improvements over the older Córdoba–Martínez-Zoroa construction that allow them to treat more general fluid equations; I have not yet digested the precise differences, but the ODEs seem to be more unstable and the high frequency corrections appear to have better spatial localization properties."

**EDIT (Tao).** An independent preprint of Ganeshram, Duruisseaux, and Anandkumar (anima-ai.org, Sep 7) "has made a significant advance on the other major approach to finite time blowup, which is to first use numerical or machine learning tools to locate an approximately self-similar blowup profile ansatz, and then demonstrate that it is stable enough to be perturbed to an actual solution. For the Euler equations (with no forcing term or boundary), they have used a physics-informed neural network (PINN) to locate a numerically stable candidate solution; though actually establishing its stability to within the tolerance of the residual error in the solution remains a major challenging task".

**Comments worth keeping (verbatim where it matters).**
- Ravi Vakil: "a milestone advance in human knowledge. The purpose of mathematics is human understanding".
- Gonzalo Cao-Labora (on GDA's PINN candidate): "the residual of the self-similar profile equation are around 0.004 in L^infty. However, the most relevant quantity in this approach tends to be a higher derivative of that residual... When working on this approach some years ago (with Wang, Buckmaseter, Gomez-Serrano, Lai, and Deepmind) we found solutions with L^infty of that size several times, but they ended up being a roadblock since no smooth solution existed closeby."
- Anonymous: "Would it be surprising if the full Navier-Stokes follows from the same method as Euler equations, but pushing harder?" — unanswered in the thread.
- Anonymous, on "wasn't Euler blowup already proved" (Chen–Hou): "That was with boundary, this is without".
- Sam Hopkins: "Any discussion of this saga which doesn't mention how Buckmaster alleges... that he was threatened by the Open AI people is burying the lede".
- "J": "Julia Stadlmann barely got her improved bound on prime gaps (246 to 240) out the door on August 31st before AI labs started racing to announce their own versions of the same result days later... a field which used to let slow, careful work speak for itself is starting to run on a different clock".
- Anonymous quoting OpenAI's page (the "did not see any of their work" paragraph, reproduced in §E below).
- Anonymous: proposes journals "reject a paper like the Navier-Stokes solution by Open AI because of 'the lack of communication effort despite a formal Lean certificate'".
- Anonymous: "this is the most pressing problem mathematicians face, not Navier-Stokes or the RH or PvNP."

---

## C. Buckmaster's statement (4 pp) and the Alpöge–Buckmaster preprints

### C.1 What they released and what they hold back

"Today, Levent Alpöge and I have made public three results: finite-time blowup with smooth forcing for incompressible porous media, for Boussinesq, and for 3d incompressible Euler. We believe we also have blowup for hypo-dissipative Navier-Stokes. We are not releasing that paper today: unlike the above, the Lean verification has not yet finished. We do not yet have anything resembling a presentable writeup. I mention it because it is suggestive of a path to unforced Euler."

### C.2 Credit

"The program this fits into was not started by us nor was it proposed by a Large Language Model. The credit for the basic idea of this program goes to Diego Córdoba and Luis Martínez-Zoroa, who for several years have been exploring the construction of forced blow ups. We took their work as a starting point, using Large Language Models to push their program to completion... The ideas making this line of attack possible are due to Córdoba and Martínez-Zoroa... I believe Luis Martínez-Zoroa deserves a Fields Medal."

### C.3 The workflow, as the sources state it

Tools: "We used several LLMs throughout: Anthropic's Claude, OpenAI's Codex, especially with GPT-5.6 Sol and, more recently, Astra. The latter was only used for writeups and auditing our arguments." Institutional status: "a purely personal collaboration, free of any institutional agreements or official involvement by either of our employers... I pay for the tools my group uses out of my own research funds, including footing a large bill to OpenAI."

Timeline (statement): "For most of the past year progress was slow. We worked through the literature and upgraded various preliminary results, up to obtaining finite time blow up for the Incompressible Porous Media equation (with smooth forcing). This was until about a month ago, when we had real progress: on August 15th, we obtained the blow up results, with smooth forcing, for both Boussinesq and Euler. I can say the first LLM generated proof Levent sent me was the most horrendous I have ever read; we verified it on Lean on August 22nd. Since this point, we have been working around the clock to understand this proof and turn it into something readable."

Boussinesq paper, §2 "AI statement" (verbatim): "We happily used both Claude and Codex to iterate on our proof. We had, using Claude, our first blowup solution, but not this one, on 8/15/26, and we Lean verified it on 8/22/26. This involved inputting ideas from previous joint work of ours on blowup for the IPM equation following Córdoba–Martínez-Zoroa and a number of other works of ours and others, as well as iteration with the model on various ansätze, eventually leading to blowup in Boussinesq. The first writeup that we produced iterating with Claude was, in our opinion, the worst writeup we had ever seen in the history of mathematics (topped soon after by the writeups for 3d Euler and then for hypodissipative Navier-Stokes). It was then our task to make a presentable and understandable writeup, and we iterated over the weeks on the writeup with Claude and Codex, then via 5.6 Sol. (Throughout our collaboration we have generally input all of our intermediate writeups to Codex for simplification, ideation, and iteration.) After iterating with Claude and Codex on various ideas of ours, including alternative proof architectures, leading to several different proofs, we arrived at the current simplified argument, which we then iterated on using Claude and Codex, first 5.6 Sol and then Astra once we had access, to arrive at the current writeup modulo our hand editing."

IPM paper (Alpöge, Buckmaster, Coiculescu), division of labor (verbatim): "We used Claude to identify the key elements of the previous proof of Córdoba and Martínez-Zoroa and to reproduce their argument. We used Claude and Codex to write the main body of the text, delegating delicate bookkeeping of inductive orders and constants to the models while implementing our ideas for adapting the forced IPM construction of Córdoba and Martínez-Zoroa to the torus and to a space–time smooth force. We used the models in conjunction with our own ideas to reduce the length of initial versions of this work. Claude originally generated an overly complicated version of the result on the whole space following a proof architecture closer in resemblance to Córdoba and Martínez-Zoroa's work. In simplifying the proof, we incorporated many of our own ideas, some of which are inspired by analogous ideas from the convex integration literature. This introduction... was written by the listed authors, but the remainder of the paper was written with the assistance of Claude and Codex, under the strict direction of the authors."

IPM paper §1.1 also records a commitment device: "Both proofs have been formally verified in Lean. To identify the precise formal-proof artifacts underlying this announcement, their SHA-256 hashes are [BOUSSINESQ SHA-256], [EULER SHA-256]." (Placeholders in the released PDF.)

Lean organization (fluid_lean READMEs, verbatim): "all Lean code in this directory, the trusted statement file `Challenge.lean` included, was written by Claude (Anthropic) under the direction of Levent Alpöge, who wrote no Lean by hand". The formalization.yaml `automation` entry: "method: autonomous, models: [Claude]". The `review` status for Euler is "author-verified" ("Levent Alpöge... read the challenge module Challenge.lean at the released revision... and confirmed it states the manuscript's blow-up theorem"); for the two Boussinesq projects it is "unreviewed" pending that read.

Boussinesq acknowledgments: "L.A. would like to thank Anthropic for support of our external academic collaboration, because the use of Claude sped our collaboration's understanding of the correct and incorrect ideas in the literature and the implementations of our own ideas decisively."

What the humans did vs the models (my reading of the above): humans chose the program (CM-Z), chose the target ladder (IPM → Boussinesq → Euler → hypodissipative NS), supplied ansätze and architecture ideas (including convex-integration-inspired simplifications), ran the models in iteration, judged which of "several different proofs" to keep, and did the hand editing; models reproduced the CM-Z argument, generated the first proofs, did the bookkeeping of inductive orders and constants, wrote the body text, and wrote all the Lean (statement file included). Lean served as the acceptance test *before* the humans understood the proof (Aug 22 verified; weeks of understanding followed).

### C.4 Presentation quality, in their own words

"I am not happy about the presentation quality in these papers... The various Boussinesq and Euler write-ups in particular are much closer to what models produce under human direction than to a paper written by a person. The Euler writeup, in particular, can only be described as AI slop. I am sorry for this."

"the important thing is instead the significance that a mathematician and an LLM model can now do all this work in a month. The significance of this with respect to the way we train students, assign credit, referee, and decide what is worth one human life's attention cannot be understated. This is a a Deep Blue-Kasparov moment."

### C.5 The dispute, as Buckmaster states it (dates his)

- Thu Sep 3: with "a rumor circulating that Anthropic had resolved a major open problem, and with Levent having received tips that information about our progress had been passed to OpenAI", he emailed "a prominent mathematician at OpenAI" (email quoted in full in the statement), saying they would post "the paper and the formalization together. We intentionally decided against rushing out a Lean certificate alongside an unpolished preprint." Reply same day: "If you are willing to give any details it would be useful to avoid competing here... if there is anything in terms of compute from OpenAI's end we would be happy to provide it."
- Fri Sep 4 and Sun Sep 6 12:45: repeated requests to meet; two calls Sunday afternoon with Sébastien Bubeck joining; Alpöge not on the calls.
- Told "an internal OpenAI model had produced a proof of finite time blowup for the forced Navier-Stokes equations"; statement given by text: "Existence of forced blowup in R3 and T3," with "the forcing function is smooth option c and d in Fefferman"; "about 100 pages. I have not seen it."
- "I was shown a prompt and told the internal research model had simply been given the problem statement. Levent had been told by Sebastien 'very little human input' had been used. This turned out not to be true. Over the course of the call... it emerged that an entire team had been working on the problem, that this was one of a number of things that was tried, that work had started on the unforced problem, that the team first set the model on easier problems, including Euler, that even the prompt that had been shown to me had been written by prompting Codex, and that an insane amount of compute had been used."
- "Eventually it was agreed that [the first prompt] had been sent in the past few days, after information about our work had reached OpenAI."
- On data: "I was told the model did not look up user data. I asked again, about training, and I did not get an answer."
- Two proposals: (1) A–B post Euler, OpenAI posts NS the next day; (2) Buckmaster alone writes a paper presenting the NS result "acknowledging that an internal OpenAI model had resolved it. Sebastien twice asserted that he wanted Levent removed from authorship". Both declined.
- Quoted exchange: "'Why would you ruin your career?' ... 'If you don't want me to be nice, then I don't have to be nice.'"
- Scope of claim: "I have not seen OpenAI's proof. I do not know what their model did, or how. I do not know whether our data was used. I am not accusing anyone of anything. I am stating what I was told, when, and what was proposed to me."

Mastodon follow-ups (Sep 8): quoting OpenAI's "Since August 28 we have been training a new internal model", he writes "Note that they are openly admitting they used training data from a period after we found our result. Is it ethical to use customer's data to try to scoop their customer?"; and "there is a far bigger story here than the one in my statement: the sheer magnitude of what frontier models can now do".

### C.6 The three preprints: abstracts and main theorems

**IPM** (`alpoge-buckmaster-ipm.pdf`, 57 pp; authors Alpöge, Buckmaster, Coiculescu). Abstract: "By adapting the techniques used in the IPM blowup result of Córdoba-Martínez-Zoroa with spatially smooth force, we prove finite-time blow-up for the IPM equation on T^2 with a uniformly spacetime smooth force. In particular, we show there exist a smooth odd initial density, a smooth odd force F ∈ C^∞([0,1]×T^2), and a classical solution ρ on [0,1) whose density gradient and spatial velocity gradient diverge in L^∞ as t↑1. Nevertheless, ρ(t) converges in C^η for every 0 ≤ η < 1." Theorem 2.1 states this with ρ_in odd, zero mean, ρ ∈ C^∞([0,T]×T^2) for every T<1, a limit ρ_* ∈ ∩_{η<1} C^η, and (4) lim_{t↑1} ‖∇ρ‖_{L^∞} = lim_{t↑1} ‖D_x u_T(ρ)‖_{L^∞} = ∞. New vs CM-Z per the paper: "Fourier space truncations that avoid a loss of derivatives and a mixed induction in time and space that ultimately shows that the force is smooth in space–time... our solution is given by an exact series and requires no nonconstructive passage through a nonlinear limit."

**Boussinesq** (`alpoge-buckmaster-boussinesq.pdf`, 76 pp). Abstract: "Following the multiscale program of Córdoba and Martínez-Zoroa, we construct finite-time blowup for the inviscid Boussinesq system on R^2 with smooth forcing in both equations. The forces belong to C^∞(R^2×[0,T_*]) and are supported in one fixed spatial ball. The initial temperature is smooth and compactly supported, and the initial velocity is zero. The temperature remains bounded, while its gradient norm tends to infinity and the vorticity norm has infinite limsup as t↑T_*, both in L^∞." Theorem 1.1: for the explicit datum θ_in = −(A_0/λ_0) sin(λ_0 x_2) χ_0(x), u_in = 0 (a smooth Rayleigh–Taylor-unstable stratification), there are odd forces f_θ ∈ C^∞_c(R^2×R), f_u ∈ C^∞_c(R^2×R; R^2) and T_* with unique smooth solutions before T_* and (1.5) sup‖θ‖_∞ < ∞, lim‖∇θ‖_∞ = ∞, limsup‖ω‖_∞ = ∞. The mechanism (§1.2) is the exact affine wave: on a background u_old = D(t)x, θ_old = G(t)·x add ϑ = Θ sin s, ϖ = Ω cos s with s = λζ(t)·x; the wave does not advect itself, and the modulation ODEs are ζ̇ = −D^Tζ, Θ̇ = −(Jζ·G)/(λ|ζ|²) Ω, Ω̇ = λζ_1 Θ, with growth rate ±√(A sin φ); a "common rotation" then returns Ω to zero and holds ζ_1 = 0 so the next layer can grow. What is new vs Córdoba–Laín-Sanclemente–Martínez-Zoroa (§1.3): "both forces have one fixed support ball and all mixed derivatives on the closed slab, and the temperature-gradient norm has a full limit of infinity."

**Euler** (`alpoge-buckmaster-euler.pdf`, 112 pp). Abstract: "We construct a finite-time singularity for the incompressible Euler equations on R^3 with a force smooth in space and time up to and including the blowup time. The initial velocity and force are axisymmetric and supported in one fixed solid torus about a circle of arbitrarily prescribed radius and height. The initial velocity is smooth, with nonzero swirl and zero meridional component. Circulation (angular momentum) and meridional velocity remain bounded, whereas the L^∞ norms of the circulation gradient and full vorticity tend to infinity. The time integral of the vorticity L^∞ norm also diverges. On every closed time interval before blowup, the solution is smooth and unique in a three-dimensional finite-energy, locally space-time Lipschitz class with bounded spatial gradients; competitors need not be axisymmetric." Theorem 1.1: for every r_0 > 0, z_0 there exist T_*, R < r_0/2, axisymmetric u_0 ∈ C^∞_c(T_R) with nonzero swirl and zero meridional velocity, and f ∈ C^∞(R^3×[0,T_*]) supported in the torus T_R, with (1.3) lim ‖∇Γ‖_∞ = lim ‖ω‖_∞ = ∞ and (1.4) ∫_0^{T_*}‖ω‖_∞ dt = ∞. Mechanism (§1.2): "The circulation transports the swirl. Its square generates azimuthal vorticity through the fixed axial derivative, and the resulting meridional velocity can amplify the circulation gradient" — the Boussinesq mechanism with Γ² playing the role of temperature, but "For Euler the symbol and the buoyancy coefficient vary across the support." The paper contains no AI statement and no acknowledgments (the one Buckmaster calls "AI slop").

---

## D. The Lean repository `tristanbuckmaster/fluid_lean`

- Created 2026-09-08 04:03 UTC; one commit ("Add affinecore, boussinesq-blowup, and euler-blowup Lean projects. Imported from lean1.zip, lean2.zi…"); 218 stars, 16 forks at read time; repository size 18,840 KB per API.
- Three sub-projects, no top-level README: `affinecore/` (1,181 `.lean` files; a second Boussinesq theorem for explicit data A_0 ≥ 1, declaration `forced_boussinesq_affine_core_blowup`), `boussinesq-blowup/` (1,453 files; `boussinesq_smooth_force_blowup`, for every κ > 0), `euler-blowup/` (1,114 files; `euler_smooth_force_blowup`). Total 3,748 Lean files, **124.4 MB of Lean source**. Largest files are machine-generated: `euler-blowup/EulerBlowup/Ring/S4r/TimeRates.lean` 7.3 MB, `.../S7r/LayerRows.lean` 4.9 MB, `.../S6r/TheoremH.lean` 3.8 MB.
- Toolchain: `leanprover/lean4:v4.32.2` ("4.32.0 plus two kernel soundness fixes"); Mathlib pinned at commit `81a5d257…` (tag v4.32.0). "Do not run `lake update`." Build: "about 1,500 modules... plan for a machine with on the order of 150 GB of memory and a couple of hours at three dozen parallel jobs rather than a laptop" (Boussinesq); affinecore's 1,113 modules "compiled in about nine minutes on a 32-core machine once Mathlib and the vendored library had been built, and the stock toolchain `leanchecker` replayed all modules in the main theorem's closure in about thirty-five minutes".
- Axioms/sorries (each README): "no file other than the trusted statement file `Challenge.lean` contains a `sorry`... the proof rests on no axiom beyond Lean's standard three (`propext`, `Classical.choice`, `Quot.sound`). `Challenge.lean` is the only file a reader must trust"; checked with `leanprover/comparator` (`comparator.json`), which "type-checks the statement file independently, checks that the solution inhabits exactly that statement, restricts axioms to the standard three, and replays the proof." `formalization.yaml`: `sorry_count: 0`, `axioms: [propext, Classical.choice, Quot.sound]`.
- Numerics: "some 1,200 machine-generated interval-arithmetic certificate modules, each an inequality between explicit rationals decided by the kernel; the fixed-point arithmetic they use is itself proved sound in Lean" and "(decide; native_decide is not used)". Affinecore instead keeps "every constant of the construction... a letter with a stated admissible range; the order hypotheses between the letters are shown consistent in Lean by exact rational arithmetic".
- Fidelity notes are explicit: "Neither sup-norm appears literally in the Lean statement: unboundedness is rendered as a minorant g(t) → +∞ attained at some point x at each instant... No rate of blow-up is certified."
- Licensing: Apache 2.0, NOTICE "Copyright 2026 Anthropic, PBC". Authorship in `formalization.yaml` for euler-blowup lists `authors: ["Claude"]`, responsible maintainer Levent Alpöge.

---

## E. News and OpenAI's own account (dispute facts only)

OpenAI page (read through a text proxy), verbatim where it matters:
- Result: "an initially smooth fluid at rest can develop a singularity in a finite time. The fluid has a smooth force applied to it, and its energy remains finite... This resolves the Navier–Stokes Millennium Prize problem by establishing statement 'C' (and also 'D')".
- Model and timeline: "Since August 28 we have been training a new internal model... On Tuesday, September 1, we heard rumors that two Millennium Prize problems had been resolved. Inspired by these rumors and by the step change in performance of our internal model, we launched an effort to evaluate it on all open Millennium Prize problems".
- System: "a system of coordinating agents powered by our internal model. The agents had access to tools such as the ability to read from a cached version of the internet and the ability to run code. Agents were subdivided into groups with the ability to communicate within the group... the group that produced the Navier–Stokes resolution involved on the order of 10,000 concurrent agents." "For each problem, we prompted different groups of agents with different variants of the problem statement, covering all variants of the problem. For the Navier–Stokes problem, we suggested versions 'A' and 'B'... and versions 'C' and 'D'... to separate groups of agents."
- Euler: "we asked our multiagent system to try a set of 'easier' problems. One of these problems was a similar blowup question for the limit of the Navier–Stokes problem with the viscosity term removed... our agents surprised us by resolving this question. The specific variant... was the unforced version... Nearly 100 agents worked together for approximately 50 hours to produce our Euler regularity disproof."
- Then: "we shifted agents away from the other Millennium Problems and prompted these agents with the Euler resolution. When a further trained version of our internal model became available over the course of the effort, we updated our agents to that model. We encouraged different groups of agents to explore a diversity of approaches. After some time, we cross-pollinated the agent groups by using Codex to consolidate the most useful insights from each agent group... The group that found the solution to Navier–Stokes was guided in such a way."
- Numbers: resolution "on Saturday, September 5, about 88 hours after the first agents were launched. Lean formalization and verification took an additional 17 hours via GPT-6 Astra... the agents sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens."
- Credit: "Our effort began on September 1st after hearing a rumor which we later realized was related to Levent Alpöge, an Anthropic employee, and Tristan Buckmaster... After the completion of our full project and Lean verification (on September 6th), believing from the rumor they also had a solution of Navier–Stokes, we reached out to them to offer a concurrent release of our result and to recognize their priority in a joint announcement. At that point we found out that they had a resolution of the forced Euler problem... We recognize the priority of their work on forced Euler". "We (the researchers and the agents) did not see any of their work through any means until they released it publicly — in particular, no specific user data was accessed in order to solve this problem. While unlikely, we cannot rule out that de-identified data derived from their usage of our products helped improve our models. However, our proofs differ significantly and even the precise results proved are different in the Euler case (forced vs unforced)." "We do not intend to claim the Millennium Prize for this result."

Quanta (2026-09-08, "AI Has Solved One of Math's $1 Million Millennium Prize Problems"): Buckmaster announced "just before midnight September 7"; OpenAI "12 hours later"; Bubeck put the compute at "several million dollars"; Fefferman: "I was thrilled that the problem was solved" and called Córdoba and Martínez-Zoroa "the heroes of the story"; Martínez-Zoroa: "I'm very happy for Tristan. It would have been nice to do this ourselves, but I'm very happy for him"; Córdoba: "I don't use AI: I have Luis." Quanta: "OpenAI cedes 3D Euler priority to Buckmaster/Alpöge" and "the details of the interaction between Buckmaster, Alpöge, and OpenAI remain murky."

TechCrunch (2026-09-08): computes 300 billion output tokens as "$22.5 million at current rates"; reports OpenAI's denial and the "cannot rule out that de-identified data" line; "Anthropic did not officially support the research."

Scientific American (2026-09-08): Bubeck at a press briefing said the proof "was developed over the weekend", that the model "independently solved the Euler problem by totally different means", "We did not use their prompt or proofs to prompt our models", and that the NS solution "did follow a similar method" to A–B's. SciAm: "It will likely take time to hash out the differences between the two proofs".

Axios: blocked (Cloudflare); not read.

---

## §Comparison

| | OpenAI unforced Euler | Alpöge–Buckmaster forced Euler | OpenAI forced Navier–Stokes |
|---|---|---|---|
| Statement | ∃ u_0 ∈ C^∞_{c,σ}(R^3), no force, no symmetry, finite lifespan; limsup‖∇u‖_∞ = ∞ and ∫‖curl u‖_∞ dt = ∞ | ∀ r_0, z_0: axisymmetric-with-swirl u_0 supported in a solid torus, smooth force f ∈ C^∞(R^3×[0,T_*]) supported in the same torus; ‖∇Γ‖_∞, ‖ω‖_∞ → ∞, ∫‖ω‖_∞ = ∞; uniqueness in a Lipschitz class | Clay statements C and D (smooth forcing, R^3 and T^3, from rest, finite energy) — per OpenAI's page and per what Buckmaster was told; the paper itself is covered by a sibling reader |
| Length | 57 pp | 112 pp | "about 100 pages" (Buckmaster, as told) |
| Formal verification | none stated in the paper | Lean, 1,114 files, standard axioms only, comparator-checked, statement read by Alpöge | Lean "17 hours via GPT-6 Astra" (OpenAI page); not independently examined here |
| Mechanism | CM-Z parent–child layer cascade; WKB packet on a rank-one shear at the fixed origin; exact two-scale correction (Gevrey-2) so no force is needed; pressure Hessian bound maintained globally | CM-Z cascade in axisymmetric volume coordinates; Boussinesq-type Γ²/azimuthal-vorticity instability; corrections up to finite order with the residual absorbed into a smooth force whose mixed derivatives are summable | per Bubeck (SciAm) "a similar method" to A–B; per OpenAI, seeded by their Euler resolution |
| Who is cited | CM-Z [9,10,11,12,13], Elgindi school, Chen–Hou, Chen/Shkoller 2026, Cheverry, Lifschitz–Hameiri, Friedlander–Vishik; **not** A–B | CM-Z and coauthors [5–9], A–B Boussinesq [1], Elgindi school, Chen–Hou, Luo–Hou; **not** OpenAI | (not read here) |
| Who credits whom | paper: CM-Z for the layer idea; page: "priority of their work on forced Euler" to A–B | statement and papers: "primary intellectual credit... belongs to" CM-Z; Fields Medal remark for Martínez-Zoroa | OpenAI's page credits nobody mathematically beyond the concurrent-work paragraph |
| Provenance | ~100 agents, ~50 h, Sep 1–5 | two people + Claude/Codex, ~1 year; Aug 15 result, Aug 22 Lean | ~10,000 agents, 88 h + 17 h Lean, ~130B output tokens |

I infer: the unforced Euler result and the A–B forced Euler result are logically incomparable (unforced but non-symmetric and unverified, vs forced but axisymmetric-with-swirl and Lean-verified); the unforced one is the stronger *statement*, the forced one the stronger *certificate*. Both descend from the same CM-Z mechanism; the technical fork is whether the residual is cancelled exactly (OpenAI) or paid for by a smooth force (A–B, and by OpenAI's own account, its NS).

## §Two workflows

**Swarm (OpenAI).** 10,000 concurrent agents in communicating groups, each group prompted with a different variant of the statement (A/B proof-side and C/D disproof-side simultaneously), tools = cached internet + code execution, an easier-problem ladder run in parallel (Euler fell first and its resolution was fed back as a prompt), periodic Codex-driven "cross-pollination" that consolidated each group's intermediate results, model swapped mid-run for a further-trained checkpoint, Lean at the end via a separate model. Cost: 300B output tokens across all problems (TechCrunch: ~$22.5M at list; Bubeck: "several million dollars"). What it bought: 88 hours wall-clock from first prompt to a claimed C/D disproof, plus an unforced Euler disproof as a by-product; no human understanding of the proof at release (Buckmaster: "they do not seem to have any mathematicians capable of understanding what they put out" — his words on Mastodon, not a verified fact) and, by the Tao-comment consensus, a writeup problem. Two things the source does not say: how the agents' correctness was checked before Lean, and whether the Euler by-product was formalized at all.

**Pair + models (Alpöge–Buckmaster).** A year of slow work "through the literature," upgrading CM-Z's IPM result first; humans supply ansätze and architecture ("iteration with the model on various ansätze"; convex-integration-inspired simplifications), models supply reproduction of the prior art, bookkeeping of "inductive orders and constants," body text, and all Lean; Lean verification (Aug 22) preceded understanding by weeks; a separate model (Astra) used "only... for writeups and auditing." What it bought: three Lean-certified theorems with a human-readable Boussinesq introduction that Tao could summarize after a half-hour call; explicit credit lineage; a ladder that already points at the next rung (hypodissipative NS, held back until Lean finishes). Cost: personal research funds; presentation quality sacrificed when the timeline collapsed. What it did not buy: speed — and, in the end, priority on NS.

I infer the decisive shared ingredients: (1) a pre-existing human program with a concrete mechanism (CM-Z) that both efforts explicitly started from; (2) a ladder of model problems with the same mechanism; (3) Lean as the arbiter of truth decoupled from comprehension; (4) a model-driven consolidation step (Codex "cross-pollination" in one, "we have generally input all of our intermediate writeups to Codex for simplification, ideation, and iteration" in the other).

## §Lessons for the RH program (each tied to a sourced fact)

1. **Start from a live human program with a named mechanism, not from the statement.** The source says: Buckmaster, "The program this fits into was not started by us nor was it proposed by a Large Language Model"; OpenAI's paper credits CM-Z's layer idea [10, §1.2]; Buckmaster on the swarm, "It is not the direction one arrives at in a few days by giving a model the problem statement." I infer: for RH the program must first choose a mechanism-bearing line (whatever the sponsor's chosen approach is) with a literature the models can reproduce, and measure progress along it; "prove RH" as a prompt is the failure mode the sources describe.

2. **Build a ladder of genuinely easier problems sharing the mechanism, and feed each rung forward.** The source says: A–B went IPM → Boussinesq → Euler → hypodissipative NS over a year; OpenAI "asked our multiagent system to try a set of 'easier' problems... our agents surprised us by resolving [Euler]... we... prompted these agents with the Euler resolution." I infer: the RH program should define its own rungs (analogues over function fields, finite-range or conditional statements, model operators, weaker zero-free or density statements — whichever the chosen mechanism admits) and treat each rung's *proof text* as input to the next.

3. **Lean is the acceptance test, and it can run ahead of understanding.** The source says: "the first LLM generated proof Levent sent me was the most horrendous I have ever read; we verified it on Lean on August 22nd. Since this point, we have been working around the clock to understand this proof." The repo shows how: a Mathlib-only `Challenge.lean` that is "the only file a reader must trust," comparator-checked, standard three axioms, `decide` not `native_decide`, a `formalization.yaml` with an honest `fidelity.divergences` block. I infer: the RH program should write and human-review the statement file first, keep a fidelity ledger of every divergence between the informal and formal statements (rates, quantifier order, norm renderings), and accept nothing into the results register without the certificate.

4. **Reserve human effort for ansätze, architecture and judgment; give the models the bookkeeping.** The source says: "delegating delicate bookkeeping of inductive orders and constants to the models while implementing our ideas"; "Levent Alpöge, who wrote no Lean by hand"; "Claude originally generated an overly complicated version... In simplifying the proof, we incorporated many of our own ideas." I infer: the sponsor's time is best spent choosing which of several model-generated proof architectures to pursue and simplifying, not on constants or Lean syntax.

5. **Run the disproof direction and the statement variants at the same time.** The source says: OpenAI prompted "versions 'A' and 'B'... and versions 'C' and 'D'... to separate groups of agents" and "covering all variants of the problem." I infer: an RH program should carry parallel lanes for the conjecture, its negation (a zero off the line), and its strengthenings/weakenings (GRH, Lindelöf, zero-density, de Bruijn–Newman-type statements), because the fluids outcome shows the *resolved* variant can be the one nobody targeted first.

6. **Consolidate across workers with a model, on a schedule.** The source says: "we cross-pollinated the agent groups by using Codex to consolidate the most useful insights from each agent group. These follow-up prompts drew on the agents' own intermediate results"; A–B "generally input all of our intermediate writeups to Codex for simplification, ideation, and iteration." I infer: the RH program's reader/writer agents should periodically hand their intermediate writeups to a consolidation pass whose output becomes the next brief — the one step both workflows share.

7. **Expect the first proof to be unreadable, and budget for the rewrite as a separate, long phase.** The source says: "the worst writeup we had ever seen in the history of mathematics"; Tao: "the actual solving of these problems is only a proxy goal for the primary goal of developing mathematical understanding"; a Tao commenter proposes rejecting papers for "the lack of communication effort despite a formal Lean certificate." I infer: plan the exposition phase (introduction with mechanism, ODE-level toy calculation, proof-order figure — the pieces Tao could actually digest) as a deliverable with its own time, since certificate-first releases were the thing everyone criticized this week.

8. **Protect provenance: commit early with hashes, keep drafts out of third-party model contexts, and be explicit about what was and was not seen.** The source says: the IPM paper published SHA-256 placeholders for the Lean artifacts as a commitment; OpenAI "cannot rule out that de-identified data derived from their usage of our products helped improve our models"; Buckmaster: "into which we had been putting all our drafts for the whole of this project." I infer: the RH program should publish hashes of its certificates and manuscripts at milestones, keep a dated log (this repo's LOG/STATUS discipline already does this), and decide deliberately which providers see which drafts.

9. **Announce only what is certified; hold the rest, and say so.** The source says: A–B withheld hypodissipative NS because "the Lean verification has not yet finished"; OpenAI's Euler paper carries no verification statement while its page claims Lean for NS only. I infer: the RH register should distinguish "Lean-certified," "human-checked," and "model-claimed," and never let the third category be reported upward as more than a lead.

10. **Be honest about the structural mismatch.** The source says: every result this week is an *existence* construction (a datum and a force that blow up); Tao's abstraction N(u)=f with an exploitable linearized instability is a construction template. I infer: RH is a universal statement, so the fluids *mechanism* does not transfer; what transfers is the workflow (program → ladder → certificate → rewrite → consolidation), and the only construction-shaped lane in an RH program is the counterexample lane, which no source suggests is promising.

## §Open questions in fluids after this week (per Tao and the papers)

- **Unforced Navier–Stokes** (Clay statements A/B, i.e. global regularity without force on R^3 and T^3): not touched by anyone. OpenAI resolved C/D only; Tao: "it should even be possible to do without the forcing term" — for the model equations, an expectation, not a result.
- **Independent scrutiny of OpenAI's NS proof**: unrefereed; ~100 pages; Lean per OpenAI but nobody outside has reported replaying it; SciAm: "It will likely take time to hash out the differences between the two proofs."
- **Unforced Euler**: OpenAI's 57-page claim is unformalized on the evidence of the paper; A–B's Lean-certified Euler is forced and axisymmetric-with-swirl. Buckmaster says hypodissipative NS "is suggestive of a path to unforced Euler" (his paper withheld until Lean finishes). Whether a Lean-certified unforced Euler blowup exists is open in public.
- **Periodic (T^3) unforced Euler and periodic versions generally**: A–B's IPM is on T^2; their Boussinesq and Euler are on R^2/R^3; OpenAI's Euler is on R^3. No periodic unforced result.
- **Self-similar route** (GDA/PINN, Tao's EDIT): the residual is ~0.004 in L^∞ but Cao-Labora notes the derivative residuals, not reported, are what decide whether "an actual smooth self-similar solution [exists] near by"; rigorous stability "remains a major challenging task."
- **Rates and profiles**: the A–B formal statements "certif[y] blow-up and no particular rate" (fidelity notes); the cascade constructions give no self-similar profile.
- **Boussinesq without force on R^2 with smooth data** (Chen–Hou is with boundary): open.
- **Hypodissipative NS with smooth force**: claimed by A–B, unreleased; CM-Z–Zheng have it with rough force (ARMA 2026).
- **Does NS "follow from the same method as Euler, but pushing harder"?** Asked in Tao's comments; Bubeck (SciAm) says OpenAI's NS "did follow a similar method"; unanswered mathematically in public.
- **Non-mathematical**: the data-use and priority questions (Buckmaster's account vs OpenAI's; "de-identified data") are unresolved by any source read here.

---

## Appendix 1. Section map of the OpenAI Euler paper (for a later reader)

| Section | Pages | Content | Load-bearing statement |
|---|---|---|---|
| 1 Introduction | 1–3 | Theorem 1.1; historical context (BKM, Elgindi school, CM-Z, Chen–Hou, ill-posedness, weak solutions, Craik–Criminale, WKB) | Theorem 1.1 |
| 2 Amplification mechanism and proof order | 3–9 | particle coordinates (2.2)–(2.3); leading WKB system (2.4); packet (2.5); phase average (2.6); leading Hessian increment (2.7); norms (2.8); Gevrey-2 convention; Figure 1; notation index | (2.1) growth + summability |
| 3 A localized oscillation over a smooth Euler flow | 9–34 | product/triangular factorial rules (3.2)–(3.3); profile f_δ (3.4); hypotheses §3.2 incl. H ≤ K_+ I (3.11); mean inverse (3.19)/(3.25); transverse inverse (3.27)/(3.29); expansion (3.33)–(3.34); residual (3.45); Lemma 3.3 exact correction; Claims 1–3 | Proposition 3.1 |
| 4 Amplification and transfer of the wave geometry | 34–44 | parent shear h q p^T (4.3); frozen coefficients, rescaled time (4.4); activation data (4.8); rotating frame (4.20); ideal growth §4.4; stability §4.5; next frame §4.6 | Proposition 4.1 |
| 5 Choosing the scales and iterating | 44–54 | base flow U_B and local existence §5.1; scales (5.3), order of choice §5.2; time intervals (5.7)–(5.8); maintained estimates (5.4)–(5.5); verification §5.5; seed §5.6; inductive step §5.7 | induction closes |
| 6 Limiting datum and breakdown | 54–56 | H^m Cauchy (6.1)–(6.3); T_∞ (6.4); stability (6.5)–(6.6); continuation criteria; log-Lipschitz (6.7) | Theorem 1.1 proved |
| References | 56–57 | 29 items | — |

## Appendix 2. Reference overlap among the three Euler documents

| Reference | OpenAI unforced Euler | A–B forced Euler | A–B Boussinesq |
|---|---|---|---|
| Beale–Kato–Majda 1984 | [1] | [2] | — |
| Córdoba–Martínez-Zoroa, forced Euler C^{1,1/2−ε} force (arXiv:2309.08495) | [10] | [6] | — |
| Córdoba–Martínez-Zoroa, IPM smooth source (arXiv:2410.22920) | [11] | [7] | [6] |
| Córdoba–Martínez-Zoroa–Zheng, Euler C^∞(R^3∖{0}) ∩ C^{1,α} (Ann. PDE 2025) | [13] | [9] | — |
| Córdoba–Laín-Sanclemente–Martínez-Zoroa, Boussinesq pendula (Adv. Math. 2025) | — | [5] | [5] |
| Córdoba–Martínez-Zoroa–Zheng, hypodissipative NS (ARMA 2026) | — | [8] | — |
| Elgindi 2021 (Ann. Math.) | [15] | [10] | — |
| Elgindi–Ghoul–Masmoudi 2021 | [16] | [11] | — |
| Elgindi–Pasqualotto (arXiv:2310.19780) | [19] | [12] | [8] |
| Chen–Hou I/II | [6],[7] | [3],[4] | [4] |
| Chen 2026 (arXiv:2605.15130), Shkoller 2026 (arXiv:2603.10945) | [5],[29] | — | — |
| Lifschitz–Hameiri 1991; Friedlander–Vishik 1991; Cheverry 2006 | [28],[21],[8] | — | — |
| Craik–Criminale 1986; Fabijonas–Holm 2004; Le Dizès–Leblanc 2006 | [14],[20],[25] | — | — |
| Bourgain–Li 2015 | [2] | — | (cited in IPM paper as [6]) |
| Alpöge–Buckmaster Boussinesq | — | [1] | — |
| Alpöge–Buckmaster–Coiculescu IPM | — | — | [1] |
| OpenAI (any) | — | — | — |

I infer from the overlap: the two Euler papers share the CM-Z core (three papers) and the Elgindi/Chen–Hou landmarks, and differ exactly where their techniques differ — OpenAI's exact-correction route draws on the WKB/geometric-optics and Craik–Criminale literature, which A–B do not cite; A–B's forced route draws on the Boussinesq-pendula and hypodissipative-NS papers, which OpenAI does not cite. Neither cites the other.

## Appendix 3. Timeline (all sources; times as printed by the sources)

| When | Event | Source |
|---|---|---|
| 2023–2025 | CM-Z forced Euler (rough force), IPM smooth-source, Boussinesq pendula, hypodissipative NS | reference lists |
| ~Sep 2025 → Aug 2026 | A–B work through CM-Z with Claude/Codex; IPM smooth forcing obtained | statement |
| Aug 15, 2026 | A–B obtain Boussinesq and Euler blowup with smooth forcing (Claude) | statement; Boussinesq §2 |
| Aug 22, 2026 | First Lean verification (Boussinesq) | statement; Boussinesq §2 |
| Aug 28, 2026 | OpenAI begins training new internal model | OpenAI page |
| Aug 31, 2026 | (context) Stadlmann prime-gap bound 246 → 240 | Tao comment "J" |
| Sep 1, 2026 | OpenAI hears rumor, launches Millennium-problem evaluation; ~100 agents resolve unforced Euler in ~50 h | OpenAI page |
| Sep 3, 2026 | Buckmaster emails OpenAI mathematician | statement |
| Sep 5, 2026 | OpenAI agents arrive at NS resolution, ~88 h in | OpenAI page |
| Sep 6, 2026 | OpenAI Lean verification complete (+17 h); two calls with Bubeck; two proposals declined | OpenAI page; statement |
| Sep 7, 2026 | GDA PINN Euler preprint (anima-ai.org); Tao's post; A–B euler.pdf built 04:34 IST Sep 8 (= 23:04 UTC Sep 7); Buckmaster announces "just before midnight" | Tao; PDF metadata; Quanta |
| Sep 8, 2026 | fluid_lean pushed 04:07 UTC; statement.pdf, ipm.pdf, boussinesq.pdf online; OpenAI announcement ~12 h after A–B; OpenAI Euler PDF built 19:07 UTC; Quanta/TechCrunch/SciAm pieces; Buckmaster Mastodon follow-ups | GitHub API; Mastodon RSS; PDF metadata; Quanta |
| Sep 9, 2026 | This report | — |

Status: COMPLETE
