# Generative AI and Linked Data
A detailed record of the research performed during my summer 2023 internship with AFRL. Everything here is declassed, so it is ok to host this publicly. A project was developed and presented by the end of the summer, but the general focus of research (very open-ended) was:

1. Getting generative models to spit out valid triples and maybe DL axioms
2. ML workflows, from end-to-end, in an operational military context of training, testing, deploying and replacing in the field
3. GPT alternatives, including ones that can run locally and can be fine-tuned more explicitly
4. Prompting techniques... we already know a lot about this stuff but there are interesting fragments in the literature to consider

This repo reflects that research, organizing it as appropriate. If I have granted you access, my summer research specific to the AFRL can be found [here](https://github.com/PR0CK0/AFRL_Summer_2023) (private).

``` All linked papers saved locally as PDFs in this repo :)```

# Table of Contents
1. [Survey](#survey)
2. [LLMs and LD Generation](#llms-and-ld-generation)
3. [ML Workflows](#ml-workflows)
   1. [ML Workflow Papers](#ml-workflow-papers)
   2. [Ontologies](#ontologies)
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

## Fine-tuning
One thought I had was [fine-tuning](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset) GPT on LD instance data and DL axioms to get a model really good at spitting out triples. This could be possible but it would require the collection of prompt-response pairs that could be generated (by using GPT), to then fine-tune off of. But at the end of the day it would take manual effort, which is why most work in the literature tends to just use GPT with a few examples in a good prompt to get valid RDF and OWL output.

# ML Workflows
By "ML Workflows", I mean all associated nomenclature, e.g.:

* ML Operations (MLOps)
* ML Engineering
* AutoML
* Etc.

The main thing of interest is the generation and maintenance of appropriate provenance for ML models over the lifecycle of operational ML. For example, in the context of, say, image classification for tanks, an ML provider may say they can give an uber model to detect anything, but this is not realistic. If it's foggy out, or rainy, or the targets paint pink unicorns all over their tanks - surprise: suddenly the model doesn't work! So ML models need to be traceable to their training data, tested quickly, deployed for actionable use and easily retirable once certain requirements aren't met, e.g., not being able to detect tanks with painted unicorns on them. So, the importance of properly serializing ML workflows cannot be understated, and this goes hand-in-hand with Linked Data, because graph data is ideal for representing provenance, e.g., consider the PROV project.

## ML Workflow Papers
* [Managing Machine Learning Workflow Components](papers/ml_workflows/1912.05665.pdf)
* [ModelDB: A System for Machine Learning Model Management](papers/ml_workflows/2939502.2939516.pdf)
* [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](papers/ml_workflows/mlops.pdf)

## Ontologies
* PROV
* [Workflow Provenance in the Lifecycle of Scientific Machine Learning](papers/ontologies/souza.pdf) - defines the PROV-ML ontology

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