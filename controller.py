from os import system
import sketchbook as sb
import view


def main_loop():
    system("cls")
    sb.s_book=view.read_file()  
    flag=1
    while flag:
        view.main_menu()
        s=view.cmd_input()
        if s=='1':
            view.notes_to_screen(sb.s_book)          
        elif s=='2':
            note_show()  
        elif s=='3':
            note_last()      
        elif s=='4':
            head = view.head_input()
            text = view.text_input()
            sb.note_add(head,text)  
        elif s=='5':
            note_edit()
        elif s=='6':  
            note_delete()
        elif s=='7':  
            view.out_file(sb.s_book)
        elif s=='0':  
            flag=0
            break
        s=input('Нажмите Enter чтобы продолжить')
        system("cls")
        
 
         
def note_edit():
    note=id_input_and_check()
    if (note != False):
        text=view.text_input()
        sb.note_replace(text)
    

def note_delete():
    note=id_input_and_check()
    if (note != False):
        sb.note_remove()
    
def note_show():
    note=id_input_and_check()
    if (note != False):
        view.note_to_screen(note)
    
    
def id_input_and_check():
    view.notes_to_screen(sb.s_book)
    id = view.id_input()
    if id.isdigit():  # проверка на число
        note = sb.get_note_by_id(int(id))
        if note == "none":
            view.wrong_id()
            return False
        else:  
            return note
    else:
        view.wrong_input() 
        return False  
    
def note_last():
    note=sb.get_last_note()
    if (note != False):
        view.note_to_screen(note)
    else:
        view.notes_empty()
        