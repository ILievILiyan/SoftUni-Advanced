def add_songs(*args):
    songs_dict = {}

    for song, lyrics in args:
        if song not in songs_dict.keys():
            songs_dict[song] = []
        for line in lyrics:
            songs_dict[song].append(line)

    output_list = []

    for song, lyrics in songs_dict.items():
        output_list.append(f'- {song}')
        if lyrics:
            for lyric in lyrics:
                output_list.append(lyric)
    return "\n".join(output_list)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
