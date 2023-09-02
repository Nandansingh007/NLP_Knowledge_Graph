# Onlinekhabar Knowledge Graph and Question Answering

This project aims to build a knowledge graph from text data scraped from Onlinekhabar articles and provide a natural language interface for querying the graph.

## Table of Contents

- [Overview](#overview)
- [Steps](#steps)
- - [Step 1: Data Scraping](#step-1-data-scraping)
- - [Step 2: Text Processing and NLP](#step-2-text-processing-and-nlp)
- - [Step 3: Entity and Relationship Extraction](#step-3-entity-and-relationship-extraction)
- - [Step 4: Building the Knowledge Graph](#step-4-building-the-knowledge-graph)
- - [Step 5: Storing the Graph Database](#step-5-storing-the-graph-database)
- - [Step 6: Question Answering](#step-6-question-answering)
- - [Step 7: Library Used](#step-7-Libraries-Used)
  

## Overview

This project involves building a knowledge graph from text data extracted from selected Onlinekhabar articles. The process includes text scraping, NLP processing, entity and relationship extraction, and graph database creation. The knowledge graph is then used to provide answers to questions based on the stored information.

## Steps

### Step 1: Data Scraping

We use web scraping libraries like Beautiful Soup or Scrapy to extract text data from chosen Onlinekhabar articles. The scraped text data is stored for further processing.

### Step 2: Text Processing and NLP

1. Preprocess the text data to remove noise and unnecessary formatting.
2. Tokenization: Split the text into sentences and words.
3. Part-of-Speech Tagging: Tag words with their grammatical parts of speech.
4. Dependency Parsing: Analyze sentence structure to identify relationships between words.

### Step 3: Entity and Relationship Extraction

1. Named Entity Recognition (NER): Identify entities (people, organizations, locations) in the text.
2. Relation Extraction: Extract relationships between entities.

### Step 4: Building the Knowledge Graph

1. Choose a graph database.
2. Define node and relationship types based on extracted entities and relationships.
3. Populate the graph database with nodes and relationships.

### Step 5: Storing the Graph Database

Use the selected graph database to store nodes, relationships, properties, and labels.

### Step 6: Question Answering

1. Parse the user's question.
2. Identify relevant entities using NER.
3. Query the graph database to retrieve relevant information.
4. Generate a coherent answer based on query results.



## Libraries Used
- NLtk
- Spacy
- beautifulsoup, pandas, matplotlib
- networkx

