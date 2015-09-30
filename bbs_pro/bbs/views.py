from django.shortcuts import render_to_response
from models import BBS,Categray,BBS_user,Chat
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
#-*- coding:utf-8 -*-
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
# Create your views here.

def index(req):
	bbs = BBS.objects.all()
	paginator = Paginator(bbs,5)
	page = req.GET.get('page')
	try:
		bbs_list = paginator.page(page)
	except PageNotAnInteger:
		bbs_list = paginator.page(1)
	except EmptyPage:
		bbs_list = paginator.page(paginator.num_pages)
	chat_list = Chat.objects.all()[0:5]
	chat_list = chat_list[::-1]	
	categray = Categray.objects.all()
	return render_to_response('index.html',{'bbs_list':bbs_list,
											'user':req.user,
											'categray_list':categray,
											'chat_list':chat_list})

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
	if comment:
		Comment.objects.create(
			content_type_id = 7,
			object_pk = id,
			site_id = 1,
			user = req.user,
			comment = comment,
			)
	return HttpResponseRedirect('/detail/%s'%id)


def bbs_pub(req):
	categray = Categray.objects.all()
	return render_to_response('publish.html',{'user':req.user,
											  'categray_list':categray})

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
	bbs = BBS.objects.filter(categray = categray_name)
	paginator = Paginator(bbs,5)
	page = req.GET.get('page')
	try:
		bbs_list = paginator.page(page)
	except PageNotAnInteger:
		bbs_list = paginator.page(1)
	except EmptyPage:
		bbs_list = paginator.page(paginator.num_pages)
	categray = Categray.objects.all()
	return render_to_response('index.html',{'bbs_list':bbs_list,
											'user':req.user,
											'categray_list':categray,
											'code_id':int(id)})

@csrf_exempt
def chat_sub(req):
	auth = req.user
	content = req.POST.get('content')
	Chat.objects.create(
		content = content,
		author = auth,
		)
	return HttpResponse('true')

@csrf_exempt
def chat_pub(req):
	id = req.POST.get('id')
	chat_list = Chat.objects.get(id = id)
	if chat_list:	
		return render_to_response('chat.html',{'chat_list':chat_list})
	else:
		return render_to_response('chat.html')
	
		