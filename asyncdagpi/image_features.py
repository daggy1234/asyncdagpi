class ImageFeatures:
    """
    Base ImageFatures that asyncdagpi has
    """

    def __init__(self, value: str, description: str):
        self.value = value
        self.description = description

    def __str__(self) -> str:
        """
        Get a string of the feature
        :return: :class:`string`
        """
        return self.value.replace("/", "")

    def __repr__(self) -> str:
        """
        get a string describing the object
        :return: :class:`str`
        """
        return "<asyncdagpi.ImageFeature feature={} >".format(
            self.value.replace("/", ""))

    @classmethod
    def pixel(cls):
        """
        Pixelate an Image
        """
        return cls("/pixel/", "Pixelate an Image")

    @classmethod
    def colors(cls):
        """
        Analyse and get an Image's Color Top 5 Colors
        """
        return cls("/colors/", "Analyse and get an Image's Color Top 5 Colors")

    @classmethod
    def wanted(cls):
        """
        Get a wanted poster of an Image.
        """
        return cls("/wanted/", "Get a wanted poster of an Image")

    @classmethod
    def triggered(cls):
        """
        Get a triggered Image gif
        """
        return cls("/triggered/", "Get a triggered Image gif")

    @classmethod
    def america(cls):
        """
        The waving american flag on an image.gif
        """
        return cls("/america/", "The waving american flag on an image.gif")

    @classmethod
    def communism(cls):
        """
        Glory of the soviet Union on an image.gif
        """
        return cls("/communism/", "Glory of the soviet Union on an image.gif")

    @classmethod
    def wasted(cls):
        """
        GTA V Wasted screen.
        """
        return cls("/wasted/", "GTA V Wasted screen")

    @classmethod
    def five_guys_one_girl(cls):
        """
        No I have never heard of this meme. Takes in 2 Image URL.
        Needs:
            - url
            - url2
        """
        return cls("/5g1g/",
                   "No I have never heard of this meme. Takes in 2 Image URL")

    @classmethod
    def why_are_you_gay(cls):
        """
        The infamous Why are you gay. Takes in 2 Image URL.
        Needs:
            - url
            - url2
        """
        return cls("/whyareyougay/",
                   "The infamous  Why are you gay. Takes in 2 Image URL")

    @classmethod
    def invert(cls):
        """
        Invert an Image.
        """
        return cls("/invert/", "Invert an Image")

    @classmethod
    def sobel(cls):
        """
        Cool SOBEL filter for Images. Only png's.
        """
        return cls("/sobel/", "Cool SOBEL filter for Images.")

    @classmethod
    def triangle(cls):
        """
        Cool triangle edge detection for Images. Only png's.
        """
        return cls("/triangle/", "Cool triangle edge detection for Images.")

    @classmethod
    def hog(cls):
        """
        Histogram of Oriented Gradients.
        """
        return cls("/hog/", "Histogram of Oriented Gradients")

    @classmethod
    def blur(cls):
        """
        Blurs an entire Image.
        """
        return cls("/blur/", "Blurs an entire Image")

    @classmethod
    def rgb(cls):
        """
        Get RGB information from an image.
        """
        return cls("/rgb/", "Get RGB information from an image")

    @classmethod
    def angel(cls):
        """
        Make an Image Angelic.
        """
        return cls("/angel/", "Make an Image angelic")

    @classmethod
    def satan(cls):
        """
        Make an Image the devil.
        """
        return cls("/satan/", "Make an Image the devil")

    @classmethod
    def hitler(cls):
        """
        Make an Image as bad as hitler.
        """
        return cls("/hitler/", "Make an Image as bad as hitler")

    @classmethod
    def obama(cls):
        """
        The obama meme of someone awarding themselves.
        """
        return cls("/obama/", "The obama meme of someone awarding themselves")

    @classmethod
    def bad(cls):
        """
        This image is bad.
        """
        return cls("/bad/", "This image is bad")

    @classmethod
    def sith(cls):
        """
        Laughs in Sithlord
        """
        return cls("/sith/", "Laughs in Sithlord")

    @classmethod
    def jail(cls):
        """
        Put an Image behind bars.
        """
        return cls("/jail/", "Put an Image behind bars")

    @classmethod
    def fedora(cls):
        """
        Tips. Fedora
        """
        return cls("/fedora/", "Tips fedora")

    @classmethod
    def delete(cls):
        """
        Delete some trash
        """
        return cls("/delete/", "Delete some trash")

    @classmethod
    def shatter(cls):
        """
        Broken like glass
        """
        return cls("/shatter/", "Broken like glass")

    @classmethod
    def gay(cls):
        """
        represent! Pastes a pride flag on an image.
        """
        return cls("/gay/", "represent! Pastes a pride flag on an image")

    @classmethod
    def pride(cls):
        """
        Wraps Image and Text into a thought
        Needs:
            - text
            - flag (one of these flags):
                * asexual

                * bisexual

                * gay

                * genderfluid

                * genderqueer

                * intersex

                * lesbian

                * nonbinary

                * progress

                * pan

                * trans
        """
        return cls("/thoughtimage/", "Wraps Image and Text into a thought")

    @classmethod
    def trash(cls):
        """
        Makes an Image trash.
        """
        return cls("/trash/", "Makes an Image trash")

    @classmethod
    def deepfry(cls):
        """
        Deepfries an Image.
        """
        return cls("/deepfry/", "Deepfries an Image")

    @classmethod
    def ascii(cls):
        """
        Turns an Image into a ascii-fied image.
        """
        return cls("/ascii/", "Turns an Image into a ascii-fied image")

    @classmethod
    def charcoal(cls):
        """
        Turns an Image into a charcoal sketch.
        """
        return cls("/charcoal/", "Turns an Image into a charcoal sketch")

    @classmethod
    def poster(cls):
        """
        Posterizes an image.
        """
        return cls("/poster/", "Posterizes an image")

    @classmethod
    def sepia(cls):
        """
        Makes an image sepia tone.
        """
        return cls("/sepia/", "Makes an image sepia tone")

    @classmethod
    def polaroid(cls):
        """
        Frames an Image like a printed polaroid.
        """
        return cls("/polaroid/", "Frames an Image like a printed polaroid")

    @classmethod
    def swirl(cls):
        """
        Swirls the center of Image.
        """
        return cls("/swirl/", "Swirls the center of Image")

    @classmethod
    def paint(cls):
        """
        Turns an Image into an oil painting.
        """
        return cls("/paint/", "Turns an Image into an oil painting")

    @classmethod
    def night(cls):
        """
        Turns day into night on an Image.
        """
        return cls("/night/", "Turns day into night on an Image")

    @classmethod
    def magik(cls):
        """
        Magik an Image
        """
        return cls("/magik/", "Magik an Image")

    @classmethod
    def stringify(cls):
        """
        Stringify an Image
        """
        return cls("/stringify/", "Stringify an Image")

    @classmethod
    def rainbow(cls):
        """
        Rainbow light effect on image
        """
        return cls("/rainbow/", "Rainbow light effect on image")

    @classmethod
    def solar(cls):
        """
        Solarizes an Image.
        """
        return cls("/solar/", "Solarizes an Image")

    @classmethod
    def captcha(cls):
        """
        Creates a realistic Captcha
        Needs:
            - text
            - image
        """
        return cls("/captcha/", "Creates a realistic Captcha")

    @classmethod
    def thought_image(cls):
        """
        Wraps Image and Text into a thought
        Needs:
            - text
            - image
        """
        return cls("/thoughtimage/", "Wraps Image and Text into a thought")

    @classmethod
    def tweet(cls):
        """
        Generates an accurate fake tweet
        Needs:
            - text
            - image
            - username
        """
        return cls("/tweet/", "Generates an accurate fake tweet")

    @classmethod
    def discord(cls):
        """
        Generated a realistic Discord Message
        Needs:
            - text
            - image
            - quote
            - dark (boolean) default is true
        """
        return cls("/discord/", "Generated a realistic Discord Message")

    @classmethod
    def youtube(cls):
        """
        Generated a realistic Yutube comment
        Needs:
            - text
            - image
            - quote
            - dark (boolean) default is true
        """
        return cls("/yt/", "Generated a realistic Yutube comment")

    @classmethod
    def retro_meme(cls):
        """
        old 2012 advice animals style meme
        Needs:
            - top_text
            - bottom_text
            - image
        """
        return cls("/retromeme/", "Generated a realistic Discord Message")

    @classmethod
    def motiv(cls):
        """
        old 2012 style Motiv memes
        Needs:
            - top_text
            - bottom_text
            - image
        """
        return cls("/motiv/", "old 2012 style Motiv memes")

    @classmethod
    def modern_meme(cls):
        """
        Mordern meme with text scaling
        Needs:
            - text
            - image
        """
        return cls("/modernmeme/", "Modern New meme style meme")
