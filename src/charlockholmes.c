#include "Python.h"

static PyObject *
charlockholmes_hi(PyObject *self, PyObject *args, PyObject *keywds)
{
    printf("Hello World\n");
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef charlockholmes_methods[] = {
    /* The cast of the function is necessary since PyCFunction values
     * only take two PyObject* parameters, and keywdarg_parrot() takes
     * three.
     */
    {"hi", (PyCFunction)charlockholmes_hi, METH_VARARGS | METH_KEYWORDS,
     "Print \"Hello World\"."},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

void
initcharlockholmes(void)
{
  /* Create the module and add the functions */
  Py_InitModule("charlockholmes", charlockholmes_methods);
}
