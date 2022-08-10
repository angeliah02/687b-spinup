/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       C:\Users\Andres P                                         */
/*    Created:      Mon Jun 20 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// LFM                  motor         1               
// LBM                  motor         10              
// RFM                  motor         11              
// RBM                  motor         20              
// inertialSensor       inertial      5               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"                    

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  
  while (true) {
    Chassis::driveControl();
  }
  
}
