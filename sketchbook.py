import view
import time

s_book=[]
note_index=0


def get_note_by_id(id):
    global s_book
    global note_index
    note_index=0
    for note in s_book:
        if int(note[0]) == id:
            return note
        note_index += 1
    return "none"


def note_add(head, text):
    global s_book
    note = (get_max_id() + 1, round(time.time()), round(time.time()), head, text)
    s_book.append(note)


def note_replace(text):
    global s_book
    global note_index
    note =  s_book.pop(note_index)
    new_note = (note[0], round(time.time()), note[2], note[3], text )
    s_book.insert(note_index, new_note)
    
def note_remove():
    global s_book
    global note_index
    s_book.pop(note_index)


def get_max_id():
    global s_book
    max_id = 0
    if len(s_book)==0:
        return max_id
    else:
        for note in s_book:
            if max_id < int(note[0]):
                max_id = int(note[0])  
        return max_id
    
def get_last_note():
    global s_book
    last_date = 0
    if len(s_book)==0:
        return False
    else:
        for note in s_book:
            if last_date < int(note[1]):
                last_date = int(note[1]) 
                last_note = note
        return last_note
