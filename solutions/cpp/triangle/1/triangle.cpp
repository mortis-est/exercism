#include "triangle.h"

int main() {
  int triangleInput = 0;

  std::cout << "Please enter the size of side A on the triangle: ";
  std::cin >> triangleInput;
  
  triangle::validInt(triangleInput);
  std::cout << "You entered: " << triangleInput;

  return 0;
  
}
