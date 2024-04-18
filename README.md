# semantic-search
Semantic search engine with a database based on Wikipedia

### Tested methods
- Tokenization: treebank, casual tokenizer, biobert, punkt.
- Vectorization: bag of words, tf-idf.
- Semantization: PCA, LDiA, SVD.
- Distance/similarity metrics: euclidean distance, cosine similarity, chebyshev distance, manhattan distance.

### Tools/libraries
- nltk (tokenization),
- transformers (tokenization),
- sklearn (vectorization, semantization and vector similarity metrics),
- pandas, numpy, matplotlib, pymongo, dearpygui. <br><br>

### GUI
<img src="search_GUI.png" alt="search engine GUI" width="600"/>

### Create environment
- Conda <br>
`conda env create -n semantic-search --file semantic-search.yml`
<br><br>
- Virtual env <br>
  - Unix/macOS: <br>
  `python3 -m venv .venv` <br>
  `source .venv/bin/activate` <br>
  `python3 -m pip install -r requirements.txt`
  - Windows: <br>
  `py -m venv .venv` <br>
  `.venv\bin\Activate.bat` <br>
  `py -m pip install -r requirements.txt`
