*************
Mopidy-IntergalacticFM
*************

.. image:: https://img.shields.io/pypi/v/Mopidy-IntergalacticFM.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-IntergalacticFM/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-IntergalacticFM.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-IntergalacticFM/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/intergalacticfm/mopidy-intergalacticfm/master.png?style=flat
    :target: https://travis-ci.org/intergalacticfm/mopidy-intergalacticfm
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/intergalacticfm/mopidy-intergalacticfm/master.svg?style=flat
   :target: https://coveralls.io/r/intergalacticfm/mopidy-intergalacticfm?branch=master
   :alt: Test coverage


`Mopidy <http://www.mopidy.com/>`_ extension for playing music from
`Intergalactic FM <http://intergalacticfm.com/>`_.


.. image:: icon.png
   :alt: Intergalactic FM icon


Installation
============


Debian/Ubuntu
-------------

This package is available from `apt.mopidy.com <http://apt.mopidy.com/>`_.

This can be installed by running::

    sudo apt-get install mopidy-intergalacticfm

Other
-----

Install by running::

    pip install Mopidy-IntergalacticFM


Configuration
=============

The extension requires that the Mopidy-Stream extension is enabled. It is
bundled with Mopidy and enabled by default, so it will be available unless
you've explicitly disabled it.

You may change prefered quality and encoding in your Mopidy configuration file::

    [intergalacticfm]
    encoding = aac
    quality = highest

- ``encoding`` must be either ``aac``, ``mp3`` or ``aacp``
- ``quality`` must be one of ``highest``, ``fast``, ``slow``, ``firewall``


Warning
=======

Intergalactic FM does not provide every possible combination of ``encoding`` and ``quality``.

For example, as of 2016/05/19, ``mp3 + highest`` gives 4 playlists while ``aac + highest`` gives only. All other combinations, for now, do not give any playlists.

Some combinations are incompatible and will give zero playlist: ``aacp + highest`` and ``aac + fast``.


.. image:: fanart.jpg
   :alt: Intergalactic FM fanart


Project resources
=================

- `Source code <https://github.com/intergalacticfm/mopidy-intergalacticfm>`_
- `Issue tracker <https://github.com/intergalacticfm/mopidy-intergalacticfm/issues>`_
- `Download development snapshot <https://github.com/intergalacticfm/mopidy-intergalacticfm/tarball/master#egg=Mopidy-IntergalacticFM-dev>`_


Thanks
======

Thanks go to the authors of the original add-on that was developed for SomaFM for allowing to fork their work from https://github.com/AlexandrePTJ/mopidy-somafm

For that and other projects using channels.xml and channels.json, I also developed a schema for XML and JSON to describe online radio station channels, see https://github.com/intergalacticfm/online-radio-channels For this, thanks go to SomaFM for allowing to describe their dataformat and reviewing my work.

Last but not least, thank you I-f and others for creating `Intergalactic FM <http://intergalacticfm.com>`_ and embracing new initiatives and technologies to keep us all in musical orbit.
