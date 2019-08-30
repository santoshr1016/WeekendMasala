def playlist(songs, k, q):
    size = len(songs)
    song_at_k = songs[k]

    songs.extend(songs)

    des_song_idx = songs.index(q)
    dist1 = des_song_idx - k
    dest_song_idx = songs.index(song_at_k, size, len(songs))
    dist2 = dest_song_idx - des_song_idx

    res = dist1 if dist1 < dist2 else dist2
    print(res)


# Write your code here



if __name__ == '__main__':

    songs_count = int(input().strip())

    songs = []

    for _ in range(songs_count):
        songs_item = input()
        songs.append(songs_item)

    k = int(input().strip())

    q = input()

    result = playlist(songs, k, q)

