#!/usr/bin/env python
#encoding=utf-8
'''
Created on 2013-12-15

@author: wlx
'''

import os

from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor
from mako.template import Template
from mako.lookup import TemplateLookup

# 基本路径参数
app_dir = os.path.dirname(__file__)
static_dir = os.path.join(app_dir, 'static')
template_dir = os.path.join(app_dir, 'templates')
# 基本应用参数
app_title = u'示例应用'
# 模板环境
lookup = TemplateLookup(directories=[template_dir], input_encoding='utf-8', output_encoding='utf-8')



class Root(Resource):
    ''' 首页，同时第一级URL路由 '''
    def getChild(self, name, request):
        if name == 'static':
            return File(static_dir)
        #session = request.getSession()
        
        else:
            return self
    def render_GET(self, request):
        tpl = lookup.get_template('index.html')
        return tpl.render(page={'app_title':app_title, 'page_title':u'首页'})


if __name__ == '__main__':
    factory = Site(Root())
    reactor.listenTCP(8880, factory)
    reactor.run()