import genanki

def generate_anki(keywords, descriptions, title):
    anki_model = genanki.Model(
        1607392319,
    'Simple Model',
    fields=[
        {'name': 'Keywords'},
        {'name': 'Description'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': '{{Keywords}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Description}}',
        },
    ]
    )
    my_deck = genanki.Deck(2059400112,title)
    for i in range(len(keywords)):
        my_note = genanki.Note(
            model=anki_model,
            fields=[keywords[i], descriptions[i]]
        )
        my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file(f"{title}.apkg")