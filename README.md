# gameoflife

## Setup

* Built with Python 3.9.6
* (Virtualenv recommended: `mkvirtualenv gameoflife`)
* `pip install -r requirements.txt`

To run on `http://locahost:5000`

`python service.py`

And the tests

`pytest`

## Usage

* `POST /new` to create a new board. Accepts `{width: N, height: M}` in payload to set the size of the board
* `POST /state` sets the state of an existing board. This is formatted as a single array:

e.g.

```
0 1 0
0 0 0
0 1 0
```

would encode as `[0, 1, 0, 0, 0, 0, 0, 1, 0]`

* `GET /tick` iterates Conway's GOL one step forward, and returns the new state






