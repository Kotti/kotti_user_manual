import os
import glob
from cStringIO import StringIO
from optparse import OptionParser
from blockdiag import parser
from blockdiag import builder
from blockdiag import drawer
from blockdiag.utils.fontmap import FontMap
from blockdiag.utils.config import ConfigParser
from blockdiag.utils.bootstrap import Application

options = None
fontmap = FontMap()

#fontmap = FontMap(StringIO("""[fontmap]
#sans-bold:        dejavu-fonts-ttf-2.33/ttf/DejaVuSans-Bold.ttf
#sans-boldoblique: dejavu-fonts-ttf-2.33/ttf/DejaVuSans-BoldOblique.ttf
#sans-extralight:  dejavu-fonts-ttf-2.33/ttf/DejaVuSans-ExtraLight.ttf
#sans-oblique:     dejavu-fonts-ttf-2.33/ttf/DejaVuSans-Oblique.ttf
#sans-normal:      dejavu-fonts-ttf-2.33/ttf/DejaVuSans.ttf"""))

ttf_fonts = \
    [('sansserif-bold', os.path.abspath(
             'dejavu-fonts-ttf-2.33/ttf/DejaVuSans-Bold.ttf')),
     ('sansserif-oblique', os.path.abspath(
             'dejavu-fonts-ttf-2.33/ttf/DejaVuSans-Oblique.ttf')),
     ('sansserif-normal', os.path.abspath(
             'dejavu-fonts-ttf-2.33/ttf/DejaVuSans.ttf'))]

fontmap.set_default_fontfamily('sansserif-normal')
fontmap.set_default_font(os.path.abspath('dejavu-fonts-ttf-2.33/ttf/DejaVuSans.ttf'))

# Add all the fonts to the fontmap.
[fontmap.append_font(ttf_font[0], ttf_font[1]) for ttf_font in ttf_fonts]


for filename in glob.glob('blockdiag/*'):

    diagram_definition = open(filename).read()

    tree = parser.parse_string(diagram_definition)

    diagram = builder.ScreenNodeBuilder.build(tree)

    image_path = \
            "../docs/images/{0}".format(filename[len('blockdiag/'):-4] + 'png')

    print 'saving', image_path
    draw = drawer.DiagramDraw('PNG',
                              diagram,
                              filename=image_path,
                              fontmap=fontmap,
                              antialias=True,
                              transparency=True)
    draw.draw()
    draw.save()
