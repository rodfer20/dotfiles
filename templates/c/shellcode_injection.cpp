-- Pretty
void (*func)();
func = (void (*)()) code;
func();
-- One liner
(*(void(*)()) code)();

