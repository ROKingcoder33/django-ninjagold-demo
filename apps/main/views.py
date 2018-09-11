from django.shortcuts import render, redirect
import random

# Create your views here.
def index(req):
  if 'gold_count' not in req.session:
    req.session['gold_count'] = 0
  
  if 'activities' not in req.session:
    req.session['activities'] = []
  return render(req, 'main/index.html')

def process(req):
  if req.method != "POST" or 'location' not in req.POST:
    return redirect('/')

  location_map = {
    'cave': random.randint(5, 10),
    'house': random.randint(2, 5),
    'farm': random.randint(10, 20),
    'casino': random.randint(-50, 50)
  }

  if req.POST['location'] not in location_map:
    return redirect('/')

  curr_gold = location_map[req.POST['location']]

  req.session['gold_count'] += curr_gold

  if curr_gold > 0:
    activity = {
      'content': "You won {} golds at the {}.".format(curr_gold, req.POST['location']),
      'css_class': 'green'
    }
  else:
    activity = {
      'content': "You lost {} golds at the {}.".format(curr_gold * -1, req.POST['location']),
      'css_class': 'red'
    }
  
  req.session['activities'].insert(0, activity)
  req.session.modified = True

  return redirect('/')

def reset(req):
  req.session.clear()
  return redirect('/')

def color(req, color):
  print "*" * 80
  print color
  return redirect('/')