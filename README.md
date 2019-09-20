# entrypoint

## Raw python file execution
Navigate to folder of app.py and run
```
python index.py
```

The app is then available on `http://localhost:8050/`

## Docker approach
Run from repo root
```
docker-compose up -d --build
```
The app is then available on `http://localhost:8051/`

# reference
Following this tutorial

https://www.datacamp.com/community/tutorials/learn-build-dash-python

and freestyling for additional functionality using the official Dash documentation, e.g. this

https://dash.plot.ly/live-updates

tutorial for CSS styling

https://www.youtube.com/watch?v=f2qUWgq7fb8

and using the following to add local CSS instead of from web (will be appended after vanilla dash css)

For multi-page stuff

https://dash.plot.ly/urls


# History of development (local development)

## in multipage_v5
putting in Docker container

Continue from this point in new project dash-multipage-app/ which is linked to github

## in multipage_v4
adding interactive annotation by clicking graph

## in multipage_v3

adding "navbar" (not full thing, just a simple link-based approximation), ability to read parameter values from url

## in multipage_v2

converted /v4 to multipage app

included background image, transparent figure backgrounds, 404 page

## in multipage_v1

Trying simple multipage stuff (two pages)

## Old below

### in v1
In v1 is a basic static dashboard showing two bar graphs on the same axes.

Also added a markdown example (handles a lot of text), presented a few paragraphs below simplest example in reference

### in v2
adding scatter plot, automatic loading of the latest data to the app (not just at the time of app launch), and automatic updating of text to reflect time. Also adding interactive text box

Added a CSS style sheet

### in v3
adding automatic interactivity between a dropdown and the app figure

### in v4
adding proper styling via bootstrap css
