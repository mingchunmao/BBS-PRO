from django.shortcuts import render_to_response
from models import BBS,Categray,BBS_user
from django.http import HttpResponseRedirect,HttpResponse
#-*- coding:utf-8 -*-
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
# Create your views here.


def index(req):
	bbs_list = BBS.objects.all()
	categray = Categray.objects.all()
	return render_to_response('index.html',{'bbs_list':bbs_list,
											'user':req.user,
											'categray_list':categray})

def detail(req,bbs_id):
	bbs_list = BBS.objects.get(id = bbs_id)
	categray = Categray.objects.all()
	return render_to_response('detail.html',{'bbs':bbs_list,
											'user':req.user,
											'categray_list':categray})

@csrf_exempt
def sub_comment(req):
	id = req.POST['bbs_id'] 
	# bbs_table_obj = ContentType.objects.get(id = 7)
	comment = req.POST.get('comment_comment')
	print comment
	Comment.objects.create(
		content_type_id = 7,
		object_pk = id,
		site_id = 1,
		user = req.user,
		comment = comment,
		)
	return HttpResponseRedirect('/detail/%s'%id)



def bbs_pub(req):
	return render_to_response('publish.html',{'user':req.user})

@csrf_exempt
def bbs_sub(req):
	author = BBS_user.objects.get(user=req.user)
	content = req.POST.get('content')
	categray_id = req.POST.get('categray_id')
	BBS.objects.create(
		title = req.POST['title'],
		summary = req.POST['summary'],
		content = content,
		author = author,
		view_count = 1,
		ranking = 1,
		categray_id = categray_id,
		)
	return HttpResponseRedirect('/')


def categray(req,id):
	categray_name = Categray.objects.get(id = id)
	bbs_list = BBS.objects.filter(categray = categray_name)
	categray = Categray.objects.all()
	return render_to_response('index.html',{'bbs_list':bbs_list,
											'user':req.user,
											'categray_list':categray,
											'code_id':int(id)})