from __future__ import unicode_literals

import logging
from mopidy import backend
from mopidy.models import Album, Artist, Ref, Track
import pykka
import mopidy_intergalacticfm
from .intergalacticfm import IntergalacticFMClient


logger = logging.getLogger(__name__)


class IntergalacticFMBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(IntergalacticFMBackend, self).__init__()

        self.intergalacticfm = IntergalacticFMClient(
            config['proxy'],
            "%s/%s" % (
                mopidy_intergalacticfm.Extension.dist_name,
                mopidy_intergalacticfm.__version__))
        self.library = IntergalacticFMLibraryProvider(backend=self)

        self.uri_schemes = ['intergalacticfm']
        self.quality = config['intergalacticfm']['quality']
        self.encoding = config['intergalacticfm']['encoding']

    def on_start(self):
        self.intergalacticfm.refresh(self.encoding, self.quality)


class IntergalacticFMLibraryProvider(backend.LibraryProvider):

    root_directory = Ref.directory(uri='intergalacticfm:root', name='Intergalactic FM')

    def lookup(self, uri):
        # Whatever the uri, it will always contains one track
        # which is a url to a pls

        if not uri.startswith('intergalacticfm:'):
            return None

        channel_name = uri[uri.index('/') + 1:]
        channel_data = self.backend.intergalacticfm.channels[channel_name]

        # Artists
        artist = Artist(name=channel_data['dj'])

        # Build album (idem as playlist, but with more metada)
        album = Album(
            artists=[artist],
            date=channel_data['updated'],
            images=[channel_data['image']],
            name=channel_data['title'],
            uri='intergalacticfm:channel:/%s' % (channel_name))

        track = Track(
            artists=[artist],
            album=album,
            genre=channel_data['genre'],
            name=channel_data['title'],
            uri=channel_data['pls'])

        return [track]

    def browse(self, uri):

        if uri != 'intergalacticfm:root':
            return []

        result = []
        for channel in self.backend.intergalacticfm.channels:
            result.append(Ref.track(
                uri='intergalacticfm:channel:/%s' % (channel),
                name=self.backend.intergalacticfm.channels[channel]['title']
                ))

        result.sort(key=lambda ref: ref.name)
        return result
