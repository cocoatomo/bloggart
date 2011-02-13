====
memo
====

memo for me.

url settings
############
app.yaml

   handlers:
   - url: /remote_api
     script: $PYTHON_LIB/google/appengine/ext/remote_api/handler.py
     login: admin

   - url: /_ah/queue/deferred
     script: deferred.py
     login: admin

   - url: /admin/.*
     script: admin.py
     login: admin

   - url: /static/([^/]+)/(.*)
     static_files: themes/\1/static/\2
     upload: themes/[^/]+/static/.*

   - url: /.*
     script: static.py

entry point is static.py
↓
register the StaticContentHandler (static.py L123) class as application

class StaticContentHandler(webapp.RequestHandler):
  def output_content(self, content, serve=True):
  ...
  def get(self, path):
  ...



structure of this library
#########################

lib
***

pygments
========
syntax hilighter
http://pygments.org/

- why this framework needs this library?
- where is this library used?

dependency
**********

how to use this blog engine
###########################

config.py
*********
setting file.
this file contains documentation for users.

