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

#open file and read all lines
with open('Spell_Fragments.txt', 'r') as f:
    toot = f.readlines()

#select random line
toot = random.choice(toot)

#toot random selection 
mastodon.status_post(toot)

