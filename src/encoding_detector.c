#include "Python.h"
#include "unicode/ucsdet.h"
#include "magic.h"

static magic_t ch_magic;
static UCharsetDetector *ch_ucd;

int
charlockholmes_init_encodec()
{
    UErrorCode status = U_ZERO_ERROR;

    ch_magic = magic_open(MAGIC_NO_CHECK_SOFT);
    if (ch_magic == NULL) {
        PyErr_SetString(PyExc_StandardError, magic_error(ch_magic));
        return -1;
    }

    ch_ucd = ucsdet_open(&status);
    if (U_FAILURE(status)) {
        PyErr_SetString(PyExc_StandardError, u_errorName(status));
        return -1;
    }

    return 0;
}

PyObject *
charlockholmes_encodec_detect(PyObject *self, PyObject *args, PyObject *keywds)
{
    PyObject *content;
    const char *binary_result;
    UErrorCode status = U_ZERO_ERROR;
    const UCharsetMatch *match;
    const char *mname;
    const char *mlang;
    int mconfidence;

    if (!PyArg_ParseTuple(args, "S", &content)) {
        return NULL;
    }

    binary_result = magic_buffer(ch_magic, PyString_AsString(content), PyString_Size(content));

    if (binary_result) {
        if (!strstr(binary_result, "text")) {
            return Py_BuildValue("{ss,si}", "type", "binary", "confidence", 100);
        }
    } else {
        PyErr_SetString(PyExc_StandardError, magic_error(ch_magic));
        return NULL;
    }


    ucsdet_setText(ch_ucd, PyString_AsString(content), (int32_t)PyString_Size(content), &status);
    match = ucsdet_detect(ch_ucd, &status);
    if (match) {
        mname = ucsdet_getName(match, &status);
        mlang = ucsdet_getLanguage(match, &status);
        mconfidence = ucsdet_getConfidence(match, &status);
        if (mlang && mlang[0])
            return Py_BuildValue("{ss,ss,si,ss}",
                    "type", "text",
                    "encoding", mname,
                    "confidence", mconfidence,
                    "language", mlang);
        else
            return Py_BuildValue("{ss,ss,si}",
                    "type", "text",
                    "encoding", mname,
                    "confidence", mconfidence);
    }

    Py_INCREF(Py_None);
    return Py_None;
}
