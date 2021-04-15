from manim import *

class Utils():
    @staticmethod
    def textbox(text):
        textobj = Text(text)
        square = Rectangle().surround(textobj)
        return VGroup(textobj, square)

    @staticmethod
    def svgToWhite(path):
        svgobj = SVGMobject(path)
        for sub_mob in svgobj:
            sub_mob.set_color(WHITE)
        return svgobj

class Introduction(Scene):
    def construct(self):
        strings = "What are web applications?"
        question = Text(strings)
        question.set_color_by_t2c({"applications": YELLOW})
        self.wait()
        self.play(
            LaggedStartMap(FadeIn, question)
        )
        self.wait(2)
        self.play(
            Uncreate(question)
        )


class PhonePCTablet(Scene):
    def construct(self):
        phone = Utils.svgToWhite("assets/phone.svg").shift(LEFT * 3)
        desktop = Utils.svgToWhite("assets/desktop.svg")
        tablet = Utils.svgToWhite("assets/tablet.svg").shift(RIGHT * 3)
        web = Utils.svgToWhite("assets/web.svg").shift(UP * 1).scale(1.3)

        gp = VGroup(phone, desktop, tablet)
        self.wait()

        # spawn devices
        for device in gp:
            self.play( Create(device), run_time=1 )
        
        #shift down
        self.play( gp.animate.shift(DOWN*2) )
        self.play( ScaleInPlace(gp, 0.7) )
        self.play( Create(web), runtime=1.5 )
        self.play( web.animate.shift(UP), gp.animate.shift(DOWN*0.5) )

        question = Text("How they actually work?").shift(DOWN*0.15)
        question.set_color_by_t2c({"work": YELLOW})
        self.wait()
        self.play(
            LaggedStartMap(Write, question)
        )
        self.wait(2)
        self.play (
            LaggedStartMap(FadeOut, self.get_top_level_mobjects())
        )
        
        self.wait(2)

class ClientServer(Scene):
    def construct(self):
        web = Utils.svgToWhite("assets/web.svg")
        client = Utils.textbox("Client").shift(UP, RIGHT)
        server = Utils.textbox("Server").shift(DOWN, RIGHT)
        userapp = Utils.svgToWhite("assets/webpage.svg").shift(UP*2, RIGHT*3)
        serversvg = Utils.svgToWhite("assets/server.svg").shift(DOWN*2, RIGHT*3)
        webui = Utils.svgToWhite("assets/webui.svg").shift(LEFT*1)
        cloudserver = Utils.svgToWhite("assets/cloudserver.svg").shift(LEFT*1)
        database = Utils.svgToWhite("assets/database.svg").shift(LEFT*1)

        self.play(FadeIn(web))
        self.play(web.animate.shift(LEFT*2))
        self.play(Create(client), Create(server), run_time=1)
        self.wait(2)
        self.play(Transform(client, userapp), run_time=2)
        self.play(Transform(server, serversvg), run_time=2)
        toUncreate = self.get_top_level_mobjects()
        toUncreate.remove(web)
        self.play(LaggedStartMap(Uncreate, toUncreate))
        self.play(web.animate.shift(LEFT*1.5).scale(0.9))

        self.play(Create(webui))
        self.play(webui.animate.shift(RIGHT*4, UP*2.5).scale(0.9))
        self.play(Create(cloudserver))
        self.play(cloudserver.animate.shift(RIGHT*4).scale(0.9))
        self.play(Create(database))
        self.play(database.animate.shift(RIGHT*4, DOWN*2.5).scale(0.9))
        self.wait()
        self.play(FadeOut(web))
        
        gp = VGroup(cloudserver, database)
        webuiG = VGroup(webui)
        gp += webuiG
        
        self.play(gp.animate.shift(LEFT*5).scale(0.8))

        gp -= webuiG
        self.add(webui)
        self.play(Write(BraceText(webuiG, "Frontend", brace_direction=RIGHT)))
        self.play(Write(BraceText(gp, "Backend", brace_direction=RIGHT)))
        self.wait()
        
class BrowserExample(Scene):
    def construct(self):
        pass

class SpecificClientServer(Scene):
    pass


class ClientTest(Scene):
    def construct(self):
        text = Text("Client")
        square = Rectangle()
        square.surround(text)
        
        self.wait(5)

class Main(Scene):
    def construct(self):
        self.add_sound("assets/ref35.wav")
        Introduction.construct(self)
        PhonePCTablet.construct(self)
        ClientServer.construct(self)
        BrowserExample.construct(self)