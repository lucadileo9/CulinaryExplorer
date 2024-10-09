import os
import smart_open
import gensim
import pickle
from pre_processing.pre_processing import pre_processing_doc2vec

def read_corpus(directory_path, pbar):
    """funzione che data la directory del dataset restituisce iterativamente
    un singolo file preprocessato

    Args:
        directory_path (string): directory del dataset
        pbar (dqdm): barra di caricamento

    Yields:
        TaggedDocument : restituisce il singolo documento preprocessato e taggato
    """
    for root, dirs, files in os.walk(directory_path):
        for file in files:#per ogni file
            file_path = os.path.join(root, file) # compongo il path
            with smart_open.open(file_path, encoding="iso-8859-1") as f: #lo apro
                content = f.read() # ne leggo il contenuto
                tokens = pre_processing_doc2vec(content) # lo preprocesso
                pbar.update(1)
                yield gensim.models.doc2vec.TaggedDocument(tokens, [file])

def load_corpus(nome_file):
    """carica il corpus dalla memoria

    Args:
        nome_file (string): nome del file contenente il corpus

    Returns:
        string: stringa contenente l'intero corpus
    """
    with open(nome_file, 'rb') as f:
        corpus = pickle.load(f)
    return corpus  
      
def save_corpus(corpus):
    """salvataggio del corpus su disco 

    Args:
        corpus (string): file da salvare
    """
    with open('corpus.pickle', 'wb') as f:
        pickle.dump(corpus, f)

def training (corpus):
    """Allenamento del modello sul corpus e
    salvataggio in memoria

    Args:
        corpus (string): corpus su cui fare addestramento

    Returns:
        Doc2Vec: modello addestrato
    """
    #Creazione del modello 
    model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=2, epochs=100, seed=1)
    # costruzione del vocabolario
    model.build_vocab(corpus)
    # allenamento del corpus
    model.train(corpus, total_examples=model.corpus_count, epochs=model.epochs) #allenamento del corpus
    # salvataggio modello
    model.save("modello_doc2vec")
    return model

def load_model(name_model):
    """caricamento del modello dalla memoria

    Args:
        name_model (string): nome del file presente in memoria che 
        contiene il modello

    Returns:
        Doc2Vec: nodello caricato
    """
    return gensim.models.doc2vec.Doc2Vec.load(name_model)