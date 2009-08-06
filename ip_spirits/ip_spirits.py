import es
import playerlib

info = es.AddonInfo() 
info.name     = "IrishPirates Spirits" 
info.version  = "0.1" 
info.url      = "http://www.irishpirates.org" 
info.basename = "ip_spirits" 
info.author   = "Gues7"

ip_spirits   = es.ServerVar(info.name, info.version, info.url).makepublic()

def load():
    es.msg("#multi", "#lightgreen[#greenSpirits#lightgreen]#default has loaded successfully")

def unload():
    es.msg("#multi", "#lightgreen[#greenSpirits#lightgreen]#default has unloaded successfully")

def round_start(ev):
    startLoop
    
def startLoop():
    deadPlayerList = playerlib.getPlayerList('#dead')
    for deadPlayer in deadPlayerList:
        drawGhost(deadPlayer)
        es.delayed(0.2, 'es_xdoblock ip_spirits/startLoop')
            
def drawGhost(arg1):
    es.serverCmd("es est_effect 11 #a 0 sprites/light_glow02.vmt server_var(%s) server_var(%s) server_var(%s) .2 .2 150" % (arg1.x, arg1.y, arg1.z))