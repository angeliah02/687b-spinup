#include "vex.h"

using namespace vex;

void Chassis::setVel(double LF, double LB, double RF, double RB) {
  LFM.spin(fwd, LF, rpm);
  LBM.spin(fwd, LB, rpm);
  RFM.spin(fwd, RF, rpm);
  RBM.spin(forward,RB,rpm);
}

void Chassis::driveControl(){
  int xAxis = Controller1.Axis1.position() * 2;
  int yAxis = Controller1.Axis2.position() * 2;
  int turning = Controller1.Axis4.position() * 2;

  // Deadzone
  if (abs(Controller1.Axis1.position()) < 5) {xAxis = 0;}
  if (abs(Controller1.Axis2.position()) < 5) {yAxis = 0;}
  if (abs(Controller1.Axis4.position()) < 5) {turning = 0;}

  int leftF = yAxis + xAxis + turning;
  int leftB = yAxis - xAxis + turning;
  int rightF = yAxis - xAxis - turning;
  int rightB = yAxis + xAxis - turning;

  setVel(leftF, leftB, rightF, rightB);
}