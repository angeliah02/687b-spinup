/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       C:\Users\Andres P                                         */
/*    Created:      Fri May 13 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// LeftFrontMotor       motor         2               
// LeftBackMotor        motor         12              
// RightFrontMotor      motor         9               
// RightBackMotor       motor         19              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  
  // Continously Checks to see the inputs of the controller
  while(true)
  { 
    // Hands the calculations to go in all directions
 
    // Right Joystick Input
    int Right_Front = Controller1.Axis2.position() - Controller1.Axis1.position();
    int Left_Front = Controller1.Axis2.position() + Controller1.Axis1.position();
    int Right_Back = Controller1.Axis2.position() + Controller1.Axis1.position();    
    int Left_Back = Controller1.Axis2.position() - Controller1.Axis1.position();

    // Left Joystick Input
    int rot = Controller1.Axis4.position();

    // Checks to see if axises 4 is moved to rotate the robot
    if (rot < 0)
    {
      Right_Front = -rot;
      Left_Front = rot;
      Right_Back = -rot;   
      Left_Back = rot;
    }
    if (rot > 0)
    {
      Right_Front = -rot;
      Left_Front = rot;
      Right_Back = -rot;   
      Left_Back = rot;
    }

    // Sets the Motor Velocity using the variables above
    RightFrontMotor.setVelocity(Right_Front, percent);
    LeftFrontMotor.setVelocity(Left_Front, percent);
    RightBackMotor.setVelocity(Right_Back,percent);
    LeftBackMotor.setVelocity(Left_Back, percent);
     
    // Spins motors when prompted
    RightFrontMotor.spin(forward);
    LeftFrontMotor.spin(forward);    
    RightBackMotor.spin(forward);
    LeftBackMotor.spin(forward);
  }
}