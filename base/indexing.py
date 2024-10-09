import os
from pre_processing.pre_processing import pre_processing_bool, pre_processing_vett
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from tqdm import tqdm
from whoosh.index import open_dir
from pathlib import Path


def create_index_vett(cartella_doc):
    """
    Crea l'indice nella cartella indexDir, e passa all'indice,dopo averli
    pre-processati tutti i documenti nella cartella cartella_doc.

    Args:
        cartella_doc (str): Il nome della cartella in cui ci sono i documenti.

    Returns:
        str: Il nome della cartella di ritorno.
    """
    totale_documenti = conta_file_ricorsivo(cartella_doc)
    
#______________________  CREAZIONE INDICE
    # Definizione dello schema dell'indice
    schema = Schema(doc_id=ID(unique=True, stored=True), content=TEXT)
    #se la directory in cui creare l'indice non esiste la creo
    if not os.path.exists("index_dir_vett"):
        os.mkdir("index_dir_vett")
    # Directory dell'index
    index_dir = "index_dir_vett"
    # Crea un index con schema schema, e nella directory index_dir
    index = create_in(index_dir, schema)
    writer = index.writer()    

    pbar = tqdm(total=totale_documenti, desc="Preprocessing") #barra per il caricamento
#______________________   AGGIUNTA DOCUMENTI
    #estraggo tutti i file nel dataset
    for root, dirs, files in os.walk(cartella_doc):
        for file_name in files:
            #mi costruisco il percorso del documento fondendo il percorso della cartella col nome del file
            percorso = os.path.join(root, file_name)
            #estraggo il contenuto del file nella variabile text
            with open(percorso, 'r',encoding='ISO-8859-1') as file:
                text = file.read()        
            #creo il documento whoosh con doc id pari al nome del documento e contenuto pari al risultato del preprocessing
            whoosh_document = {"doc_id": file_name, "content": pre_processing_vett(text)}
            writer.add_document(**whoosh_document)#aggiungo il documento all'indice 
            pbar.update(1) #aggiornamento della barra
    pbar.close() #chiusura della barra
    # Chiusura del writer
    writer.commit()
    return index

def create_index_bool(cartella_doc):
    """
    Crea l'indice nella cartella indexDir, e passa all'indice,dopo averli
    pre-processati tutti i documenti nella cartella cartella_doc.

    Args:
        cartella_doc (str): Il nome della cartella in cui ci sono i documenti.

    Returns:
        str: Il nome della cartella di ritorno.
    """
    totale_documenti = conta_file_ricorsivo(cartella_doc)
    schema = Schema(doc_id=ID(unique=True, stored=True), content=TEXT)
    if not os.path.exists("index_dir_bool"):
        os.mkdir("index_dir_bool")
    index_dir = "index_dir_bool"
    index = create_in(index_dir, schema)
    writer = index.writer()    
    pbar = tqdm(total=totale_documenti, desc="Preprocessing") #barra per il caricamento
    for root, dirs, files in os.walk(cartella_doc):
        for file_name in files:
            percorso = os.path.join(root, file_name)
            with open(percorso, 'r',encoding='ISO-8859-1') as file:
                text = file.read()        
            whoosh_document = {"doc_id": file_name, "content": pre_processing_bool(text)}
            writer.add_document(**whoosh_document)#aggiungo il documento all'indice 
            pbar.update(1) #aggiornamento della barra
    pbar.close() #chiusura della barra
    writer.commit()
    return index


def load_index(index_dir):
    """
    Carica l'indice.
    
    Args:
        path (str): Percorso completo della directory dell'indice.
    
    Returns:
        index: indice su cui effettuare la ricerca
    """
    #Apertura della cartella in cui c'è l'indice
    index = open_dir(index_dir)
    return index

def conta_file_ricorsivo(directory):
    path_directory = Path(directory) #per poter analizzare la cartella

    # Utilizza pathlib.Path.rglob() per ottenere tutti i file ricorsivamente
    file_list = list(path_directory.rglob('*'))

    # Filtra solo i file
    numero_documenti = sum(1 for file in file_list if file.is_file())

    return numero_documenti

