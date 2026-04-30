ART = """\
              ,   ,-',
        ,', ,'  ','  ,'   ÅÑGË£ÏÇÄ †(–)Ë ßRÄ†
      '-',  '      ,'
          ' -,    ',
              ' -, ',                                         , - - -,
             ('''''' ®'''''''')                        ,,,,,    ,-' -,''''''''',
              ` ~„''`„~ '                          ',  ,', -' , -,'' ''''''''',
                  "„  " - „                   „ - ",®,-'     `~~' '''''''
                 „"         " „         „ - "      ,',,,',
               „-" " " " " " " ~~~~~~" - „       ,'
            „" –,'' ~ ,       • ; •          "      "„
            \"\"\"\";      ' - , ,  ; , , , - '' ' ' -,_ ', ',
           , -' ' ',           ,'    ,'             ',~', ',
         ,'         ' - , ,()' /\\    ',          (),'¯ ,'   `¸`;
         ',                            ` ` ` ` ` `      ,-,,,-'
           '-,                                  ,¬  ,-'
              ' -, ~            ~~~~~~' ' ` ,-'
                  `~-,,,,,,,      ,,,,,,,,,,-~'
      ('('('(,,,              ;    ;                •Å(V)åö•
       '-, '-,'''      ,-';`,`'ˆˆˆˆˆ ,' ;' ' -,           •97•
         ;¯ ;      ;  ;  ', ; ; ,'  ;  ‚¸  ' -,        •••
         ;   ;     ;       '''''''''''    ``'-,',  ,'
         ;   ;, -¬;    O   O   O  O   '-',,,,,,,,,,,,
         ;        ;  O   O     O O    O  ,'     O     ,'
          ' - - ' `;    O        O  O    O   O    ,'
               ,-'   O    O    O  O      O    O   ,'
            ,-' O O  O   O        O        O ,'
         ,-'   O      O   O   O     O  O     ,'
      ,-'  O    O    O  O   O   O O O   O,-'-,
       ``¬ -,,,,,,,-¬~,~~~~~~~~~--',)  (' -,
                    ',   (',                     ' -,    '-,
                     ',)  (',                        `-,)  ' -,
                      ',    ',                           `-,  ,',-----,
                       ',)   ;                              `\\,- ---'
                   ¸,,,,'‡  (;
                  (¸,,,,,';_'\\ ßy §(V)òó†(–)775 ™
"""

FORBIDDEN = set("'`,-")


def find_pupils_row(lines):
    for y, line in enumerate(lines):
        if "•" in line and line.count("•") == 2:
            return y
    raise ValueError("Pupils row not found")


def count_pupil_chars(line):
    return sum(1 for ch in line if ch not in FORBIDDEN and not ch.isspace())


def find_lips_row(pupils_y):
    return pupils_y + 1


def lips_range(line):
    indices = [i for i, ch in enumerate(line) if ch not in FORBIDDEN and not ch.isspace()]
    return indices[0], indices[-1]


def compute_polkadot_score(art):
    lines = art.split("\n")

    pupils_y = find_pupils_row(lines)
    pupils_line = lines[pupils_y]

    pupil_chars = pupils_line.count("•")

    lips_y = find_lips_row(pupils_y)
    lips_start_x, lips_end_x = lips_range(lines[lips_y])

    polkadot_xs = [x for y, line in enumerate(lines) for x, ch in enumerate(line) if ch == "O"]

    inside = sum(1 for x in polkadot_xs if lips_start_x <= x <= lips_end_x)
    outside = len(polkadot_xs) - inside
    score = outside + inside * pupil_chars

    return {
        "pupils_y": pupils_y,
        "pupils_line": pupils_line,
        "pupil_chars": pupil_chars,
        "lips_y": lips_y,
        "lips_line": lines[lips_y],
        "lips_start_x": lips_start_x,
        "lips_end_x": lips_end_x,
        "total_polkadots": len(polkadot_xs),
        "inside": inside,
        "outside": outside,
        "score": score,
    }


if __name__ == "__main__":
    result = compute_polkadot_score(ART)
    print(f"pupils row y         : {result['pupils_y']}")
    print(f"pupils line          : {result['pupils_line']!r}")
    print(f"pupil char count     : {result['pupil_chars']}")
    print(f"lips row y           : {result['lips_y']}")
    print(f"lips line            : {result['lips_line']!r}")
    print(f"lips x range         : [{result['lips_start_x']}, {result['lips_end_x']}]")
    print(f"total polkadots (O)  : {result['total_polkadots']}")
    print(f"  inside lips range  : {result['inside']}")
    print(f"  outside lips range : {result['outside']}")
    print(f"FINAL SCORE          : {result['score']}")
