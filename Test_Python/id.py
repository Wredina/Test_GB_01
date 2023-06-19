def new_id(note):
    id_count = 1
    for id in note:
        if id['id'] == id_count:
            id_count += 1
    return id_count
