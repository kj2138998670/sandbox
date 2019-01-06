"""(Incomplete) Tests for Song class."""
from song import Song

def run_tests():
# test empty song (defaults)
    song = Song()
    print(song)
    assert song.artist == ""
    assert song.title == ""
    assert song.year == 0
    assert song.is_required

# test initial-value song
    song2 = Song("Amazing Grace", "John Newton", 1779, True)
    print(song2)
    assert song2.is_required

# test mark_learned()
    song2.mark_learned()
    print(song2)
    assert not song2.is_required

run_tests()