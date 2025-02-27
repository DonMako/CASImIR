class Image():
    """
    :param str url: URL of the image (where it was originally found)
    :param str name: Name under which the image is locally stored
    :param int score: Score of confident the model has for the image to represent a child
    """

    def __init__(self, url: str, score: int):
        self.url = url
        self.name = self.url.split('/')[-1]
        self.score = score