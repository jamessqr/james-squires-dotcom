from django.contrib.syndication.views import Feed
from blog.models import Entry
from django.utils.feedgenerator import Rss201rev2Feed

class CorrectMimeTypeFeed(Rss201rev2Feed):
    mime_type = 'application/xml'

# This is a django.contrib.syndication.feeds.Feed subclass whose feed_type
# is set to our preferred MIME type.
class BlogFeed(Feed):
    feed_type = CorrectMimeTypeFeed
    	
class LatestEntriesFeed(BlogFeed):	
    title = "James Squires - An outdoor journal"
    link = "http://www.james-squires.com"
    description = "James Squires is an outdoor enthusiast with passions for bowhunting midwest whitetails and fly fishing the small streams of the driftless area."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body