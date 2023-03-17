#include <python.h>

/**
 * print_python_list - a function that prints some basic info about python lists
 * @p: the python list
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, a;
	const char *typename;

	size = Pylist_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %zd\n[*] Allocated = %zd\n", size, allocated);
		for (a = 0; a < size; a++)
		{
			typename = Py_TYPE(PyList_GET_ITEM(p, a))->tp_name;
			printf("Element %zd: %s\n", a, typename);
		}
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object");
	}
}

/**
 * print_python_bytes - a function that prints some basic info about python
 * byte objects
 * @p: the python object
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size;

	bytes_size = Pybytes_Size(p);
	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  size: %zu\n", bytes_size);
		printf("  trying string: %s\n", PyBytes_AS_STRING(p));
		for (i = 0; i < bytes_size; i++)
		{
			printf("  first %zu bytes: %02x ", bytes_size + 1, PyBytes_AS_STRING(p)[i]);
		}
		printf("\n");
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}

