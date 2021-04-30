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
        strings = "What is a web application?"
        question = Text(strings)
        question.set_color_by_gradient(BLUE, GREEN)
        #question.set_color_by_t2c({"applications": YELLOW})
        self.wait()
        self.play(
            LaggedStartMap(FadeIn, question)
        )
        self.play(
            FadeOutAndShift(question, direction=RIGHT)
        )

class Software(Scene):
    def construct(self):
        compsoftware = Utils.svgToWhite("assets/compsoftware.svg").shift(DOWN*2)
        server = Utils.svgToWhite("assets/server.svg").shift(UP*2, LEFT*3)
        userapp = Utils.svgToWhite("assets/webpage.svg").shift(UP*2)
        appgroup = VGroup(userapp, server)
        user = Utils.svgToWhite("assets/user.svg").next_to(compsoftware, direction=RIGHT).scale(0.7)
        normalSoftware = Utils.textbox("Normal Software").align_to(compsoftware, direction=DOWN)
        webApplication = Utils.textbox("Web Application").align_to(userapp, direction=UP)

        self.play(FadeIn(webApplication))
        self.play(FadeTransform(webApplication, appgroup))
        self.wait()
        self.play(FadeIn(normalSoftware))
        self.play(FadeTransform(normalSoftware, compsoftware))
        self.play(FadeIn(user))
        self.wait(1.5)
        self.play(server.animate.shift(LEFT * 1), userapp.animate.shift(RIGHT * 4))
        self.play(user.animate.next_to(userapp, direction=LEFT))
        self.wait()
        self.play(user.animate.next_to(server, direction=RIGHT), run_time=2)
        self.wait(2)


        self.play (
            LaggedStartMap(FadeOut, self.get_top_level_mobjects())
        )

class PhonePCTablet(Scene):
    def construct(self):
        phone = Utils.svgToWhite("assets/phone.svg").shift(LEFT * 3)
        desktop = Utils.svgToWhite("assets/desktop.svg")
        tablet = Utils.svgToWhite("assets/tablet.svg").shift(RIGHT * 3)
        web = Utils.svgToWhite("assets/web.svg").shift(UP * 2).scale(0.85)

        gp = VGroup(phone, desktop, tablet)
        self.play( Create(web), runtime=2 )
        self.wait()
        self.play( Create(gp), run_time=3 )
        
        #shift down
        
        self.play( gp.animate.shift(DOWN*2) )
        self.wait(2)
        self.play( ScaleInPlace(gp, 0.7) )
        self.play( web.animate.shift(UP*0.5), gp.animate.shift(DOWN*0.5) )

        question = Text("How they actually work?").shift(DOWN*0.15)
        question.set_color_by_gradient(GREEN, BLUE)
        self.wait(2)
        self.play(
            LaggedStartMap(Write, question)
        )
        self.wait()
        self.play (
            LaggedStartMap(FadeOut, self.get_top_level_mobjects())
        )
        

class ClientServer(Scene):
    def construct(self):
        web = Utils.svgToWhite("assets/web.svg").scale(0.9).shift(LEFT*2)
        client = Utils.textbox("Client").shift(UP, RIGHT)
        server = Utils.textbox("Server").shift(DOWN, RIGHT)
        userapp = Utils.svgToWhite("assets/webpage.svg").shift(UP*2, RIGHT*3)
        serversvg = Utils.svgToWhite("assets/server.svg").shift(DOWN*2, RIGHT*3)
        webui = Utils.svgToWhite("assets/webui.svg").shift(LEFT*1)
        cloudserver = Utils.svgToWhite("assets/cloudserver.svg").shift(LEFT*1)
        database = Utils.svgToWhite("assets/database.svg").shift(LEFT*1)

        self.play(FadeIn(web))
        self.play(Create(client), Create(server), run_time=1)
        self.wait()
        self.play(Transform(client, userapp), run_time=2)
        self.wait()
        self.play(Transform(server, serversvg), run_time=2)
        toUncreate = self.get_top_level_mobjects()
        toUncreate.remove(web)
        self.play(LaggedStartMap(Uncreate, toUncreate))
        self.wait(2)
        self.play(web.animate.shift(LEFT*1.5).scale(0.9))

        self.play(Create(webui))
        self.play(webui.animate.shift(RIGHT*3, UP*2.5).scale(0.8))
        self.wait(2)
        self.play(Create(cloudserver))
        self.play(cloudserver.animate.shift(RIGHT*3).scale(0.8))
        self.wait(2)
        self.play(Create(database))
        self.play(database.animate.shift(RIGHT*3, DOWN*2.5).scale(0.8))
        self.wait(3)
        self.play(FadeOut(web))
        
        gp = VGroup(cloudserver, database)
        webuiG = VGroup(webui)
        gp += webuiG
        
        self.play(gp.animate.shift(LEFT*4).scale(0.9))
        self.wait(5)
        gp -= webuiG
        self.add(webui)
        frontend = BraceText(webuiG, "Frontend", brace_direction=RIGHT)
        self.play(Write(frontend))
        backend = BraceText(gp, "Backend", brace_direction=RIGHT)
        self.play(Write(backend))
        self.wait(2)
        self.play(*[ obj.animate.shift(LEFT*2) for 
            obj in self.get_top_level_mobjects() ], run_time = 1)
        frontText = Text("User Interface").next_to(frontend).scale(0.8)
        backText = Text("Server Side").next_to(backend).scale(0.8)
        self.play(FadeIn(frontText))
        self.wait(3)
        self.play(FadeIn(backText))
        self.wait(10)
        self.play(LaggedStartMap(Uncreate, self.get_top_level_mobjects()))
        
        
