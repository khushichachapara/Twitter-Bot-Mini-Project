import tweepy




api_key="4GMAx9jRS3UeAKAZ1SgkD"
api_secret="Xd9ezbzJW8bY73okQCXfXtZVUzqxD2EjDpnctNsrPlXJ"
bearer_token=r"AAAAAAAAAAAAAAAAAAAAAKnRswEAAAAAXu356Z%2BYRfvKnRH0wm9ERpg%3DiOTutWdybvbOlavGRoiyUT4wsmdIPoaPO2KcaRTDG9Xdj35jTD"
access_token="1771409454363475968-8Ooowjo7CRboVgIocEPiarmutx"
access_token_secret="H6i48TOFBjsZIyv4GTUO05IQo97jKsesx6Cej4Xn"


client_secret="kpuMppB5FzxtM85eUjbhNf6ElSGWpSzBf7XM87Bl_-58dlWgON"
client_id="TG9nU1BrTFdtUVRyOVljS3NDZ206MTpjaQ"




client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

#client.create_tweet(text = "hello this is me")

#client.create_tweet(text = "khushi chachapara")

'''api.destroy_status(1771801222577586201)
try:
    api.get_status(1771801222577586201)
except:
    print('this status has been successfully deleted.')'''
    
api.update_profile(description='python')

'''user_id = "narendramodi"
create_friendship(api, user_id)'''

'''filename='4215.jpg'
api.update_profile_image(filename)'''

'''filename='9686.jpg'
api.update_profile_banner(filename)'''


# client.create_tweet(text = "khushi chachapara")


#api.destroy_status(1772536647973790174)

'''try:
    api.verify_credentials()
    print("Authentication successful")
except Exception as e:
    print("Error during authentication:", e)
    
    api.verify_credentials()'''
    
def create_friendship(api, username='narendramodi'):
    try:
        api.create_friendship(username)
        print(f"Friendship created with {username}!")
    except tweepy.error.TweepError as e:
        print(f"Error creating friendship with {username}: {e}")



