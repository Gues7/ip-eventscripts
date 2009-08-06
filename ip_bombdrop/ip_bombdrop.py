'''

'''

import es
import playerlib
import gamethread

info = es.AddonInfo() 
info.name     = "IrishPirates AFK bomb drop" 
info.version  = "0.1" 
info.url      = "http://www.irishpirates.org" 
info.basename = "ip_bombdrop" 
info.author   = "Gues7 & Ajurna"

ip_bombdrop   = es.ServerVar(info.name, info.version, info.url).makepublic()
afktime       = 7

def load():
        es.msg("#multi","#green[#lightgreenAFK Bomb Drop#green]#default Has loaded successfully")
        
def unload():
        es.msg("#multi","#green[#lightgreenAFK Bomb Drop#green]#default Has unloaded successfully")
        
def player_spawn(ev):
    myPlayer = playerlib.getPlayer(int(ev["userid"]))
    if myPlayer.hasC4():
        gamethread.delayed(1, initcheck, (ev["userid"],))

def initcheck(userid):
    myPlayer = playerlib.getPlayer(userid)
    gamethread.delayed(afktime, c4check, (userid, myPlayer.x,))

def c4check(userid, location):
    myPlayer = playerlib.getPlayer(int(userid))
    if myPlayer.hasC4():
        if myPlayer.x == location:
            es.sexec(userid, "use weapon_c4")
            es.sexec(userid, "drop")