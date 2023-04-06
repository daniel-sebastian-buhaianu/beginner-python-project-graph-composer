import string, random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, "r") as f:
        text = f.read()
        text = ' '.join(text.split()) # turn whitespaces into just spaces
        text = text.lower() # make everything lowercase to compare stuff
        # remove all the punctuation to avoid silly scenarios like (Mr. Brightside)
        # "hello! it's me." -> "hello its me"
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    # for each word
    for word in words:
        # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)
        
        # if there was a previous word, then add an edge if it doesn't already exist
        # in the graph, otherwise increment the weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our word to the previous word and iterate
        previous_word = word_vertex 
    
    # generate the probability mappings
    # before returning the graph
    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    comp = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start
    for _ in range(length):
        comp.append(word.value)
        word = g.get_next_word(word)
    
    return comp

def main():
    # step 1: get words from text
    words = get_words_from_text("texts/hp_sorcerer_stone.txt")

    # step 2: make a graph using those words
    g = make_graph(words)

    # step 3: get the next word for x number of words (defined by user)
    comp = compose(g, words, 100)

    # step 4: print
    return ' '.join(comp) # returns string where all the words are separated by a space

if __name__ == "__main__":
    print(main())