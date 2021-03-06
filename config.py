# Name of the blog
blog_name = 'Elliptium'

# Your name (used for copyright info)
author_name = 'cocoatomo'

# copyright years
copyright_years = '2011-2013'

# (Optional) slogan
slogan = 'powered by my impulse'

# The hostname this site will primarially serve off (used for Atom feeds)
host = 'blog.elliptium.net'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'cocoatomo'

# List of page templates
page_templates = {
	'Theme.html': 'Theme',
	'Simple.html': 'Simple',
}

# Defines the URL organization to use for blog postings. Valid substitutions:
#   slug - the identifier for the post, derived from the title
#   year - the year the post was published in
#   month - the month the post was published in
#   day - the day the post was published in
post_path_format = '/%(year)d/%(month)02d/%(slug)s'

# A nested list of sidebar menus, for convenience. If this isn't versatile
# enough, you can edit themes/default/base.html instead.
sidebars = [
    ('Profile', [
            '<a href="http://twitter.com/cocoatomo">@cocoatomo</a>',
            '<a href="http://d.hatena.ne.jp/cocoatomo">hatena diary (my old blog)</a>',
            '<a href="http://iddy.jp/profile/cocoatomo/">iddy</a>',
            ]),
    ('Licenses', [
            '''<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.1/jp/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/2.1/jp/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.1/jp/deed.en_US">Creative Commons Attribution-ShareAlike 2.1 Japan License</a>.''',
            '''This blog engine is derived from Arachnid's work <a href="https://github.com/arachnid/bloggart">bloggart</a>.''',
            '''This blog is originally designed by <a href="http://www.styleshout.com/">styleshout</a>.'''
            ])
]

# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
disqus_forum = 'elliptium'

# Length (in words) of summaries, by default
summary_length = 200

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = 'UA-6577093-6'

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to ping Google Sitemap when your sitemap is generated change this to True, else False
# see: http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=34609 for more information
google_sitemap_ping = True

# If you want to use Google Site verification, go to
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = None

# Default markup language for entry bodies.
# one of 'txt', 'textile', 'html', 'markdown' and 'rst'
default_markup = 'rst'

# Syntax highlighting style for RestructuredText and Markdown,
# one of 'manni', 'perldoc', 'borland', 'colorful', 'default', 'murphy',
# 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
# 'friendly', 'native'.
highlighting_style = 'friendly'

# Absolute url of the blog application use '/blog' for host/blog/
# and '' for host/.Also remember to change app.yaml accordingly
url_prefix = ''

# Defines where the user is defined in the rel="me" of your pages.
# This allows you to expand on your social graph.
rel_me = None

# For use a feed proxy like feedburne.google.com
feed_proxy = None

# To use Google Friends Connect.                                          
# If you want use Google Friends Connect, go to http://www.google.com/friendconnect/ 
# and register your domain for get a Google Friends connect ID.
google_friends_id = None
google_friends_comments = True # For comments.
google_friends_members  = True # For a members container.

# To format the date of your post.
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#now
date_format = "d F, Y"
