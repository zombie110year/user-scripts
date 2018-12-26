# Make PythonScript binary dist

Rm = rm
RmFlags = -rf

clean:
	cd build && $(Rm) $(RmFlags) *
	cd dist &&  $(Rm) $(RmFlags) *
.PHONY: clean
