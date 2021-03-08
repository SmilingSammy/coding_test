# 베스트 앨범 (Lv3)
def solutions(genres, plays):
    album_dict = {}
    album_sum_dict = {}
    idx = 0
    for g, p in zip(genres, plays):
        if g not in album_dict:
            album_dict[g] = []
            album_sum_dict[g] = 0
        album_dict[g].append((p, idx))
        album_sum_dict[g] += p
        idx += 1
    key_sort = sorted(album_sum_dict.keys(), key=lambda x: album_sum_dict[x], reverse=True)
    result = []
    for key in key_sort:
        val_sort = sorted(album_dict[key], key=lambda x: x[0], reverse=True)
        result += [elem[1] for elem in val_sort][:2]
    return result