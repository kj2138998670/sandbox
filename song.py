class Song:
    # Create song constructor #
    def __init__(self,title="",artist="",year=0,is_required=""):
        self.title= title
        self.artist= artist
        self.year=year
        self.is_required=is_required

    def __str__(self):
        if self.is_required == "n":
            is_required = "learned"
            return "You have learned {} by {} ({})".format(self.title,self.artist,is_required)
        else:
            is_required="not learned"
            return "You have not learned {} by {} ({})".format(self.title, self.artist,is_required)

    def mark_learned(self):
        self.is_required = "n"
        return self.is_required