import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#funzione che data un'etichetta POS nltk restituiscie l'etichette wordnet
def get_wordnet_pos(nltk_pos):
    if nltk_pos.startswith('J'):
        return wordnet.ADJ  # Aggettivi
    elif nltk_pos.startswith('V'):
        return wordnet.VERB  # Verbi
    elif nltk_pos.startswith('R'):
        return wordnet.ADV  # Avverbi
    elif nltk_pos.startswith('N'):
        return wordnet.NOUN  # Sostantivi
    elif nltk_pos.startswith('S'):
        return wordnet.ADJ_SAT  # Aggettivi derivati da aggettivi
    elif nltk_pos.startswith('M'):
        return wordnet.ADV  # Avverbi di modo
    elif nltk_pos.startswith('L'):
        return wordnet.ADJ  # Avverbi derivati da aggettivi
    elif nltk_pos.startswith('A'):
        return wordnet.ADJ  # Aggettivi
    elif nltk_pos.startswith('R'):
        return wordnet.ADV  # Avverbi
    else:
        return wordnet.NOUN  # Sostantivi (default)

#preprocessing per i documenti, prende in input un percorso, ne estrae il testo e lo preprocessa, ritorna un set di token
def pre_processing_document(percorso):
    #estraggo il contenuto del file nella variabile text
    with open(percorso, 'r',encoding='ISO-8859-1') as file:
        text = file.read()
    #print(text)

    #rendo tutto minuscolo
    text = text.lower()

    #divisione di text in un insieme di tokens (=parole)
    tokens = word_tokenize(text)

    # Rimozione della punteggiatura
    tokens = [parola for parola in tokens if parola.isalnum()]

    # Scarica l'elenco delle stop words
    stop_words = set(stopwords.words('english'))
    # Rimuovi le stop words dai token
    tokens_senza_stopwords = [parola for parola in tokens if parola not in stop_words]

    #dà un tag grammaticale ad ogni parola, cioè indica se è un nome, verbo, proposizione ecc..
    tokens_tagged=nltk.pos_tag(tokens_senza_stopwords) 
    #print(tagged)

    # Inizializza il lemmatizzatore WordNet
    lemmatizzatore = WordNetLemmatizer()
    # Lemmatizzazione
    tokens_lemmatizzati = [lemmatizzatore.lemmatize(token, pos=get_wordnet_pos(tag)) for token,tag in tokens_tagged]

    #creo un set, così da non avere duplicati
    tokens_final=set(tokens_lemmatizzati)

# print( "Tokens after elimination of stopwords and noun selection:")
# print( tokens_final)
    return tokens_final

#preprocessing per le query, prende una stringa, la preprocessa e ritorna una query
def pre_processing_query(query):
    query = query.lower()
    tokens = word_tokenize(query)
    # Rimozione della punteggiatura, non si sa mai
    tokens = [parola for parola in tokens if parola.isalnum()]
    stop_words = set(stopwords.words('italian'))
    tokens_senza_stopwords = [parola for parola in tokens if parola not in stop_words]
    tokens_tagged=nltk.pos_tag(tokens_senza_stopwords) 
    lemmatizzatore = WordNetLemmatizer()
    tokens_lemmatizzati = [lemmatizzatore.lemmatize(token, pos=get_wordnet_pos(tag)) for token,tag in tokens_tagged]
    query_preprocessata= " ".join(tokens_lemmatizzati)# ritrasformo la query in una stringa, altrimenti non potrei passarla a parser.parse
    return query_preprocessata

 