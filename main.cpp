#include <pybind11/pybind11.h>
#include "library.h" // добавили инклюд

namespace py = pybind11;


PYBIND11_MODULE(library, m) {
    m.def("input", &input); // добавили функцию в модуль
    m.def("solve", &solve);
};