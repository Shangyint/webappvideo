from manim import *

class Utils():
    @staticmethod
    def textbox(text, buff=MED_LARGE_BUFF):
        textobj = Text(text)
        square = SurroundingRectangle(textobj, color=WHITE, buff=buff)
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
        question.set_color_by_gradient(BLUE, GREEN)
        #question.set_color_by_t2c({"applications": YELLOW})
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
        self.wait(3)
        self.play(LaggedStartMap(Uncreate, self.get_top_level_mobjects()))
        self.wait(2)
        
class BrowserExample(Scene):
    def construct(self):
        browser = Utils.svgToWhite("assets/browser.svg")
        self.play(FadeIn(browser))
        self.play(browser.animate.scale(3.8))
        url = Tex("\\texttt{facebook.com}", font='inconsolata').align_to(browser, UP).shift(DOWN*0.7, RIGHT*0.8).scale(1.3)
        self.play(Write(url))

        browserurl = VGroup(browser, url)
        self.play(browserurl.animate.scale(0.3).shift(LEFT*3.5))

        dnsServer = Utils.svgToWhite("assets/server.svg")
        dnsText = Utils.textbox("Domain Name\n      Server", buff=MED_SMALL_BUFF).scale(0.3).next_to(dnsServer, UP)
        dns = VGroup(dnsServer, dnsText)
        self.play(Create(dns))
        self.play(dns.animate.shift(RIGHT*3.5))

        browserToDnsArrow = Arrow(browser.get_edge_center(RIGHT), dnsServer.get_edge_center(LEFT))
        self.play(GrowArrow(browserToDnsArrow))
        self.wait(1)
        
        browserAndDns = VGroup(dns, browserurl, browserToDnsArrow)
        newDnsText = dnsText.next_to(dnsServer, DOWN)
        self.play(browserAndDns.animate.shift(UP*2.5))
        self.play(Transform(dnsText, newDnsText))
        self.play(FadeOut(browserToDnsArrow))

        webServer = Utils.svgToWhite("assets/server.svg")
        webText = Utils.textbox("Web Server", buff=MED_SMALL_BUFF).scale(0.3).next_to(webServer, UP)
        web = VGroup(webServer, webText)
        self.play(Create(web))
        self.play(web.animate.shift(RIGHT*3.5, DOWN*2.5))
        DnsToWebArrow = Arrow(newDnsText.get_edge_center(DOWN), webText.get_edge_center(UP))
        self.play(GrowArrow(DnsToWebArrow))
        self.wait(2)
        self.play(FadeOut(DnsToWebArrow))

        databaseSvg = Utils.svgToWhite("assets/database.svg")
        databaseText = Utils.textbox("Database", buff=MED_SMALL_BUFF).scale(0.3).next_to(databaseSvg, UP)
        database = VGroup(databaseSvg, databaseText)
        self.play(Create(database))
        self.play(database.animate.shift(LEFT*3.5, DOWN*2.5))

        WebToDBArrow = Arrow(webServer.get_edge_center(LEFT), databaseSvg.get_edge_center(RIGHT))
        self.play(GrowArrow(WebToDBArrow))
        self.wait(2)
        self.play(FadeOut(WebToDBArrow))

        DBToWebArrow = Arrow(databaseSvg.get_edge_center(RIGHT), webServer.get_edge_center(LEFT))
        self.play(GrowArrow(DBToWebArrow))
        self.wait(2)
        self.play(FadeOut(DBToWebArrow))

        WebToBrowserArrow = Arrow(webServer.get_edge_center(LEFT), browserurl.get_edge_center(RIGHT))
        self.play(GrowArrow(WebToBrowserArrow))
        self.wait(2)
        self.play(FadeOut(WebToBrowserArrow))

        # TODO transform the previous empty browser to with content

        self.wait(3)

        

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
        self.add_sound("assets/refl1min.wav")
        Introduction.construct(self)
        PhonePCTablet.construct(self)
        ClientServer.construct(self)
        BrowserExample.construct(self)