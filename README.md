# mul-tutorial-finder
Find tutorials on /r/MakeupLounge by product. UI almost exactly the UI from the [Flask Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/factory/). Note: Sign in/Register is only partially implemented.

## Installation
1. Have python 3 installed on your system. Check [here](https://www.python.org/downloads/) for downloads/instructions. I was using Python 3.6.7 during development.
2. Clone the repo
3. Create the virtual environment for the project 
	1. Open the repo's directory in a command prompt/console
	2. Create and activate the vitual environment 
		
		Linux:
		```
		python3 -m venv venv
		. venv/bin/activate
		```
		Windows:
		```
		py -3 -m venv venv
		venv\Scripts\activate
		```
4. Install dependencies
	```
	pip install Flask
	pip install praw
	```
5. Create environment variables & run
	
	Linux: 
	```
	export FLASK_APP=src
	export FLASK_ENV=development
	flask run
	```
	Windows:
	```
	$env:FLASK_APP = "src"
	$env:FLASK_ENV = "development"
	flask run
	```
## Future Plans
- add loading screen when fetching tutorials and looking for matches
- allow user to pick the sort of the search (right now it sorts by 'top', but reddit offers other options)
- allow user to limit the number of submissions searched (default limit is 100)
- expand to other subreddits that have a defined flair/top level comment structure (different searches)

### Reach Goals
- create db of pallettes, search by every shade in the palette if the palette is the search term
- allow users to create profiles where they can save their favorite products, implement a roullette wheel that picks product and finds a tutorial

Suggestions? Critiques? More use cases? Let me know!


Made possible by [Flask](http://flask.pocoo.org/docs/1.0/#) and [Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/index.html)
