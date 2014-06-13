from google.appengine.ext import ndb

# TODO: Convert this non-Endpoints version to use Endpoint Models!


class Weatherpic(ndb.Model):
    """ Model to store a WeatherPic. """
    image_url = ndb.StringProperty()
    caption = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
