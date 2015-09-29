#-*- coding:utf-8 -*-
from django.contrib import admin
from models import *
# Register your models here.
class BBS_admin(admin.ModelAdmin):
	list_display = ('title','summary','author','signature','view_count')
	list_filter = ('created_at',)
	search_fields = ('title','author__user__username')

	#调用外键的内容。。。
	def signature(self,obj):
		return obj.author.signature
	signature.short_description='hah'

class Chat_admin(admin.ModelAdmin):
	list_display = ('content','author','submit_at')

admin.site.register(BBS,BBS_admin)
admin.site.register(Categray)
admin.site.register(BBS_user)
admin.site.register(Chat,Chat_admin)