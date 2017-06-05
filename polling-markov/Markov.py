import markovify
import sys

def main(argv):
    # Get raw text as string.
    with open("db/corpus.txt") as f:
        text = f.read()
    # Build the model.
    text_model = markovify.NewlineText(text, state_size=2)

    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(3):
        print(text_model.make_short_sentence(140))

if __name__ == "__main__":
    main(sys.argv[1:])
