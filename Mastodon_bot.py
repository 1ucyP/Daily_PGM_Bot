#import relevant libraries
import mastodon
import random
from time import sleep
from mastodon import Mastodon

#credentials
mastodon = Mastodon(
    access_token = 'token_masto.secret',
    api_base_url = 'https://archaeo.social/'
)

def send_toot(text):
    with open(text, 'r', encoding='UTF-8') as file:
        line = file.readlines()
        for x in text:
            mastodon.status_post(random.choice(line))
            sleep(86400)
            
def main():
    mastodon.status_post(send_toot('Spell_Fragments.txt'))

if __name__ == "__main__":
    main()
    

