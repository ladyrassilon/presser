import unittest

from presser.presser import Presser
from presser.exceptions import PresserJavaScriptParseError, PresserURLError, Presser404Error, PresserRequestError

EXPECTED_VINE = {
    u'avatarUrl': u'http://v.cdn.vine.co/r/avatars/9D5770C2B11093640923147292672_241c89c013c.0.4.jpg?versionId=N7epx0AXV8yx.ZR1EnwMaqyn1riq1Hgm',
    u'comments': {
        u'anchor': None,
        u'anchorStr': None,
        u'backAnchor': u'',
        u'count': 0,
        u'nextPage': None,
        u'previousPage': None,
        u'records': [],
        u'size': 10
    },
    u'created': u'2014-07-24T21:15:41.000000',
    u'description': u'Rainbow dash',
    u'entities': [],
    u'explicitContent': 0,
    u'foursquareVenueId': u'4ab5691ef964a520707420e3',
    u'foursquareVenueIdStr': u'4ab5691ef964a520707420e3',
    u'liked': 0,
    u'likes': {
        u'anchor': None,
        u'anchorStr': None,
        u'backAnchor': u'',
        u'count': 0,
        u'nextPage': None,
        u'previousPage': None,
        u'records': [],
        u'size': 10
    },
    u'loops': {
        u'count': 62, u'onFire': 0, u'velocity': 0
    },
    u'myRepostId': 0,
    u'myRepostIdStr': u'0',
    u'permalinkUrl': u'https://vine.co/v/M0WmADraAD2',
    u'postId': 1104202231840116700,
    u'postIdStr': u'1104202231840116736',
    u'private': 0,
    u'reposts': {
        u'anchor': None,
        u'anchorStr': None,
        u'backAnchor': u'',
        u'count': 0,
        u'nextPage': None,
        u'previousPage': None,
        u'records': [],
        u'size': 10
    },
    u'shareUrl': u'https://vine.co/v/M0WmADraAD2',
    u'shortId': u'M0WmADraAD2',
    u'tags': [],
    u'thumbnailUrl': u'http://v.cdn.vine.co/r/thumbs/DEB2A6EAC91104202215885008896_27992670f1e.1.2.5318815706057142197.mp4.jpg?versionId=jBAUu6ahv1JwdKVNFg2jnwSf4PLlpvuO',
    u'userId': 1073609278625148900,
    u'userIdStr': u'1073609278625148928',
    u'username': u'Gemma Hentsch',
    u'vanityUrls': [],
    u'venueAddress': u'Rungestr. 20',
    u'venueCategoryIconUrl': u'https://foursquare.com/img/categories_v2/building/eventspace_32.png',
    u'venueCategoryId': u'4bf58dd8d48988d171941735',
    u'venueCategoryIdStr': u'4bf58dd8d48988d171941735',
    u'venueCategoryShortName': u'Event Space',
    u'venueCity': u'Berlin',
    u'venueCountryCode': u'DE',
    u'venueName': u'c-base',
    u'venueState': u'Berlin',
    u'verified': 0,
    u'videoDashUrl': None,
    u'videoLowURL': u'http://v.cdn.vine.co/r/videos_r1/DFCD3B0B9C1104202213573693440_22f7d6615ca.1.2.5318815706057142197.mp4?versionId=.RofqiDr6rlf1snQgqJve9p.bjEpI720',
    u'videoUrl': u'http://mtc.cdn.vine.co/r/videos/DFCD3B0B9C1104202213573693440_22f7d6615ca.1.2.5318815706057142197.mp4?versionId=jnyF8noA.fT_Egg2Yg1VUSxqjkdDHTZD'
}

EXPECTED_VINE_URL = 'https://vine.co/v/M0WmADraAD2'

EXPECTED_VINE_ID = 'M0WmADraAD2'
class VineStructureTest(unittest.TestCase):

    def setUp(self):
        self.presser = Presser()

    def test_vine_is_returned(self):
        vine = self.presser.get_data_for_vine_from_url(EXPECTED_VINE_URL)
        self.assertEqual(vine["permalinkUrl"], EXPECTED_VINE_URL)

    def test_non_existant_vine_errors(self):
        self.assertRaises(Presser404Error, self.presser.get_data_for_vine_from_url, "https://vine.co/v/NOTAVINE")

    def test_keys_in_response(self):
        KEYS = [
            u'username',
            u'videoUrl',
            u'liked',
            u'videoDashUrl',
            u'description',
            u'tags',
            u'foursquareVenueId',
            u'venueCategoryId',
            u'permalinkUrl',
            u'userId',
            u'userIdStr',
            u'private',
            u'foursquareVenueIdStr',
            u'postIdStr',
            u'likes',
            u'venueCategoryIdStr',
            u'loops',
            u'verified',
            u'venueCity',
            u'postId',
            u'explicitContent',
            u'myRepostId',
            u'venueState',
            u'vanityUrls',
            u'venueCategoryIconUrl',
            u'thumbnailUrl',
            u'myRepostIdStr',
            u'avatarUrl',
            u'venueName',
            u'created',
            u'shareUrl',
            u'shortId',
            u'comments',
            u'entities',
            u'videoLowURL',
            u'venueCountryCode',
            u'venueCategoryShortName',
            u'venueAddress',
            u'reposts'
        ]
        vine = self.presser.get_data_for_vine_from_url(EXPECTED_VINE_URL)
        for key in KEYS:
            self.assertTrue(key in vine)

    def test_static_variables(self):
        EXPECTED_STATIC_VALUES = {
            u'created': u'2014-07-24T21:15:41.000000',
            u'description': u'Rainbow dash',
            u'permalinkUrl': u'https://vine.co/v/M0WmADraAD2',
            u'postId': 1104202231840116700,
            u'shortId': u'M0WmADraAD2',
            u'thumbnailUrl': u'http://v.cdn.vine.co/r/thumbs/DEB2A6EAC91104202215885008896_27992670f1e.1.2.5318815706057142197.mp4.jpg?versionId=jBAUu6ahv1JwdKVNFg2jnwSf4PLlpvuO',
            u'userId': 1073609278625148900,
            u'videoUrl': None,
            u'videoUrls': [
                {
                    'default': 1,
                    'format': 'h264',
                    'id': 'original',
                    'idStr': 'original',
                    'rate': 200,
                    'videoUrl': 'http://mtc.cdn.vine.co/r/videos/DFCD3B0B9C1104202213573693440_22f7d6615ca.1.2.5318815706057142197.mp4?versionId=jnyF8noA.fT_Egg2Yg1VUSxqjkdDHTZD'
                },
                {
                    'format': 'h264',
                    'id': 'r1',
                    'idStr': 'r1',
                    'rate': 0,
                    'videoUrl': 'http://mtc.cdn.vine.co/r/videos_r1/DFCD3B0B9C1104202213573693440_22f7d6615ca.1.2.5318815706057142197.mp4?versionId=.RofqiDr6rlf1snQgqJve9p.bjEpI720'
                },
                {
                    'default': 1,
                    'format': 'h264c',
                    'id': 'r1',
                    'idStr': 'r1',
                    'rate': 0,
                    'videoUrl': 'http://mtc.cdn.vine.co/r/videos_r1/DFCD3B0B9C1104202213573693440_22f7d6615ca.1.2.5318815706057142197.mp4?versionId=.RofqiDr6rlf1snQgqJve9p.bjEpI720'
                }]
        }
        vine = self.presser.get_data_for_vine_from_url(EXPECTED_VINE_URL)
        for key, value in EXPECTED_STATIC_VALUES.items():
            self.assertEqual(value, vine[key])