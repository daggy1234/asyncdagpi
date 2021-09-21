from typing import Type, TypeVar, Optional

IF = TypeVar('IF', bound='ImageFeatures')


class ImageFeatures:

    """
    Base ImageFatures that asyncdagpi has
    """

    def __init__(self, value: str, description: str):
        """
        Initialise the dagpi Image feature
        """
        self.value: str = value
        self.description: str = description

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
        return f"<asyncdagpi.ImageFeature feature={self.value.replace('/', '')} >"

    @classmethod
    def from_path(cls: Type[IF], path: str) -> IF:
        """
        Construct an Image Feature from it's path.
        """
        return cls(path, "")

    @classmethod
    def mirror(cls: Type[IF]) -> IF:
        """
        Flip image horizontally (left to right).
        """
        return cls("/mirror/", "Flip image horizontally (left to right).")

    @classmethod
    def flip(cls: Type[IF]) -> IF:
        """
        Flip the image vertically (top to bottom).
        """
        return cls("/flip/", "Flip the image vertically (top to bottom).")

    @classmethod
    def pixel(cls: Type[IF]) -> IF:
        """
        Pixelate an Image
        """
        return cls("/pixel/", "Pixelate an Image")

    @classmethod
    def colors(cls: Type[IF]) -> IF:
        """
        Analyse and get an Image's Color Top 5 Colors
        """
        return cls("/colors/", "Analyse and get an Image's Color Top 5 Colors")

    @classmethod
    def wanted(cls: Type[IF]) -> IF:
        """
        Get a wanted poster of an Image.
        """
        return cls("/wanted/", "Get a wanted poster of an Image")

    @classmethod
    def triggered(cls: Type[IF]) -> IF:
        """
        Get a triggered Image gif
        """
        return cls("/triggered/", "Get a triggered Image gif")

    @classmethod
    def america(cls: Type[IF]) -> IF:
        """
        The waving american flag on an image.gif
        """
        return cls("/america/", "The waving american flag on an image.gif")

    @classmethod
    def communism(cls: Type[IF]) -> IF:
        """
        Glory of the soviet Union on an image.gif
        """
        return cls("/communism/", "Glory of the soviet Union on an image.gif")

    @classmethod
    def bomb(cls: Type[IF]) -> IF:
        """
        Kaboom
        """
        return cls("/bomb/", "Kaboom")

    @classmethod
    def wasted(cls: Type[IF]) -> IF:
        """
        GTA V Wasted screen.
        """
        return cls("/wasted/", "GTA V Wasted screen")

    @classmethod
    def five_guys_one_girl(cls: Type[IF]) -> IF:
        """
        No I have never heard of this meme. Takes in 2 Image URL.
        Needs:
            - url
            - url2
        """
        return cls("/5g1g/",
                   "No I have never heard of this meme. Takes in 2 Image URL")

    @classmethod
    def slap(cls: Type[IF]) -> IF:
        """
        Have someone slap someone.
        Needs:
            - url
            - url2
        """
        return cls("/slap/",
                   "Have someone slap someone.")

    @classmethod
    def why_are_you_gay(cls: Type[IF]) -> IF:
        """
        The infamous Why are you gay. Takes in 2 Image URL.
        Needs:
            - url
            - url2
        """
        return cls("/whyareyougay/",
                   "The infamous  Why are you gay. Takes in 2 Image URL")

    @classmethod
    def invert(cls: Type[IF]) -> IF:
        """
        Invert an Image.
        """
        return cls("/invert/", "Invert an Image")

    @classmethod
    def sobel(cls: Type[IF]) -> IF:
        """
        Cool SOBEL filter for Images. Only png's.
        """
        return cls("/sobel/", "Cool SOBEL filter for Images.")

    @classmethod
    def triangle(cls: Type[IF]) -> IF:
        """
        Cool triangle edge detection for Images. Only png's.
        """
        return cls("/triangle/", "Cool triangle edge detection for Images.")

    @classmethod
    def hog(cls: Type[IF]) -> IF:
        """
        Histogram of Oriented Gradients.
        """
        return cls("/hog/", "Histogram of Oriented Gradients")

    @classmethod
    def blur(cls: Type[IF]) -> IF:
        """
        Blurs an entire Image.
        """
        return cls("/blur/", "Blurs an entire Image")

    @classmethod
    def rgb(cls: Type[IF]) -> IF:
        """
        Get RGB information from an image.
        """
        return cls("/rgb/", "Get RGB information from an image")

    @classmethod
    def angel(cls: Type[IF]) -> IF:
        """
        Make an Image Angelic.
        """
        return cls("/angel/", "Make an Image angelic")

    @classmethod
    def satan(cls: Type[IF]) -> IF:
        """
        Make an Image the devil.
        """
        return cls("/satan/", "Make an Image the devil")

    @classmethod
    def hitler(cls: Type[IF]) -> IF:
        """
        Make an Image as bad as hitler.
        """
        return cls("/hitler/", "Make an Image as bad as hitler")

    @classmethod
    def obama(cls: Type[IF]) -> IF:
        """
        The obama meme of someone awarding themselves.
        """
        return cls("/obama/", "The obama meme of someone awarding themselves")

    @classmethod
    def bad(cls: Type[IF]) -> IF:
        """
        This image is bad.
        """
        return cls("/bad/", "This image is bad")

    @classmethod
    def sith(cls: Type[IF]) -> IF:
        """
        Laughs in Sithlord
        """
        return cls("/sith/", "Laughs in Sithlord")

    @classmethod
    def jail(cls: Type[IF]) -> IF:
        """
        Put an Image behind bars.
        """
        return cls("/jail/", "Put an Image behind bars")

    @classmethod
    def fedora(cls: Type[IF]) -> IF:
        """
        Tips. Fedora
        """
        return cls("/fedora/", "Tips fedora")

    @classmethod
    def delete(cls: Type[IF]) -> IF:
        """
        Delete some trash
        """
        return cls("/delete/", "Delete some trash")

    @classmethod
    def shatter(cls: Type[IF]) -> IF:
        """
        Broken like glass
        """
        return cls("/shatter/", "Broken like glass")

    @classmethod
    def gay(cls: Type[IF]) -> IF:
        """
        represent! Pastes a pride flag on an image.
        """
        return cls("/gay/", "represent! Pastes a pride flag on an image")

    @classmethod
    def pride(cls: Type[IF]) -> IF:
        """
        Pride flag overlay
        Needs:
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

                * agender

                * ally

                * polysexual
        """
        return cls("/pride/", "Pride flag overlay")

    @classmethod
    def trash(cls: Type[IF]) -> IF:
        """
        Makes an Image trash.
        """
        return cls("/trash/", "Makes an Image trash")

    @classmethod
    def deepfry(cls: Type[IF]) -> IF:
        """
        Deepfries an Image.
        """
        return cls("/deepfry/", "Deepfries an Image")

    @classmethod
    def ascii(cls: Type[IF]) -> IF:
        """
        Turns an Image into a ascii-fied image.
        """
        return cls("/ascii/", "Turns an Image into a ascii-fied image")

    @classmethod
    def charcoal(cls: Type[IF]) -> IF:
        """
        Turns an Image into a charcoal sketch.
        """
        return cls("/charcoal/", "Turns an Image into a charcoal sketch")

    @classmethod
    def poster(cls: Type[IF]) -> IF:
        """
        Posterizes an image.
        """
        return cls("/poster/", "Posterizes an image")

    @classmethod
    def sepia(cls: Type[IF]) -> IF:
        """
        Makes an image sepia tone.
        """
        return cls("/sepia/", "Makes an image sepia tone")

    @classmethod
    def polaroid(cls: Type[IF]) -> IF:
        """
        Frames an Image like a printed polaroid.
        """
        return cls("/polaroid/", "Frames an Image like a printed polaroid")

    @classmethod
    def glitch(cls: Type[IF]) -> IF:
        """
        *Cool Glitched image*
        """
        return cls("/glitch/", "*Cool Glitched image*")

    @classmethod
    def swirl(cls: Type[IF]) -> IF:
        """
        Swirls the center of Image.
        """
        return cls("/swirl/", "Swirls the center of Image")

    @classmethod
    def paint(cls: Type[IF]) -> IF:
        """
        Turns an Image into an oil painting.
        """
        return cls("/paint/", "Turns an Image into an oil painting")

    @classmethod
    def sketch(cls: Type[IF]) -> IF:
        """
        How an artist would create an image.
        """
        return cls("/sketch/", "How an artist would create an image.")

    @classmethod
    def spin(cls: Type[IF]) -> IF:
        """
        the gif goes round and round.
        """
        return cls("/spin/", "the gif goes round and round")

    @classmethod
    def dissolve(cls: Type[IF]) -> IF:
        """
        Thanos snapped and back.
        """
        return cls("/dissolve/", "Thanos snapped and back.")

    @classmethod
    def neon(cls: Type[IF]) -> IF:
        """
        A cool multicolored glowing neon sign from an image.
        """
        return cls("/neon/", "A cool multicolored glowing neon sign form an image.")

    @classmethod
    def petpet(cls: Type[IF]) -> IF:
        """
        Pet Pet Pet.
        """
        return cls("/petpet/", "Pet Pet Pet.")

    @classmethod
    def comic(cls: Type[IF]) -> IF:
        """
        classic black and white comic.
        """
        return cls("/comic/", "Classic black and white commic.")

    @classmethod
    def burn(cls: Type[IF]) -> IF:
        """
        Burn an image untill there's molten remains.
        """
        return cls("/burn/", "Burn an image untill there's molten remains.")

    @classmethod
    def freeze(cls: Type[IF]) -> IF:
        """
        Get blasted by Mr.Freeze from batman.
        """
        return cls("/freeze/", "Get blasted by Mr.Freeze from batman.")

    @classmethod
    def earth(cls: Type[IF]) -> IF:
        """
        Become one with Rock.
        """
        return cls("/earth/", "Become one with rock.")

    @classmethod
    def night(cls: Type[IF]) -> IF:
        """
        Turns day into night on an Image.
        """
        return cls("/night/", "Turns day into night on an Image")

    @classmethod
    def magik(cls: Type[IF]) -> IF:
        """
        Magik an Image
        """
        return cls("/magik/", "Magik an Image")

    @classmethod
    def stringify(cls: Type[IF]) -> IF:
        """
        Stringify an Image
        """
        return cls("/stringify/", "Stringify an Image")

    @classmethod
    def rainbow(cls: Type[IF]) -> IF:
        """
        Rainbow light effect on image
        """
        return cls("/rainbow/", "Rainbow light effect on image")

    @classmethod
    def solar(cls: Type[IF]) -> IF:
        """
        Solarizes an Image.
        """
        return cls("/solar/", "Solarizes an Image")

    @classmethod
    def bonk(cls: Type[IF]) -> IF:
        """
        Bonk Someone
        """
        return cls("/bonk/", "Bonk Someone")

    @classmethod
    def captcha(cls: Type[IF]) -> IF:
        """
        Creates a realistic Captcha
        Needs:
            - text
            - image
        """
        return cls("/captcha/", "Creates a realistic Captcha")

    @classmethod
    def thought_image(cls: Type[IF]) -> IF:
        """
        Wraps Image and Text into a thought
        Needs:
            - text
            - image
        """
        return cls("/thoughtimage/", "Wraps Image and Text into a thought")

    @classmethod
    def tweet(cls: Type[IF]) -> IF:
        """
        Generates an accurate fake tweet
        Needs:
            - text
            - image
            - username
        """
        return cls("/tweet/", "Generates an accurate fake tweet")

    @classmethod
    def discord(cls: Type[IF]) -> IF:
        """
        Generated a realistic Discord Message
        Needs:
            - text
            - image
            - username
            - dark (boolean) default is true
        """
        return cls("/discord/", "Generated a realistic Discord Message")

    @classmethod
    def youtube(cls: Type[IF]) -> IF:
        """
        Generated a realistic Yutube comment
        Needs:
            - text
            - image
            - username
            - dark (boolean) default is true
        """
        return cls("/yt/", "Generated a realistic Yutube comment")

    @classmethod
    def retro_meme(cls: Type[IF]) -> IF:
        """
        old 2012 advice animals style meme
        Needs:
            - top_text
            - bottom_text
            - image
        """
        return cls("/retromeme/", "Generated a realistic Discord Message")

    @classmethod
    def motiv(cls: Type[IF]) -> IF:
        """
        old 2012 style Motiv memes
        Needs:
            - top_text
            - bottom_text
            - image
        """
        return cls("/motiv/", "old 2012 style Motiv memes")

    @classmethod
    def modern_meme(cls: Type[IF]) -> IF:
        """
        Mordern meme with text scaling
        Needs:
            - text
            - image
        """
        return cls("/modernmeme/", "Modern New meme style meme")

    @classmethod
    def mosiac(cls: Type[IF]) -> IF:
        """
        Turn an image into a roman mosiac
        Needs:
            - image
            - pixels
        """
        return cls("/mosiac/", "Turn an image into a roman mosiac")

    @classmethod
    def cube(cls: Type[IF]) -> IF:
        """
        Turn an image into a cube
        Needs:
            - image
        """
        return cls("/cube/", "Turn an image into a cube")

    @classmethod
    def lego(cls: Type[IF]) -> IF:
        """
        image out of lego bricks
        Needs:
            - image
        """
        return cls("/lego/", "image out of lego bricks")

    @classmethod
    def expand(cls: Type[IF]) -> IF:
        """
        blown out of proportions
        Needs:
            - image
        """
        return cls("/expand/", "blown out of proportions")

    @classmethod
    def from_string(cls: Type[IF], feature: str) -> Optional[IF]:
        """Get an image feature from a string

        Args:
            cls (Type[IF]): class stuff
            feature (str): string feature to try

        Returns:
            IF: Image Feature
        """
        try:
            image_feature = getattr(cls, feature)
            called = image_feature()
            return cls(called.value, called.description)
        except BaseException:
            return None
