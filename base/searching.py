from whoosh.qparser import QueryParser
from whoosh.qparser import QueryParser
from whoosh import scoring
from pre_processing.pre_processing import pre_processing_vett, pre_processing_doc2vec

def search_bool(index, user_query):
    """
    Funzione che data una query e la cartella dell'indice esegue la ricerca e ritorna i documenti rilevanti per la query
    Args:
        index_dir (str): Nome della cartella dell'indice.
        user_query (str): Query dell'utente, in formato BOOLEANO.
    Returns:
        nomi_documenti (list): Una lista di identificatori (doc_id) dei documenti rilevanti per la query.
        risultati (Results): Un oggetto Results che contiene informazioni sui documenti rilevanti 
    """

    with index.searcher(weighting=scoring.Frequency()) as searcher:
        # Utilizzo Whoosh QueryParser per analizzare la query preprocessata
        parser = QueryParser("content", schema=index.schema)
        # Costruzione di un query_parser passandoci la query
        query_parser = parser.parse(user_query)# pancetta AND formaggio ,  come fare la carbonara con la pancetta
        # Ricerca della query, verrà restituito un insieme di documenti
        risultati = searcher.search(query_parser, limit = 10)
        # Estrai i risultati come lista di documenti
        nomi_documenti = [risultato["doc_id"] for risultato in risultati]

    return nomi_documenti, risultati


def search_vett(index, user_query):
    """
    Funzione che data una query e la cartella dell'indice esegue la ricerca e ritorna i documenti rilevanti per la query
    Args:
        index_dir (str): Nome della cartella dell'indice.
        user_query (str): Query dell'utente.
    Returns:
        nomi_documenti (list): Una lista di identificatori (doc_id) dei documenti rilevanti per la query.
        risultati (Results): Un oggetto Results che contiene informazioni sui documenti rilevanti 
    """
    with index.searcher(weighting=scoring.TF_IDF()) as searcher:
        # Utilizzo Whoosh QueryParser per analizzare la query preprocessata
        parser = QueryParser("content", schema=index.schema)
        # Costruzione di un query_parser passandoci la query
        query_parser = parser.parse(pre_processing_vett(user_query))# pancetta AND formaggio ,  come fare la carbonara con la pancetta
        # Ricerca della query, verrà restituito un insieme di documenti
        risultati = searcher.search(query_parser, limit=10)
        # Estrai i risultati come lista di documenti
        nomi_documenti = [risultato["doc_id"] for risultato in risultati]

    return nomi_documenti, risultati

def search_doc2vec(model, user_query):
    """ricerca utilizzando il modello doc2vec

    Args:
        model (Doc2Vec): modello preaddestrato
        user_query (string): query dell'utente

    Returns:
        list: lista di tuple, dove ogni tupla rappresenta un documento simile
        e la sua similarità rispetto al vettore di documenti inferito
    """
    # Creazione del vettore relativo alla query preprocessata dell'utente
    inferred_vector = model.infer_vector(pre_processing_doc2vec(user_query))
    # Ricerca dei documenti più simili
    sims = model.dv.most_similar([inferred_vector], topn=10)
    return sims
