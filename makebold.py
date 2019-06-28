#!/usr/bin/python
import fontforge
f=fontforge.open("FelineseRegular.sfd")
f.weight="Bold"
f.fontname="FelineseBold"
f.fullname="Felinese Bold"
f.appendSFNTName(1038, "SubFamily", "Félkövér")
f.appendSFNTName(1043, "SubFamily", "Vet")
f.selection.all()
for glyph in list(f.selection.byGlyphs):
  glyph.changeWeight(25, "LCG", 0, 0, "auto", 0)
f.save("FelineseBold.sfd")
f.close()
