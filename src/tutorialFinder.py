import praw
import sys
import pprint

from prawcore.exceptions import (BadRequest)

from flask import Flask

from flask import ( Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from src.auth import login_required
from src.db import get_db


bp = Blueprint('tutorialFinder', __name__)

reddit = praw.Reddit(client_id='TgY85H8sbIQ1Cw', client_secret='2h3wwLLS-J2FlqCXk0IxgioCnlI', user_agent='MUL Tutorial Finder 0.1')

subredditList = ['makeuplounge', 'makeupaddiction']
subredditFlairs = {'makeuplounge': 'Technique/Tutorial', 'makeupaddiction': 'Tutorial'}

def findTutorial(sub, flair, product):
    subreddit = reddit.subreddit(sub)
    flair = "flair:" + flair
    matchingPosts = []
    submissions = subreddit.search(query=flair, sort = 'top', time_filter='all')
    #print('searching ' , len(submissions), ' submissions')
    print(vars(submissions))
    for submission in submissions:
        author = submission.author
        authorComments = [comment for comment in submission.comments.list() if comment.author == author and  comment.is_root]
        
        if len(authorComments)<1:
            continue
        
        for comment in authorComments:
            if product.lower() in comment.body.lower():
                matchingPosts.append(submission)

                print ("Title: ", submission.title)
                print(submission.preview.get('images')[0].get('source').get('url'))
                #print(vars(submission.preview.get('images')[0]))
                print ("---------------------------------\n")
                break
    
    print('found posts: ', len(matchingPosts))
    return matchingPosts

@bp.route('/')
def findTutorials():
    if len(request.args) == 0:
        return render_template('tutorialFinder/tutorialFinder.html', subreddits=subredditList)
    
    print("request args")    
    dictionary = request.args
    for key in dictionary:
        print (dictionary.get(key))
        print (dictionary.getlist(key))

    subsToSearch = request.args.getlist('subs')
    terms = request.args.get('searchterms')
    if subsToSearch is None: 
        return render_template('error.html', message='please select at least one sub')
    if terms is None or len(terms) == 0:
        return render_template('error.html', message='please input at least one search term')
    print('search terms: ', terms)

    allMatchingPosts = []

    
    for sub in subsToSearch:
        print(sub)
        print(type(sub))
        print('subreddit=', sub, ' flair=', subredditFlairs[sub])
        try:
            allMatchingPosts.extend(findTutorial(sub, subredditFlairs[sub], terms))
        except BadRequest:
            render_template('error.html', message='Bad request - check https://reddit.statuspage.io/')
    print('Found ', len(allMatchingPosts), ' total posts')
    return render_template('tutorialFinder/results.html', posts = allMatchingPosts)
    
