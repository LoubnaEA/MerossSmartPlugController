# Easily control your Meross Smart Plug using this Python script ! 

import asyncio
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

EMAIL = 'youremail@xxx.com'
PASSWORD = 'YourPassword'

async def main():
    # Créer un client HTTP Meross
    http_api_client = await MerossHttpClient.async_from_user_password(
    api_base_url='https://iotx-eu.meross.com',
    email=EMAIL,
    password=PASSWORD
    )

    # Créer un gestionnaire Meross avec le client HTTP
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Découverte des appareils
    await manager.async_device_discovery()

    # Recherche du smart plug 
    # MSS310 (Smart plug with power consumption)
    smart_plugs = manager.find_devices(device_type="mss310")

# Vérifier s'il y a des smart plugs trouvés
    # Allumer toutes les prises intelligentes trouvées
    if len(smart_plugs) == 0:
        print("Aucune prise intelligente trouvée.")
    else:
        for smart_plug in smart_plugs:
        print(f"Allumage de la prise intelligente {smart_plug.name}")
        await smart_plug.async_turn_on()    #TURN ON
        
        await asyncio.sleep(1)
        
        print(f"Fermer de la prise intelligente {smart_plug.name}")
        await smart_plug.async_turn_off()   #TURN OFF

        await asyncio.sleep(1)
            
    # Fermer le gestionnaire et se déconnecter du client HTTP
    manager.close()
    await http_api_client.async_logout()

# Exécuter la fonction main dans un événement loop asyncio
if __name__ == '__main__':
    asyncio.run(main())
