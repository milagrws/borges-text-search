# Passage Retrieval in a Borges Short Story

Natural language processing (NLP) with Python.

## Objective

Retrieve passages from Jorge Luis Borges’s “Pierre Menard, autor del Quijote” that are most similar to a search query written in Spanish.

## Method

- Split the text into passages of 100 words.
- Represent the passages using TF-IDF.
- Rank passages using cosine similarity.
- Display up to three results with positive similarity scores.

## How to Run

Requirements: Python and scikit-learn.

Install the dependency:

```bash
python -m pip install scikit-learn
```

Run `recherche_borges.py`, then select a UTF-8 text file containing the story. The full story is not included in this repository.

To change the search query, edit the `rechercher(...)` call in the script.

## Example Searches

### Query: “escribir el Quijote”

The program returned the following passages:
Passage 10; score de similarité: 0.192
Passage 15; score de similarité: 0.134
Passage 13; score de similarité: 0.117

Passage 10 has the highest similarity score for this query. These scores measure similarity based on shared vocabulary; they are not relevance percentages. Reading the passages is still necessary to assess their relevance.

### Query: “elefante”

Output: “Aucun mot de la recherche retrouvé.”  
English translation: “No query words were found.”

This test checks how the program handles a query containing a word absent from the indexed vocabulary. Instead of returning passages with zero similarity scores, the program displays a message indicating that no match was found.

## Limitations

The method relies on shared vocabulary rather than a deep understanding of meaning. It may miss relevant passages that use different words. Splitting the text into fixed-length passages can also break sentences.

## Source

Jorge Luis Borges, “Pierre Menard, autor del Quijote,” in *Ficciones*.
