import praw
import sys

from flask import Flask

from flask import ( Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('tutorialFinder', __name__)

reddit = praw.Reddit(client_id='TgY85H8sbIQ1Cw', client_secret='2h3wwLLS-J2FlqCXk0IxgioCnlI', user_agent='MUL Tutorial Finder 0.1')
subreddit = reddit.subreddit("makeuplounge")


subredditList = ['makeuplounge', 'makeupaddiction']

def setSubreddit(sub):
    subreddit = reddit.subreddit(sub)

def findTutorial(product):
    for submission in subreddit.search(query="flair:Technique/Tutorial", time_filter='all'):
        author = submission.author
        authorComments = [comment for comment in submission.comments.list() if comment.author == author and  comment.is_root]
    
        if len(authorComments)<1:
            continue
        
        for comment in authorComments:
            if product.lower() in comment.body.lower():
                print ("Title: ", submission.title)
                print ("Link: ", submission.permalink)
                print ("Score: ", submission.score)
                print ("---------------------------------\n")
                break

@bp.route('/')
def findTutorial():
    return render_template('tutorialFinder/tutorialFinder.html')

    
