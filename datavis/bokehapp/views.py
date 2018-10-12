from django.shortcuts import render
from . import BasicLine
from bokeh.embed import server_session
from bokeh.util import session_id

def index(request):
    context={
        "div":BasicLine.div,
        "js":BasicLine.js,
        "cdn_js":BasicLine.cdn_js,
        "cdn_css":BasicLine.cdn_css
    }
    return render(request, 'bokehapp/index.html', context)

def interactive(request):
    #bokeh_script=autoload_server(None,  url="http://localhost:5006/random-generator")
    server_script = server_session(None, session_id=session_id.generate_session_id(), url="http://localhost:5006/slider")
    context = {"graphname":"Sliders",
            "server_script": server_script,
    }
    return render(request, 'bokehapp/interactive.html', context)