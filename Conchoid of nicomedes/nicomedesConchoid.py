from manim import *
import numpy as np

class Conchoid(MovingCameraScene):

    def construct(self):
        
        title = Tex("Conchoid of Nicomedes").move_to(UP*2.5)
        title.font_size=60
        self.play(Write(title))
        self.wait(2)

        ac = Tex("Arran Cheung").move_to(UP*1.5)
        sf = Tex("Samim Fayazi").move_to(UP*1)
        kh = Tex("Kenneth Ha").move_to(UP*0.5)

        self.play(Write(VGroup(ac,sf,kh)))

        self.wait(3)

        self.play(FadeOut(VGroup(ac,sf,kh)))
        self.play(FadeOut(title))

        self.wait(0.3)

        # What is a conchoid + History

        whatIsAConchoid = Tex("What is a conchoid?").move_to(UP*2)
        self.play(Write(whatIsAConchoid))

        conchoidDescription = Tex("A conchoid is a curve generated using: a fixed point, a curve and a length k").move_to(UP*1)
        conchoidDescription.font_size = 34
        self.play(Write(conchoidDescription))
        self.wait(4)

        inventor = Tex("Invented by Greek mathematician Nicomedes").move_to(DOWN*0.5)
        inventor.font_size = 34
        self.play(Write(inventor))

        self.wait(3)

        whatDidHeDo = Tex("He tried to solve geometric problems such as doubling the cube and trisecting the angle").move_to(DOWN*1.5)
        whatDidHeDo.font_size = 34
        self.play(Write(whatDidHeDo))

        self.wait(3.4)

        # end of history section

        self.play(FadeOut(VGroup(whatIsAConchoid, conchoidDescription, inventor, whatDidHeDo)))

        # Basic construction

        construction = Tex("Construction").move_to(UP*2.5)
        self.play(Write(construction))

        self.wait(0.5)
        self.play(FadeOut(construction))  

        originDot = Dot(ORIGIN, color=RED)
        self.play(Write(originDot))
        originLabel = Tex("O").move_to(RIGHT*0.5 + DOWN*0.5)
        self.play(Write(originLabel))
        self.wait(0.3)

        line = Line(start=4*LEFT+3*DOWN, end=4 * RIGHT + 3 * UP)
        lineLabel = Tex("m").move_to(4.5*LEFT+3*DOWN)
        self.play(Write(line))
        self.play(Write(lineLabel))
        self.wait(0.3)

        straightLine = Line(start=4*LEFT + 1*UP, end=4*RIGHT+1*UP)
        self.play(Write(straightLine))
        straightLineLabel = Tex("l").move_to(4.5*LEFT + 1*UP)
        self.play(Write(straightLineLabel))
        self.wait(0.3)

        lineMLabel = Tex("m is a line passing through O and given line l").move_to(1*RIGHT+3*DOWN)
        lineMLabel.font_size = 34
        self.play(Write(lineMLabel))
        self.wait(0.6)

        self.play(FadeOut(lineMLabel))

        p1, p2 = line.get_start(), line.get_end()
        p3, p4 = straightLine.get_start(), straightLine.get_end()
        intersection = line_intersection((p1,p2), (p3,p4))
        intersectionDot = Dot(intersection, color=RED)
        self.add(intersectionDot)
        intersectionLabel = Tex("p").move_to(intersection + DOWN*0.5 + RIGHT*0.5)
        self.play(Write(intersectionLabel))

        k = 3
        gradient = 3/4
        angle = np.arctan(gradient)
        xComp = k*np.cos(angle)
        yComp = k*np.sin(angle)

        Q1 = Dot(intersection + xComp * LEFT + yComp * DOWN, color=RED)
        self.play(Write(Q1))
        q1Label = Tex("Q1").move_to(intersection + xComp * LEFT + yComp * DOWN + 0.5 *RIGHT + 0.5 * DOWN)
        self.play(Write(q1Label))

        Q2 = Dot(intersection + xComp * RIGHT + yComp * UP, color=RED)
        self.play(Write(Q2))
        q2Label = Tex("Q2").move_to(intersection + xComp * RIGHT + yComp * UP + 0.5 * RIGHT + 0.5 * DOWN)
        self.play(Write(q2Label))

        distanceKText = Tex("distance[Q1,p] = distance[Q2,p] = k").move_to(LEFT*2 + 2.5*UP)
        distanceKText.font_size=34
        self.play(Write(distanceKText))
        self.wait(2)

        self.play(FadeOut(distanceKText))

        formationOfConchoid = Tex("The locus of Q1 and Q2 as p varies along l is the").move_to(LEFT*2.7 + 2.5*UP)
        conchoidOfNicomedes = Tex("Conchoid of Nicomedes").move_to(LEFT*0.75 + 2*UP)
        formationOfConchoid.font_size = 34
        conchoidOfNicomedes.font_size = 34
        self.play(Write((VGroup(formationOfConchoid, conchoidOfNicomedes))))

        self.wait(3.5)

        self.play(FadeOut(VGroup(formationOfConchoid, conchoidOfNicomedes, originDot, originLabel, intersectionDot, intersectionLabel, lineLabel, q1Label, q2Label)))

        self.play(Rotate(VGroup(line, Q1, Q2), 2.5*PI/4, about_point=ORIGIN, run_time=2, rate_func=linear))


        # end of construction

        self.wait(4)

        # transition

        self.play(FadeOut(VGroup( line, straightLine, straightLineLabel, Q1, Q2)))

        # equations

        equations = Tex("Equations").move_to(UP*2.5)
        self.play(Write(equations))

        conchoidEq = Tex(r"$r=\frac{b}{\sin \theta}\pm k$").move_to(UP*1)
        self.play(Write(conchoidEq))

        self.wait(2)

        explainConstants = Tex("where $y=b$ the asymptote of the curve, $k$ is the distance from the point to the line")
        explainConstants.font_size = 34
        self.play(Write(explainConstants))

        self.wait(3.5)

        self.play(FadeOut(explainConstants))

        evaluateK = Tex("$k$ controls the size of the conchoid").move_to(DOWN*0.5)
        evaluateK.font_size = 34
        self.play(Write(evaluateK))

        self.wait(2)

        evaluateB = Tex("$b$ controls the distance from the origin to the conchoid").move_to(DOWN*1.5)
        evaluateB.font_size = 34
        self.play(Write(evaluateB))

        # end of equations

        self.wait(3)
        
        # transition

        self.play(FadeOut(VGroup(equations, conchoidEq, evaluateK, evaluateB)))

        # start of overall construction

        curves = VGroup()
        
        def ConchoidConstruct(l):
            a = 1
            tMax = ValueTracker(0.01)

            lvalue = Tex("k = " , -l).move_to(DOWN * 3 + 3*LEFT)
            self.play(FadeIn(lvalue))

            def conchoid_func(t):
                eps = 1e-3

                sin_t = np.sin(t)
                if abs(sin_t) < eps:
                    sin_t = eps if sin_t >= 0 else -eps

                r = a / sin_t + l # polar version of conchoid
                return np.array([r * np.cos(t), r * np.sin(t), 0]) # converting coords into cartesian
            
            def conchoid_func_minus(t):
                eps = 1e-3

                sin_t = np.sin(t)
                if abs(sin_t) < eps:
                    sin_t = eps if sin_t >= 0 else -eps

                r = a / sin_t - l # polar version of conchoid
                return np.array([r * np.cos(t), r * np.sin(t), 0]) # converting coords into cartesian

            large_conchoid = always_redraw(lambda: ParametricFunction(
                conchoid_func,
                t_range=[0, tMax.get_value()],
                color=YELLOW
            ))

            small_conchoid = always_redraw(lambda: ParametricFunction(
                conchoid_func_minus,
                t_range=[0, tMax.get_value()],
                color=YELLOW
            ))

            self.add(large_conchoid, small_conchoid)  
            curves.add(large_conchoid)
            curves.add(small_conchoid)
            self.play(tMax.animate.set_value(PI), run_time=7, rate_func=linear)
            self.wait()

            self.play(FadeOut(lvalue))

        for i in range(5):
            ConchoidConstruct(-i)

        self.wait(3)

        self.play(FadeOut(curves))
        self.wait()

        # Practical uses

        usesOfCN = Tex("Applications").move_to(UP*2.5)
        self.play(Write(usesOfCN))

        angleTrisection = Tex("Angle trisection: Splitting an angle into 3 equal angles").move_to(UP*1.5)
        angleTrisection.font_size = 34
        self.play(Write(angleTrisection))

        LineonePointfive = Line(start=LEFT*2 +DOWN*2.5 ,end= DOWN*2.5)
        LineonePointfive.color = YELLOW
        self.play(Write(LineonePointfive))

        verticalLine = Line(start= LEFT*2+DOWN*2.5, end=DOWN*0.5+LEFT*2)
        verticalLine.color = YELLOW
        self.play(Write(verticalLine))

        perpAngle = RightAngle(LineonePointfive, verticalLine, length=0.4, color=YELLOW)
        perpAngleLabel = Tex("90$^\circ$").move_to(LEFT*1 + DOWN*2)
        perpAngleLabel.font_size = 34
        self.play(Write(perpAngle))
        self.play(Write(perpAngleLabel))
        self.wait(0.75)
        self.play(FadeOut(VGroup(perpAngleLabel, perpAngle)))

        diagLine1 = Line(start=LEFT*2+DOWN*2.5, end= DOWN*2.5).rotate(PI/6, about_point=LEFT*2+DOWN*2.5)
        diagLine2 = Line(start=LEFT*2+DOWN*2.5, end= DOWN*2.5).rotate(2*PI/6, about_point=LEFT*2+DOWN*2.5)

        self.play(Write(diagLine1))
        self.play(Write(diagLine2))

        self.wait(4)

        # end of applications

        self.play(FadeOut(VGroup(usesOfCN, angleTrisection, LineonePointfive, verticalLine, diagLine1, diagLine2)))

        # References

        references = Tex("References").move_to(UP*2)
        self.play(Write(references))
        doc = Tex("Wikipedia: en.wikipedia.org/wiki/Conchoid").move_to(UP*1.5)
        doc.font_size = 30
        self.play(Write(doc))
        doc1 = Tex("3D-XploreMath project: www.math.uni-bonn.de/people/karcher/VMMPlaneCurves/docs/Conchoid.pdf").move_to(UP*0.5)
        doc1.font_size = 30
        self.play(Write(doc1))
        code = Tex("Code: github.com/ArranCheung/Conchoid-of-Nicomedes-Animation/tree/main").move_to(DOWN*0.5)
        code.font_size = 30
        self.play(Write(code))
        self.wait(3.5)

        self.play(FadeOut(VGroup(references, doc, doc1, code)))