class BrowserExample(Scene):
    def construct(self):
        browser = Utils.svgToWhite("assets/browser.svg")
        self.wait(4.5)
        question = Text("Client-Server Request and Response").scale(0.9)
        question.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(question))
        self.wait(2)
        self.play(Unwrite(question))
        self.wait(2.5)
        self.play(FadeIn(browser))
        self.play(browser.animate.scale(3.8))
        url = Tex("\\texttt{facebook.com}", font='inconsolata').align_to(browser, UP).shift(DOWN*0.7, RIGHT*0.8).scale(1.3)
        self.play(Write(url))

        browserurl = VGroup(browser, url)
        self.wait(0.5)
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
        self.wait(0.5)
        self.play(GrowArrow(WebToDBArrow))
        self.wait(7)
        business_logic = Utils.svgToWhite("assets/gear.svg").next_to(WebToDBArrow, direction=UP).scale(0.85)
        self.play(Create(business_logic))
        self.wait(10)
        self.play(FadeOut(WebToDBArrow), Uncreate(business_logic))

        DBToWebArrow = Arrow(databaseSvg.get_edge_center(RIGHT), webServer.get_edge_center(LEFT))
        self.play(GrowArrow(DBToWebArrow))
        self.wait(1)
        self.play(FadeOut(DBToWebArrow))

        WebToBrowserArrow = Arrow(webServer.get_edge_center(LEFT), browserurl.get_edge_center(RIGHT))
        self.play(GrowArrow(WebToBrowserArrow))
        self.wait(1)
        self.play(FadeOut(WebToBrowserArrow))

        # TODO transform the previous empty browser to with content
        
        colorWeb = SVGMobject("assets/colorwebpage.svg").scale(2.5)
        self.play(LaggedStartMap(Uncreate, [database, dns, web]))
        self.play(Transform(browserurl, colorWeb), run_time=3)
        self.wait(8)
        self.play (
            LaggedStartMap(FadeOut, self.get_top_level_mobjects()), run_time=3
        )
        
        self.wait(2)


class Framework(Scene):
    def construct(self):
        theory = Utils.textbox("Theory").shift(LEFT*3)
        practice = Utils.textbox("Practice").shift(RIGHT*3)
        question = Text("How webapps are implemented?")
        question.set_color_by_gradient(PURPLE, GREEN)
        self.play(Write(question), run_time=2)
        self.wait(2)
        self.play(Unwrite(question), run_time=1.5)
        self.wait(1)

        self.play(Write(theory), Write(practice), run_time=3)
        self.wait(6)
        self.play(Unwrite(theory), Unwrite(practice), runtime=2)
        self.wait(1)

        userapp = Utils.svgToWhite("assets/webpage.svg").shift(UP*2)
        serversvg = Utils.svgToWhite("assets/server.svg").shift(DOWN*2)
        client = Utils.textbox("Client", buff=MED_SMALL_BUFF).next_to(userapp)
        server = Utils.textbox("Server", buff=MED_SMALL_BUFF).next_to(serversvg)
        framework = Utils.svgToWhite("assets/framework.svg")
        ffs = [framework.copy().shift(DOWN*i*2.7 + RIGHT*j*2.7).set_color(random_color()) 
            for i in range(-1, 2) for j in range(-1, 2)]
        frameworks = VGroup(*ffs)

        clientServer = VGroup(userapp, serversvg)
        clientServerwithText = VGroup(userapp, serversvg, client, server)
        self.play(Create(clientServerwithText), run_time=3)
        self.wait(10)
        self.play(ReplacementTransform(clientServerwithText, framework), run_time=2)
        self.wait(7)
        self.play(framework.animate.scale(1.2), run_time=2)
        self.wait(5)
        self.play(ReplacementTransform(framework, frameworks), run_time=2.5)
        self.wait(17)
        userapp = Utils.svgToWhite("assets/webpage.svg").shift(UP*2)
        serversvg = Utils.svgToWhite("assets/server.svg").shift(DOWN*2)
        clientServer = VGroup(userapp, serversvg)
        self.play(ReplacementTransform(frameworks, clientServer), run_time=4)
        self.wait(3)
        

        strings = "COM217 Group 404\nArda Gurer\n Bradley Bottomlee\nCharlo Zhu\nShangyin Tan".splitlines()
        names = [ Text(i) for i in strings ]
        names[0].shift(UP*2).set_color_by_gradient(BLUE_A, GREEN)
        for i in range(len(names) - 1):
            names[i+1].next_to(names[i], DOWN).set_color_by_gradient(BLUE_A, GREEN)
        
        self.play(ReplacementTransform(clientServer, names[0]), run_time=2)
        self.play(*[Write(s) for s in names[1:]], run_time=3)
        self.play(*[Unwrite(s) for s in self.get_top_level_mobjects()], run_time=3)


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
        #self.add_sound("assets/refl1min.wav")
        Introduction.construct(self)
        Software.construct(self)
        PhonePCTablet.construct(self)
        ClientServer.construct(self)
        BrowserExample.construct(self)
        Framework.construct(self)