In:
A directory path

Out:
A dictionary of words, counted from .txt files, including ones in archives and sub-dirs
A histogram generated from the dictionary

Setup:
1. install Python 3.5.2
2. install pip
3. install Numpy: pip install numpy==1.12.0
4. install Matplotlib: pip install matplotlib==2.0.0

Usage:
python text_scanner.py [some-directory]
    example: python text_scanner.py res/simple
    p.s. change the number at line 22 of text_scanner.py to see top n used words

List of supported archive formats:
(Relies on helper applications to handle those archive formats (for example bzip2 for BZIP2 archives))
7z (.7z, .cb7), ACE (.ace, .cba), ADF (.adf), ALZIP (.alz), APE (.ape), AR (.a),
ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab), COMPRESS (.Z), CPIO (.cpio),
DEB (.deb), DMS (.dms), FLAC (.flac), GZIP (.gz), ISO (.iso), LRZIP (.lrz),
LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo), RPM (.rpm),
RAR (.rar, .cbr), RZIP (.rz), SHN (.shn), TAR (.tar, .cbt), XZ (.xz),
ZIP (.zip, .jar, .cbz) and ZOO (.zoo) archive formats.

Environment, dependencies and libraries:
Python 3.5.2
Patool 1.12 (included)
Numpy 1.12.0 (pip install numpy==1.12.0)
Matplotlib 2.0.0 (pip install matplotlib==2.0.0)

Tested on Python 3.5.2
Files in ./res/ folder belongs to Paradox Interactive, see policy here https://www.paradoxplaza.com/mod-policy-en