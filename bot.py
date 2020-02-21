import time
from pyrogram import Client
import pyrogram.errors 
from random import randint

app = Client("my_account",
              api_id=1234567,
              api_hash="1a234bc56d78e901g12fx899ad5eq42"
              )

msg = '''advertise'''

app.start()

targets_file = open('targets.txt', 'r').readlines()
targets = [target for target in targets_file]
for target_user in targets:
    import pyrogram

    try:
        app.send_message(target_user, msg)
        time.sleep(randint(2, 6))
    except pyrogram.errors.bad_request_400.PeerFlood as e:
        print(e)
        pass
    except pyrogram.errors.bad_request_400.UsernameNotOccupied as e:
        print(e)
        pass
    except:
        pass

app.stop()
