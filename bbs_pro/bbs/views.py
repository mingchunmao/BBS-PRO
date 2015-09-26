from django.shortcuts import render_to_response
from models import BBS,Categray,BBS_user
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
# Create your views here.


def index(req):
	bbs_list = BBS.objects.all()
	return render_to_response('index.html',{'bbs_list':bbs_list})

def detail(req,bbs_id):
	bbs_list = BBS.objects.get(id = bbs_id)
	return render_to_response('detail.html',{'bbs':bbs_list})


def sub_comment(req):
	id = req.POST['bbs_id'] 
	return HttpResponseRedirect('/detail/%s'%id)