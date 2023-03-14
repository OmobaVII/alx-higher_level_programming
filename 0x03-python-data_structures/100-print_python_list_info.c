#include <Python.h>

/**
 * this includes the header file for object.h
 * and listobject.h
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, a;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);
		for (a = 0; a < size; a++)
		{
			printf("Element %zd: %s\n", a, Py_TYPE(PyList_GetItem(p, a))->tp_name);
		}
	}
}
