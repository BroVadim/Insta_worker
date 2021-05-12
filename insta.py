import subprocess
import instaloader

class Instagram:
    def __init__(self,user,password):
        self.L  = instaloader.Instaloader()
        self.L.login(user, password)
        self.L.interactive_login(user)
        self.create_session(user)
        self.L.load_session_from_file(user)
    
    def create_session(self,user):
        subprocess.call(["instaloader", "-l", user])

    def search_posts_by_tag(self, tag):
        for post in instaloader.Hashtag.from_name(self.L.context, tag).get_posts():
            self.L.download_post(post, target='#{}'.format(tag))

if __name__=="__main__":
    user_login = 'your_login'
    user_password = 'your_password'
    inst = Instagram(user_login,user_password)
    inst.search_posts_by_tag("денежнаялотерея")