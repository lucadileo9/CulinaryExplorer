# Recipe Search Engine

This project is a Python-based search engine that indexes and retrieves online cooking recipes from various websites. Developed as part of an **Information Management** course project, it allows users to choose from different indexing models and perform searches accordingly.

The recipes were collected via web scraping from the following sources:
1. [Cookaround](https://www.cookaround.com/)
2. [Giallo Zafferano](https://www.giallozafferano.it/)
3. [Ricette Facili e Veloci](http://www.ricettefacilieveloci.it/)
4. [Ricette Regionali](http://www.ricetteregionali.net/)

N.B.: The recipes are in Italian

## Features

- **Indexing Models**:
  - **Boolean (b)**: Search using boolean logic.
  - **Vector (v)**: Retrieve recipes using vector space model.
  - **Doc2Vec (d)**: Search based on document embeddings.

- **Functionality**:
  - **Indexing**: Users can choose to create or update the index.
  - **Search**: Perform recipe searches based on the chosen model.

## Evaluation and Benchmarks

As part of the project, we conducted benchmarks to evaluate the performance of each search engine model. These benchmarks involved testing the models on known queries and measuring how well the results matched the expected outcomes. The results are documented in the `evaluation` file, which contains detailed metrics such as:

- **Discounted Cumulative Gain (DCG)**: Used to measure the relevance of search results. DCG is calculated by assigning higher relevance scores to items appearing earlier in the result list, while later items have diminishing importance. This provides a fair way to evaluate the ranking quality of each search engine model.
  
- **Other metrics** in the `evaluation` file:
  - **Index Creation Time**
  - **Storage Space Used**
  - **Average Search Time**

Additionally, a **PowerPoint presentation** is included that compares the performance of the different models through graphs and charts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lucadileo9/CulinaryExplorer.git
   cd CulinaryExplorer
   ```

2. Set up a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```
3. Install the requirments:
    ```bash
   pip install -r requirements.txt
   ```
4. Download the Italian language model for spaCy:                                                                                                                          
   ```bash
   python -m spacy download it_core_news_sm
   ```
## Usage
  
3. Run the script:
   ```bash
   python culinaryexp.py
   ```

4. Choose the indexing model for the search:
   - Type `b` for **Boolean**.
   - Type `v` for **Vector**.
   - Type `d` for **Doc2Vec**.

5. Select the next action:
   - Create or update the index.
   - Perform a search query.
   
Creating the index takes a long time, and is typically a process that is only done when the dataset changes. The best thing to do is to do some research

N.B.: The recipes are in Italian

## Credits

This project was developed by **Luca** in collaboration with **Giuseppe Nutricato** as part of a bachelor's degree course project.

## Future Improvements
- **GUI Integration**: Adding a graphical user interface for easier interaction.
- **Dataset Enhancement**: Expanding the dataset with more recipes from additional sources.
- **Advanced Search Options**: Implementing search functionalities by ingredient, preparation method, and cooking time.

## License
This project is licensed under the MIT License.
