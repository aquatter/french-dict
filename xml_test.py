__author__ = 'alomakin'

from xml.dom.minidom import parse
import io

ndic = 58
path = r'c:\Users\alomakin.lomakin-home\AppData\Local\ABBYY\Lingvo\15.0\Dic\TutorDict'

dom1 = parse( path + '/dic_{}FrRu.xml'.format( ndic ) )
f = io.open( path + '/dic_{}.bxd'.format( ndic ), 'w', encoding='utf-16' )

for cards in dom1.getElementsByTagName( 'card' ):
    text_word = cards.getElementsByTagName( 'word' )[0].firstChild.data
    meanings = cards.getElementsByTagName( 'meanings' )[0].getElementsByTagName( 'meaning' )[0]

    text_transcription = ''
    try:
        text_transcription = meanings.attributes[ 'transcription' ].value
    except KeyError:
        text_transcription = ''

    translations = meanings.getElementsByTagName( 'translations' )[0]

    text_translations = []

    for words in translations.getElementsByTagName( 'word' ):
        text_translations.append( words.firstChild.data )

    text_example = ''
    if len( meanings.getElementsByTagName( 'examples' ) ) > 0:
        text_example = meanings.getElementsByTagName( 'examples' )[0].getElementsByTagName( 'example' )[0].firstChild.data

    s = '\t'.join( [ text_word, ', '.join( text_translations ), text_transcription, text_example  ] )

    f.write( s.replace( u';', u',' ) )
    f.write( u'\n' )

f.close()
