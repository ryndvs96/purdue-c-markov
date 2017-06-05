import markovify
import Mine
import os
import sys

INFO = '''INFO:

    You should have setup `auth` and `page_id` values in ./config.json like so:
    
    {
        "auth":"YOUR_API_KEY",
        "page_id":"YOUR_PAGE_ID"
    }
    
    \t-h for help/info
    \t-l to load model in db/model.json
    \t-r to refresh db/corpus and the model\n'''

MODEL_PATH = 'db/model.json'
CORPUS_PATH = 'db/corpus.txt'
STATES=2

def main(argv):
    # try to load model unless override specified
    refresh = False
    if len(argv) > 0:
        if argv[0] == '-r':
            refresh = True 
        elif argv[0] == '-l':
            refresh = False
        else:
            print(INFO)
            return
    
    if refresh:
        print('Refreshing Markov Model')
        model = newmodel()
    else:
        model = loadmodel()
        if model is None:
            print("Unable to load Model, attempting to build new one")
            model = newmodel()

    print('Example Chains:\n')
    # Print five randomly-generated sentences
    for i in range(5):
        print(model.make_sentence() + '\n')

def loadmodel():
    print('Attempting to load the Markov Model from {}'.format(MODEL_PATH))
    if not os.path.isfile(MODEL_PATH):
        print('{} does not exist'.format(MODEL_PATH))
        return None

    model_json = open(MODEL_PATH).read()
    try:
        model = markovify.Text.from_json(model_json)
    except:
        print('Error Loading Model: {}'.format(sys.exc_info()[0]))
        return None
    return model

def newmodel():
    print('Mining text for {}'.format(CORPUS_PATH))
    Mine.main([])
            
    print('Loading {} ...'.format(CORPUS_PATH))
    corpus = open(CORPUS_PATH).read()

    print('Building the new model...')
    model = markovify.NewlineText(corpus, state_size=STATES)

    print('Saving new model in {}'.format(MODEL_PATH))
    if os.path.isfile(MODEL_PATH):
        os.remove(MODEL_PATH)
    f = open(MODEL_PATH, 'w+')
    f.write(model.to_json())

    return model

if __name__ == "__main__":
    main(sys.argv[1:])
