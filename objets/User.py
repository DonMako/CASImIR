class User:
    """
    :param str id: Identifiant of the user
    :param str platform: Where the user posted the images
    :param list images: List of images the user posted
    """

    def __init__(self, id: str, platform: str, images: list):
        self.id = id
        self.platform = platform
        self.images = images