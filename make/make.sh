mkdir ./out
rm ./out/*
rm ./rawya.*
python make/makeglyph.py
# python make/makeplaydate.py
python make/makepfb.py