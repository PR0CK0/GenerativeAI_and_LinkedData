# Generative AI and Linked Data
A detailed record of my research into the interplay of LD and ML. Mostly interested in maintaining ML provenance, from requirements to phase-out and archival, with a focus on generative AI models. The general focus of the research:

1. Getting generative models to spit out valid triples and maybe DL axioms
2. ML workflows, from end-to-end, in an operational context
3. GPT alternatives, including ones that can run locally and can be fine-tuned more explicitly
4. Prompting techniques... we already know a lot about this stuff but there are interesting fragments in the literature to consider

This repo reflects that research, organizing it as appropriate.

``` All linked papers saved locally as PDFs in this repo :)```

# Table of Contents
1. [Survey](#survey)
2. [LLMs and LD Generation](#llms-and-ld-generation)
3. [ML Workflows](#ml-workflows)
   1. [ML Workflow Papers](#ml-workflow-papers)
   2. [MLOps Systems/Platforms](#mlops-systemsplatforms)
   3. [Ontologies](#ontologies)
4. [GPT Alternatives](#gpt-alternatives)
   1. [A List of Large Models](#a-list-of-large-models)
   2. [Local GPTs](#local-gpts)
   3. [Hosting Services](#hosting-services)
   4. [Evaluating Models](#evaluating-models)
   5. [Jailbroken GPT](#jailbroken-gpt)
5. [Prompting Techniques](#prompting-techniques)
   1. [Prompting Technique Papers](#prompting-technique-papers)

# Survey
On the interplay between Linked Data constructs and LLMs, Tim (@A-J-S97) has included me on a paper of his that surveys this exact topic. He extracted 5 key sub-topics of research:

* Knowledge Graph Generation
* Knowledge Graph Completion
* Knowledge Graph Enrichment
* Ontology Alignment
* Language Model Probing

It is in the publication pipeline and stuck on [Teams](https://teams.microsoft.com/l/team/19%3a7FqwuyXS3frXY6m10sysSjMtKm_l4NRT55nyJw4nkzI1%40thread.tacv2/conversations?groupId=ba2b05c7-541b-4166-93dd-a25d355f20e7&tenantId=6931c963-07b7-4156-ab0e-35d1f79035b8). Any paper cited here is out of the scope of Tim's paper, or else it was missed. 

# LLMs and LD Generation
* [OntoGPT GitHub](https://github.com/monarch-initiative/ontogpt) - a Python package for extracting semantics and creating ontologies from raw text; three approaches, SPIRES, HALO and SPINDOCTOR
   * [Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES)](papers/lms_and_ld/2304.02711.pdf) - the main method underlying OntoGPT
* [KG-BERT](https://github.com/yao8839836/kg-bert)
* [LLMs and SPARQL](https://www.wisecube.ai/blog/sparql-queries-gpts-and-large-language-models-where-are-we-currently/)

## Fine-tuning
One thought I had was [fine-tuning](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset) GPT on LD instance data and DL axioms to get a model really good at spitting out triples. This could be possible but it would require the collection of prompt-response pairs that could be generated (by using GPT), to then fine-tune off of. But at the end of the day it would take manual effort, which is why most work in the literature tends to just use GPT with a few examples in a good prompt to get valid RDF and OWL output.

# ML Workflows
By "ML Workflows", I mean all associated nomenclature, e.g.:

* ML Operations (MLOps)
* ML Engineering
* AutoML
* Etc.

## MLOps Systems/Platforms
What platforms exist for managing ML in an operational context? I mean not just training and storing models, but tracking their creation, phasing them out, archiving them, etc. The entire lifecycle. Everyone simply assumes it's an ad-hoc process or totally proprietary. This is incorrect. Below are several tools for MLOps, including the important aspect of provenance.

* [Kubeflow](https://www.kubeflow.org/) - from Google, for deploying ML workflows on Kubernetes, which is for deploying and scaling containerized apps
* [MLflow](https://mlflow.org/) / [MLflow GitHub](https://github.com/mlflow/mlflow) - end-to-end ML lifecycle management tool
* [TensorFlow Extended](https://www.tensorflow.org/tfx) - mostly for deploying production ML
* [Metaflow](https://metaflow.org/) / [Metaflow GitHub](https://github.com/Netflix/metaflow) - from Netflix, meant for any data science project (not just ML), from exploration to deployment and monitoring
* [Seldon](https://www.seldon.io/) / [Seldon GitHub](https://github.com/SeldonIO/seldon-core) - an enterprise MLOps framework to deal with thousands of ML models
* [Hydra](https://hydra.cc/docs/intro/) / [Hydra GitHub](https://github.com/facebookresearch/hydra) - from Facebook, meant for configuring large apps (may not be entirely applicable)
* [DVC (Data Version Control)](https://dvc.org/) / [DVC GitHub](https://github.com/iterative/dvc) - Git-based version control for ML 
* [Pachyderm](https://www.pachyderm.com/) / [Pachyderm GitHub](https://github.com/pachyderm/pachyderm) - from HP, automates data-driven pipelines for ML
* [Neptune](https://neptune.ai/) / [Neptune GitHub](https://github.com/neptune-ai) - Provenance and metadata store for ML modelst
* [Weights & Biases](https://wandb.ai/site) - data versioning and ML collaboration platform
* [Tecton](https://www.tecton.ai/) - enterprise platform for the ML feature lifecycle
* [Allegro Trains](https://clear.ml/) / [Allegro GitHub](https://github.com/allegroai/clearml) - system is called ClearML; touted as a CI/CD for the ML workflow
* More to come... and I will investigate these deeper...

## ML Workflow Papers
* [Managing Machine Learning Workflow Components](papers/ml_workflows/1912.05665.pdf)
* [ModelDB: A System for Machine Learning Model Management](papers/ml_workflows/2939502.2939516.pdf)
* [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](papers/ml_workflows/mlops.pdf)
* [Automatically Tracking Metadata and Provenance of Machine Learning Experiments](papers/ml_workflows/automatically-tracking-metadata-and-provenance-of-machine-learning-experiments.pdf)
* [Implicit Provenance for Machine Learning Artifacts](papers/ml_workflows/provenance_mlsys20.pdf)
* [Time Travel and Provenance for Machine Learning Pipelines](papers/ml_workflows/opml20_paper_ormenisan.pdf)
* [Machine Learning Pipelines: Provenance, Reproducibility and FAIR Data Principles](papers/ml_workflows/provenance-and-annotation-of-data-and-processes-2021.pdf) - pg. 226

## Ontologies
* PROV
* [Workflow Provenance in the Lifecycle of Scientific Machine Learning](papers/ontologies/souza.pdf) - defines the PROV-ML ontology
   * [Provenance Data in the Machine Learning Lifecycle in Computational Science and Engineering](papers/ml_workflows/souza2019.pdf)

# GPT Alternatives
In a bit of Orwellian doublespeak, "OpenAI" is entirely closed-source. Directly quoting from the 100-page GPT-4 [techical report](papers/lms/2303.08774.pdf):

```"Given both the competitive landscape and the safety implications of large-scale models like GPT-4, this report contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar."```

So, this section pertains to any "alternatives" to GPT, including ways of getting around its limitations. This is for the reason that a lot of military data is classified and cannot even be discussed on online platforms like ChatGPT.

## A List of Large Models
There are tons of large transformer models, e.g., BERT. All of them are potential alternatives to GPT, but (disclaimer!) they are all inferior in almost every circumstance. OpenAI has some secret sauce that simply places them leagues above any other models.
* [Awesome Huge Models](https://github.com/zhengzangw/awesome-huge-models) - The best resource on all of them, including GPTs, LLaMa, PaLM, BLOOM, etc.); I contributed some to it and it is a one-stop shop

## Local GPTs
* [A list of open GPT alternatives](https://github.com/nichtdax/awesome-totally-open-chatgpt)
* [PrivateGPT](https://github.com/imartinez/privateGPT)
* [GPT4All](https://github.com/nomic-ai/gpt4all)

## Hosting Services
* [ColossalAI](https://github.com/hpcaitech/ColossalAI)

## Evaluating Models
* [Holistic Evaluation of Language Models](papers/lms/2211.09110.pdf)
  * [Stanford's CRFM HELM project site](https://crfm.stanford.edu/helm/v0.2.2/)

## Jailbroken GPT
It is possible to prompt GPT so heavily with instructional input, that it can be "persuaded" to evade some of OpenAI's restrictions (e.g., ethical ones):

* [ChatGPT DAN](https://gist.github.com/coolaj86/6f4f7b30129b0251f61fa7baaa881516)
* [ChatGPT Jailbreaks](https://github.com/0xk1h0/ChatGPT_DAN)

# Prompting Techniques
This is the definitive guide on prompt engineering, including links to papers and outside resources, as a GitHub repo:
* [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
   * [Prompting papers](https://www.promptingguide.ai/papers)

## Prompting Technique Papers
* [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](papers/prompting/2201.11903.pdf)
