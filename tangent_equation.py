import math

def tangent_equation():
    points = [1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.85,1.9,1.95]
    for point in points:
        slope = math.cos(point) - 0.5
        out_at_y = math.sin(point)-(point/2)+10
        eqn = slope*(-point)+out_at_y
        new_point = point + 2*math.pi
        slopeB = math.cos(new_point) - 0.5
        out_at_B = math.sin(new_point)-(new_point/2)+10
        eqn_B = slopeB*(-new_point)+out_at_B
        if eqn_B == eqn:
            print("The points are: ({}) and ({})".format(y,round(new_point,4)))
            pass
        print("Checked!")
    #print("The equation of the tangent line is: {}x+ {}".format(round(slope,4),round(eqn,4)))

tangent_equation()