from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import ContactForm
from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates/')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            asn = request.POST.get('asn', '')
            peer = request.POST.get('peer', '')
            peerasn = request.POST.get('peerasn', '')
            netw = request.POST.get('netw', '')
            env = Environment(loader=file_loader)
            template = env.get_template('bgp_template.j2')
            res_output = template.render(j2_asn=asn, j2_peer=peer, j2_peerasn=peerasn, j2_netw=netw)
            return render(request, 'index.html', {'form' : form, 'output' : res_output})
        else:
            print("Validation failed..")
            #raise Http404
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

