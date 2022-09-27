#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = PyList_Size(p), i;
	PyTypeObject *type;

	if (PyList_CheckExact(p))
	{
		printf("[*] Size of the Python List = %lu\n", len);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < len; i++)
		{
			type = Py_TYPE(PyList_GetItem(p, i));
			printf("Element %lu: %s\n", i, type->tp_name);
		}
	}
}
