import unittest

from mopidy_intergalacticfm.intergalacticfm import IntergalacticFMClient


class IntergalacticFMClientTest(unittest.TestCase):

    def test_refresh(self):
        sfmc = IntergalacticFMClient()
        sfmc.refresh('mp3', 'highest')

        self.assertIsNotNone(sfmc.channels)
        self.assertNotEqual(len(sfmc.channels), 0)

    def test_refresh_firewall(self):
        sfmc = IntergalacticFMClient()
        sfmc.refresh('mp3', 'firewall')

        self.assertIsNotNone(sfmc.channels)
        self.assertNotEqual(len(sfmc.channels), 0)

    def test_refresh_no_channels(self):
        sfmc = IntergalacticFMClient()
        sfmc.CHANNELS_URI = ''
        sfmc.refresh('mp3', 'highest')

        self.assertDictEqual(sfmc.channels, {})
        self.assertEqual(len(sfmc.channels), 0)

    def test_downloadContent(self):
        url = "http://intergalacticfm.com/channels.xml"
        sfmc = IntergalacticFMClient()
        data = sfmc._downloadContent(url)
        self.assertNotEqual(len(data), 0)

    def test_extractStreamUrlFromPls(self):
        url = "http://intergalacticfm.com/ifm1-128mp3.pls"
        sfmc = IntergalacticFMClient()
        data = sfmc.extractStreamUrlFromPls(url)
        self.assertNotEqual(len(data), 0)
        self.assertNotEqual(data, url)

    def test_extractStreamUrlFromPls_unknown(self):
        url = "http://intergalacticfm.com/ifm2-128mp3.pls"
        sfmc = IntergalacticFMClient()
        data = sfmc.extractStreamUrlFromPls(url)
        self.assertNotEqual(len(data), 0)
        self.assertEqual(data, url)
