# Script Imports
import es
import playerlib
import gamethread

# Script Information
info = es.AddonInfo() 
info.name     = "IrishPirates Training Server" 
info.version  = "0.1" 
info.url      = "http://www.irishpirates.org" 
info.basename = "ip_trainingserver" 
info.author   = "Gues7"

# Script CVar's
ip_trainingserver           = es.ServerVar(info.name, info.version, info.url).makepublic()
ip_trainingserver_enable    = es.ServerVar("ip_trainingserver_enable", 1, "Enable / Disable the training script")

# Script Config Var's
training_money              = 16000     # Players starting money each round
training_report_damage      = 1         # Report damage dealt per hit (1=on, 0=off)
training_advertise          = 1         # Display in game advertisements (1=on, 0=off)
training_advert_timer       = 20        # Time between advertisements

def load():
    if ip_trainingserver_enable > 0:
        if training_advertise > 0:
            global advertisements
            advertisements = []
            AddonPath = es.getAddonPath('ip_trainingserver')
            advertisement_file = open(AddonPath+'/advertisements.txt')
            for adline in advertisement_file:
                advertisements.append(adline.replace('\n', ''))
            advertisement_file.close
            advertisement()
        es.msg("#multi", "#lightgreen[#greenIP#lightgreen]#default Server now in training mode")

def unload():
    if training_advertise > 0:
        gamethread.cancelDelayed("advertisements")
    es.msg("#multi", "#lightgreen[#greenIP#lightgreen]#default Server no longer in training mode")
        
def player_spawn(ev):
    if ip_trainingserver_enable > 0:
        player = playerlib.getPlayer(ev['userid'])
        player.set("cash", training_money)
        
def player_hurt(ev):
    if ip_trainingserver_enable > 0:
        
        victim   = playerlib.getPlayer(ev['userid'])
        attacker = playerlib.getPlayer(ev['attacker'])
        
        if training_report_damage > 0:
            es.centertell(ev['attacker'], "Hurt %s for %s " % (victim.name, ev['dmg_health']))
            
def advertisement(index=0):
    if training_advertise > 0 and ip_trainingserver_enable > 0:
        if len(advertisements):
            es.msg("#multi", advertisements[index])
        index += 1
        
        if index >= len(advertisements):
            index = 0
            
        gamethread.delayedname(training_advert_timer, "advertisements", advertisement, index)