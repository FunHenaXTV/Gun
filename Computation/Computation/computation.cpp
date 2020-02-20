#include <Python.h>
#include <Windows.h>
#include <cmath>
#include <string>

const double e = 2.7182818284590452353602874713527;

double sinh_impl(double x) {
	return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
}

double cosh_impl(double x) {
	return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x));
}

PyObject* tanh_impl(PyObject* self, PyObject* args) {
	double x, y, len;


	if (PyTuple_Size(args) != 3) {
		PyErr_SetString(self, "func_ret_str args error");
	}

	PyArg_ParseTuple(args, "ddd", &x, &y, &len);
	double tg = (250 - y) / x;
	double x1 = sqrt(len * len / (1 + tg * tg));
	double y1 = 250 - tg * x1;
	double sum = int(x1)*10000+int(y1);


	return (PyFloat_FromDouble(sum));
}

static PyMethodDef computation_methods[] = {
	// The first property is the name exposed to Python, fast_tanh, the second is the C++
	// function name that contains the implementation.
	{ "fast_tanh", (PyCFunction)tanh_impl, METH_VARARGS, nullptr },

	// Terminate the array with an object containing nulls.
	{ nullptr, nullptr, 0, nullptr }
};


static PyModuleDef computation_module = {
	PyModuleDef_HEAD_INIT,
	"computation",                        // Module name to use with Python import statements
	"Provides some functions, but faster",  // Module description
	0,
	computation_methods                   // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_computation() {
	return PyModule_Create(&computation_module);
}
