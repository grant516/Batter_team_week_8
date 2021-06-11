import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        right_up = Point(1,-1)
        right_down = Point(1,1)
        left_up = Point(-1,-1)
        left_down = Point(-1,1)

        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        #marquee.set_text("")
        ball_direction = ball.get_velocity()
        paddle_spot = paddle.get_position()

        #deals with the collision of the bricks and the ball
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                if(ball_direction.get_x() == left_up.get_x() and ball_direction.get_y() == left_up.get_y() and brick.get_text() == "*"):
                    ball.set_velocity(left_down)
                elif(ball_direction.get_x() == left_down.get_x() and ball_direction.get_y() == left_down.get_y() and brick.get_text() == "*"):
                    ball.set_velocity(left_up)
                elif(ball_direction.get_x() == right_up.get_x() and ball_direction.get_y() == right_up.get_y() and brick.get_text() == "*"):
                    ball.set_velocity(right_down)
                elif(ball_direction.get_x() == right_down.get_x() and ball_direction.get_y() == right_down.get_y() and brick.get_text() == "*"):
                    ball.set_velocity(right_up)

                if(brick.get_text() == "*"):
                    brick.set_text("")

        #Deals the with collision of the paddle and the ball
        for x in range (0, len(paddle.get_text())):
            if ((ball.get_position().get_x() == paddle_spot.get_x()+x) and (ball.get_position().get_y() == paddle_spot.get_y()-1)):
                if(ball_direction.get_x() == left_up.get_x() and ball_direction.get_y() == left_up.get_y()):
                    ball.set_velocity(left_down)
                elif(ball_direction.get_x() == left_down.get_x() and ball_direction.get_y() == left_down.get_y()):
                    ball.set_velocity(left_up)
                elif(ball_direction.get_x() == right_up.get_x() and ball_direction.get_y() == right_up.get_y()):
                    ball.set_velocity(right_down)
                elif(ball_direction.get_x() == right_down.get_x() and ball_direction.get_y() == right_down.get_y()):
                    ball.set_velocity(right_up)

        if(ball.get_position().get_x()-1 == 0):
            if(ball_direction.get_x() == left_up.get_x() and ball_direction.get_y() == left_up.get_y()):
                    ball.set_velocity(right_up)
            elif(ball_direction.get_x() == left_down.get_x() and ball_direction.get_y() == left_down.get_y()):
                ball.set_velocity(right_down)
        elif(ball.get_position().get_x()+1 == constants.MAX_X):
            if(ball_direction.get_x() == right_up.get_x() and ball_direction.get_y() == right_up.get_y()):
                    ball.set_velocity(left_up)
            elif(ball_direction.get_x() == right_down.get_x() and ball_direction.get_y() == right_down.get_y()):
                ball.set_velocity(left_down)

        elif(ball.get_position().get_y()-1 == 0):
            if(ball_direction.get_x() == left_up.get_x() and ball_direction.get_y() == left_up.get_y()):
                    ball.set_velocity(left_down)
            elif(ball_direction.get_x() == left_down.get_x() and ball_direction.get_y() == left_down.get_y()):
                ball.set_velocity(left_up)
            elif(ball_direction.get_x() == right_up.get_x() and ball_direction.get_y() == right_up.get_y()):
                ball.set_velocity(right_down)
            elif(ball_direction.get_x() == right_down.get_x() and ball_direction.get_y() == right_down.get_y()):
                ball.set_velocity(right_up)
        
        elif(ball.get_position().get_y()+1 == constants.MAX_Y):
            ball.set_text("")
            val = Point(0,0)
            ball.set_velocity(val)
