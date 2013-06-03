#Simple Spam Filter
It is a simple spam filter using Bayesian method. 
Sadly, I can only provide a simple api, not the whole plugin of the spam filter.
##Test The Spam Filter
The main function of this application is `classify()` in `classify.py`.
If the `feature.db` already exists, you can test the main function in this way:
```python
from classify import classify

print classify(txt)
```
Another way to test is just using the simple `test.py`: `python test.py`. You can just read the source code of `test.py`.

If the `feature.db`  not exists yet, you have run `python train.py` first to generate the database for classifying mails.

##Add (or Change) Corpus
You can add file folders of spams or hams to the corpus by adding file folders in `corpus/` folder.
You can see there already exists many folders.
Then you should register your own folders either in `spam.list` or `ham.list`
After that, you should run `python train.py` to generate datebase according to the Corpus.
It may take quite a while.




