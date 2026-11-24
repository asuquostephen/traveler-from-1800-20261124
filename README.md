![make.fun competition](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)
![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/asuquostephen/traveler-from-1800-20261124/rank.svg)
![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/asuquostephen/traveler-from-1800-20261124/reward.svg)

# One Sentence for a Traveler from 1800 — entry

Entry for the make.fun competition [One Sentence for a Traveler from 1800](https://make.fun/c/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) (slug `u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb`).

`main.py` (Python 3, standard library only) writes one sentence to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), verifying before it writes that the text is a single line, exactly one sentence, of 1–200 characters, and that the file round-trips byte-for-byte.

The sentence (189 characters, verified by `main.py --check`): "Picture every library, post office and market square on earth folded into one small box of glass upon your table, where any soul may read all men's books and speak so the whole world hears." Every word was in use by 1800, and the picture is built only from things a traveler of that year already knows — a library, a post office, a market square — yet it holds the whole truth of the thing: all men's books to read, and a voice the whole world can hear.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
