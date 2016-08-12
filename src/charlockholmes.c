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

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "charlockholmes",     /* m_name */
    "",  /* m_doc */
    -1,                  /* m_size */
    charlockholmes_methods,    /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
};
#endif

#ifndef PyMODINIT_FUNC  /* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif

#if PY_MAJOR_VERSION >= 3
    #define MOD_INIT(name) PyMODINIT_FUNC PyInit_##name(void)
#else
    #define MOD_INIT(name) PyMODINIT_FUNC init##name(void)
#endif

MOD_INIT(charlockholmes)
{
    PyObject* m = NULL;

    /* Create the module and add the functions */
#if PY_MAJOR_VERSION >= 3
    m = PyModule_Create(&moduledef);
#else
    m = Py_InitModule("charlockholmes", charlockholmes_methods);
#endif
    charlockholmes_init_encodec();

#if PY_MAJOR_VERSION >= 3
    return m;
#endif
}
