
# Purdue Confessions Markov Generator

A simple Markov Generator based on the [Purdue Confession](https://www.facebook.com/PurdueC/) facebook page.

The first part was mining the data via the [Facebook Graph API](https://developers.facebook.com/docs/graph-api/reference/v2.9/page/). You can use the [explorer](https://developers.facebook.com/tools/explorer/) to test out the API if you wish. You can also use it to find the page id and generate an API key.

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

