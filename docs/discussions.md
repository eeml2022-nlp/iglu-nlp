# Initial tasks:

From: https://www.aicrowd.com/challenges/neurips-2022-iglu-challenge/problems/neurips-2022-iglu-challenge-nlp-task

1. Binary classification baseline (any simple finetuning)
2. Question scoring using semantic search baseline - https://www.sbert.net/examples/applications/semantic-search/README.html
3. Question scoring via finetuning - e.g. polyencoder: https://github.com/facebookresearch/ParlAI/tree/main/projects/polyencoder/

We decided to split into teams based on that...

# Conceptual questions

1. What shall we try for our baseline? It should be something simple and trained fast.
2. Link to a notebook? Repo? Dunno how cloud notebooks work when more than a single person is working on it, never done that. Does it fork/merge properly?
3. I suggest we agree on weekly meets, 30 min long, to recap what's done and share findings, ask questions. I suggest Saturday morning, i.e. 10:00.
4. I personally like to manage short term projects in Discord better. I.e. have separate  channels for papers and research, coding questions, training, meeting place, calendar etc.
5. I'd love myself a rough roadmap, with a simple kanban/speadsheet to manage tasks / notes. Without a doc to track things, it's just a permanent state of confusion...

# How to communicate:

1. Linked some stuff in my first message - easy baseline is to try semantic search even without finetuning 
2. We should use repo that i created in our organization 
3. Weekly meets sounds good, though we probably should agree on time, as @Al Ceb is from Columbia meaning large time difference 
4. Large plus - discord/slack is much better for me, but it’s necessary that people will read it, from our slack experience most of us were ignoring it:)
5. Roadmap, kanban board etc can be done on our github page - there are a lot of tools for that there

# Models to try:

1. https://github.com/facebookresearch/DPR
2. https://github.com/stanford-futuredata/ColBERT


# Baselines and metrics: 

1. https://www.aicrowd.com/showcase/baseline-bert-classifier-bm25-ranker
2. https://machinelearning.wtf/terms/mean-reciprocal-rank-mrr/

