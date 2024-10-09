import spacy

nlp = spacy.load("it_core_news_sm")
#preprocessing per i documenti, prende in input direttamente il contenuto del documento, restituisce una stringa 
def pre_processing_vett(text):
    """
    Preprocessa il testo passatogli, rendendo il testo minuscolo, per poi eseguire la tokenizazzione,
    la lemmatizzazione, l'eliminazione delle punteggiatura e delle stopwords. Funziona solo per l'italiano.
    Args:
        text (str): Testo da preprocessare.

    Returns:
        str: Testo preprocessato, sotto forma stringa
    """
    #rendo tutto minuscolo
    text = text.lower()
    #divisione di text in un insieme di tokens (=parole)
    doc = nlp(text)
    # Estrazione lemmi, ossia prendo solo il campo lemma di ogni token
    tokens_lemmatizzati = [token.lemma_ for token in doc]
    # Rimozione punteggiatura e stop words
    stop_words = spacy.lang.it.stop_words.STOP_WORDS
    tokens_filtrati = [lemma for lemma in tokens_lemmatizzati if lemma.isalnum() and lemma not in stop_words]
    return " ".join(tokens_filtrati)

def pre_processing_bool(text):
    """
    Preprocessa il testo passatogli, rendendo il testo minuscolo, per poi eseguire la tokenizazzione,
    la lemmatizzazione, l'eliminazione delle punteggiatura e delle stopwords. Elimina i duplicati.
    Funziona solo per l'italiano.
    Args:
        text (str): Testo da preprocessare.

    Returns:
        str: Testo preprocessato 
    """
    text = text.lower()
    doc = nlp(text)
    tokens_lemmatizzati = [token.lemma_ for token in doc]
    stop_words = spacy.lang.it.stop_words.STOP_WORDS
    tokens_filtrati = [lemma for lemma in tokens_lemmatizzati if lemma.isalnum() and lemma not in stop_words]
    tokens_finali= set(tokens_filtrati)
    return " ".join(tokens_finali)

def pre_processing_doc2vec(text):
    """
    Preprocessa il testo passatogli, rendendo il testo minuscolo, per poi eseguire la tokenizazzione,
    la lemmatizzazione, l'eliminazione delle punteggiatura e delle stopwords. Funziona solo per l'italiano.
    Args:
        text (str): Testo da preprocessare.

    Returns:
        list: Lista di tokens 
    """
    text = text.lower()
    doc = nlp(text)
    tokens_lemmatizzati = [token.lemma_ for token in doc]
    stop_words = spacy.lang.it.stop_words.STOP_WORDS
    tokens_filtrati = [lemma for lemma in tokens_lemmatizzati if lemma.isalnum() and lemma not in stop_words]
    return tokens_filtrati
 