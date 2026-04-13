#pragma once
#include <iostream>

namespace triangle {

// Add a function that checks that input is greater a positive, non-zero integer
// will be re-used for each side of the triangle

  void invalidInput() {
    std::cout << "Invalid entry!\n";
  }

  bool validInt(int triSide) {
    if (std::isdigit(triSide)) {
      if ((triSide > 0) && (triSide != NULL) { return true; }

      else {
        invalidInput();
        std::cout << "Please enter a positive, non-zero, digit (or set of digits)..."
        
        return false;
      }
    }
    else {
      invalidInput();
      std::cout << "You must enter a value that only consists of digits.\nPlease try again...";
      
      return false;
    }
  }



}  // namespace triangle
