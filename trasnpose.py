guitar_tabe = "e|------------------------7-8-----8-7-----7----7-8--------7-7-----------------7---|"
guitar_tabb = "B|--------------7-8---7-8-----8-------8------10----7-8--10-----10-8-10---8-10---10|"
guitar_tabg = "G|----------7-9-----9-----------9-------7------------------------------9----------|"
guitar_tabd = "D|---7-9-10-----------------------------------------------------------------------|" 
guitar_taba = "A|10------------------------------------------------------------------------------|" 
guitar_tabE = "E|--------------------------------------------------------------------------------|"

transpose_by = 2

def transpose(guitar_tab, transpose_by):
    guitar_tabe = guitar_tabe.replace("e", "").replace("|", "").replace("-", " ")
    guitar_tabb = guitar_tabb.replace("B", "").replace("|", "").replace("-", " ")
    guitar_tabg = guitar_tabg.replace("G", "").replace("|", "").replace("-", " ")
    guitar_tabd = guitar_tabd.replace("D", "").replace("|", "").replace("-", " ")
    guitar_taba = guitar_taba.replace("A", "").replace("|", "").replace("-", " ")
    guitar_tabE = guitar_tabE.replace("E", "").replace("|", "").replace("-", " ")

    


