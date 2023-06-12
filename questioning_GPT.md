# Prompting GPT for SPARQL
I have an idea on replacing SPARQL with GPT prompting. SPARQL has a very limited set of terms, unlike programming languages, and mostly results in playing games of pattern matching. This tendency to literally just spend SPARQL debugging time matching patterns between nodes interests me, as GPT-4 is capable as an instructional model. Many papers detail prompt engineering techniques centered around giving GPT examples, instructing it, etc., which is intuitive in natural language with RDF graphs. I think massive LLMs can probably do well with it this, because SPARQL has been around on the Web since 2008, so an LLM like GPT-4 likely has a massive amount of training data on SPARQL. Being a W3C standard, I am sure there are shards of it all over the web, hidden or otherwise. Anyhow, to get a feeling about how strong it is with SPARQL, this readme has my exploratory prompts and GPT-4's answers on how much it knows on SPARQL. As it turns out, it's quite good.

## General Knowledge Prompt
With this prompt, I wanted to know just generally what it could say about SPARQL. Nothing implementation specific. It knows the jist. Fine.

```I would like to test your knowledge of SPARQL for querying RDF data. Can you give me a rundown of what you know?```

### Response
```
SPARQL (SPARQL Protocol and RDF Query Language) is a semantic query language for databases, able to retrieve and manipulate data stored in Resource Description Framework (RDF) format. SPARQL allows users to write queries against what can be thought of as a global database of all RDF data.

Here are some key components and concepts associated with SPARQL:

RDF (Resource Description Framework): RDF is a standard model for data interchange on the Web. RDF has features that facilitate data merging even if the underlying schemas differ, and it specifically supports the evolution of schemas over time without requiring all the data consumers to be changed.

Triple Patterns: A fundamental aspect of SPARQL queries is the triple pattern. These patterns match triples in the RDF data. A triple pattern is like an RDF triple, but each of the subject, predicate, and object can be a variable. For example, if you have RDF data about people and their ages, you might use a triple pattern to find all triples where the predicate is "age".

Basic Query Types: SPARQL supports several query forms, which are:

SELECT: returns a table of results.
CONSTRUCT: returns an RDF graph constructed by substituting variables in a set of triple templates.
ASK: returns a boolean indicating whether a query pattern matches or not.
DESCRIBE: returns an RDF graph that describes the resources found.
Graph Patterns: A graph pattern can be a triple pattern or a combination of patterns. The two most common types are Basic Graph Patterns (a set of triple patterns) and Optional Graph Patterns (used to make some parts of the query optional).

Filtering: SPARQL provides FILTER keyword to restrict the solutions of graph patterns. The FILTER keyword is followed by a constraint that acts as a condition.

Prefixes: Prefixes in SPARQL allow you to abbreviate IRIs in your queries. For example, the prefix "rdf:" is usually bound to "http://www.w3.org/1999/02/22-rdf-syntax-ns#", allowing you to use "rdf:type" instead of the full IRI.

Here's an example of a simple SPARQL query:

sparql
Copy code
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name WHERE {
  ?person a foaf:Person.
  ?person foaf:name ?name.
}
This query selects the names of all people defined according to the "foaf" vocabulary in the RDF data.

Remember that the success and efficiency of SPARQL queries can highly depend on the specific database or data set you are querying against, as well as how well your query is written.
```

## SPARQL Property Path Prompt
With this one, I was trying to get it to use property paths...

```
Say I have an RDF dataset where I want to get who foaf:knows who I foaf:know.

For example:
a -> foaf:knows b
b -> foaf:knows c

Where I am the variable 'a'. What query would you write to get all instances of 'c' for me?
```

### Response
Removed header and footer messages
```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?c WHERE {
  :a foaf:knows ?b.
  ?b foaf:knows ?c.
}
```

### Followup Prompt
This one got it.

```Can you rewrite this to use SPARQL property paths? It should be doable in one line.```

### Response
Removed header and footer messages
```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?c WHERE {
  :a foaf:knows/foaf:knows ?c.
}
```