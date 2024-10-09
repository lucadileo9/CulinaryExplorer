from base.searching import  search_bool,  search_vett , search_doc2vec
from base.indexing import create_index_bool, create_index_vett, load_index
import time
from doc2vec.training import training, read_corpus, load_corpus, save_corpus, load_model

cartella_doc = "DATASET_FINALE"

scelta_modello=input("Choose the model, boolean(b), vector(v), doc2vec(d), more infos(i): ")
if scelta_modello== "b":
    scelta_operazione=input("Choose the operation to do: search(s), create index(c):")
    if scelta_operazione == "c":
        index_dir= create_index_bool(cartella_doc) # BOOLEANO
    else:
        nome_dir="index_dir_bool" # BOOLEANO
        index_dir=load_index(nome_dir)
        
    print("To exit the search type esc")    
    user_query=input("Insert text: ")
    while(user_query!='esc'):
        tempo_iniziale = time.time()
        names, results =search_bool(index_dir, user_query)
        tempo_finale = time.time()
        print(f"Time: {round((tempo_finale - tempo_iniziale),3)}")
        print("Search Results:")
        for result in results:
            print(f"{result.rank + 1}° {names[result.rank]}")
        user_query=input("Insert text: ")

elif scelta_modello== "v":
    scelta_operazione=input("Choose the operation to do: search(s), create index(c):")
    if scelta_operazione == "c":
        index_dir= create_index_vett(cartella_doc) #   VETTORIALE
    else:
        nome_dir="index_dir_vett" # VETTORIALE
        index_dir=load_index(nome_dir)
    
    print("To exit the search type esc")    
    user_query=input("Insert text: ")
    while(user_query!='esc'):
        tempo_iniziale = time.time()
        names, results =search_vett(index_dir, user_query)      # VETTORIALE
        tempo_finale = time.time()
        print(f"Time: {round((tempo_finale - tempo_iniziale),3)}")
        print("Search Results:")
        for result in results:
            print(f"{result.rank + 1}° {names[result.rank]}")
        user_query=input("Insert text: ")

elif scelta_modello== "d":
    scelta_operazione=input("Choose the operation to do: search(s), training(t):  ")
    if scelta_operazione == "t":
        print("Training started")
        # caricamento corpus 
        nome_file= 'corpus.pickle' # DOC2VEC
        corpus= load_corpus(nome_file) # DOC2VEC
        # TRAINING
        model= training(corpus)
        print("Training finished")
    else:
        name_model= "modello_doc2vec"
        model = load_model(name_model)  #DOC2VEC
    
    print("To exit the search type esc")        
    user_query=input("Insert text: ")
    while(user_query!='esc'):
        tempo_iniziale = time.time()
        sims =search_doc2vec(model, user_query)     #DOC2VEC
        tempo_finale = time.time()
        print(f"Tempo: {round((tempo_finale - tempo_iniziale),3)}")
        for index, (doc_id, similarity) in enumerate(sims[:10]):
            document_title = doc_id 
            print(f"{index + 1}. {document_title}")
        user_query=input("Insert text: ")
elif scelta_modello== "i":
    print("""
    The boolean model:
    - Uses frequency weighting
    - Based on the presence or absence of words
    - Suitable for short queries
    - Best for queries with "abstract" terms

    The vector model:
    - Uses TF-IDF weighting
    - Based on the frequency of words
    - Suitable for medium queries
    - Best for searches with common words

    The doc2vec model:
    - Uses cosine similarity
    - Based on the similarity between vectors
    - Suitable for long queries
    - More general
    """)
else:
    print("Invalid value")