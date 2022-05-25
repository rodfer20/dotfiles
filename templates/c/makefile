CXX = gcc
DEBUG = -g -Wall -Wextra
PROGGIE = proggie

.PHONY: main
main: src/$(PROGGIE).c 
	$(CXX) src/$(PROGGIE).c -o main_$(PROGGIE)

.PHONY: debug
debug: src/$(PROGGIE).c
	$(CXX) $(DEBUG) src/$(PROGGIE).c -o debug_$(PROGGIE) 2>debug_$(PROGGIE).log && gdb debug_$(PROGGIE)

.PHONY: run
run: src/$(PROGGIE).c
	$(CXX) src/$(PROGGIE).c -o main_$(PROGGIE) && ./main_$(PROGGIE)

.PHONY: test
test: main_$(PROGGIE)
	echo "No tests founds"

.PHONY: clean
clean:
	rm -f main_$(PROGGIE)
	rm -f debug_$(PROGGIE)
	rm -f debug_$(PROGGIE).log
