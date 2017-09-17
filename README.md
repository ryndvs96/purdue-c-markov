
# Purdue Confessions Markov Generator

A simple Markov Generator based on the [Purdue Confession](https://www.facebook.com/PurdueC/) facebook page.

The first part was mining the data via the [Facebook Graph API](https://developers.facebook.com/docs/graph-api/reference/v2.9/page/). You can use the [explorer](https://developers.facebook.com/tools/explorer/) to test out the API if you wish. You can also use it to find the page id and generate a v2.9 API key.

Next step is to create a `config.json` file in the root directory and add in your page id and API key:

```json
{
  "auth":"YOUR_API_KEY_HERE",
  "page_id":"YOUR_PAGE_ID_HERE"
}
```

This file gets loaded into `Mine.py` to make all the API requests.

After mining all the data into `db/corpus.txt` you're done! Just kidding, but it's almost that simple.

`Markov.py` simply uses the [markovify](https://github.com/jsvine/markovify) python library to generate the model. From there you can go on to use markovify's methods as you wish, or export the model as a `model.json` file to save for later.

Then just run everything:

To load an existing model from `db/model.json`:
```
python3 Markov.py -l
```
To refresh the whole model and refresh `db/corpus.txt`:
```
python3 Markov.py -r
```

## Example Chains!

> Phone rings, it”s the neighbors: “Can you put the garlic in a room full of racists, bigots, terrorists, killers, rapists, pedophiles, and so are you sure you're ok?

> I don't understand why they had to make a move but I have never been good when it comes to guys.

> For video games and all the research published so far; 99% is shit.

> Is it socially acceptable to make out with anyone random.

> I'm at 350lb and fluffy, but I came in, but because I have a pretty chivalrous guy and girl that will help her when talking to me that I'm a straight up left to do it and I don't think he is so strong between us, I'm thankful for all their food frozen.

They don't always make sense, but it's fun to see what the model comes up with!

