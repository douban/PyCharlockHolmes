#include "Python.h"
#include "charlockholmes.h"

static PyObject *
charlockholmes_hi(PyObject *self, PyObject *args, PyObject *keywds)
{
    printf("Hello World\n");
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef charlockholmes_methods[] = {
    {"hi", (PyCFunction)charlockholmes_hi, METH_VARARGS | METH_KEYWORDS,
        "Print \"Hello World\"."},
    {"detect", (PyCFunction)charlockholmes_encodec_detect, METH_VARARGS | METH_KEYWORDS,
        "Detect string encodec."},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

void
initcharlockholmes(void)
{
    /* Create the module and add the functions */
    Py_InitModule("charlockholmes", charlockholmes_methods);
    charlockholmes_init_encodec();
}
